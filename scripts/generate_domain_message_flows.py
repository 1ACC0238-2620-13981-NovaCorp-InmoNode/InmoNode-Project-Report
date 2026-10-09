"""Generate the report tables and vector/raster diagrams from one message definition.

Run from any directory: python scripts/generate_domain_message_flows.py [--check]
Requires Pillow. --check compares generated artifacts without writing files.
"""

from __future__ import annotations

import argparse
import io
import math
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont
from domain_flow_html import html_outputs


ROOT = Path(__file__).resolve().parents[1]
AGENT = "Agente Comercial de Campo"
BUYER = "Comprador e Inversionista"
ADMIN = "Área administrativa / Back-office financiero"
CAT_ADMIN = "Administrador / Back-office de Catálogo"
FIELD = "Gestión Comercial en Campo"
VOUCHER = "Gestión de Comprobantes"
VOUCHER_FIELD = "Gestión de Comprobantes (campo)"
VOUCHER_SERVER = "Gestión de Comprobantes (servidor)"
DIGITAL = "Cotización y Separación Digital"
FINANCE = "Control Financiero y Documental"
CATALOG = "Catálogo Inmobiliario"
CLOCK = "Planificador de vencimientos"


def message(step, sender, receiver, kind, name, data, condition):
    return dict(step=step, sender=sender, receiver=receiver, kind=kind,
                name=name, data=data, condition=condition)


def flow(code, title, participants, note, messages):
    return dict(code=code, title=title, participants=participants, note=note,
                messages=[message(*row) for row in messages])


FLOWS = [
    flow("1A", "Registro comercial local", [AGENT, FIELD, VOUCHER],
         "Disponibilidad local: permite registrar una intención; no garantiza el bloqueo central del lote.", [
        ("1", AGENT, FIELD, "Consulta", "Consultar disponibilidad y ficha del lote", "lotId.", "El prospecto solicita información sobre un lote."),
        ("2", FIELD, AGENT, "Respuesta", "Disponibilidad y ficha local del lote", "lotId, projectId, estado local, área, precio, moneda y fecha de actualización del catálogo.", "Se consulta la copia descargada; puede estar desactualizada."),
        ("3", AGENT, FIELD, "Comando", "Registrar prospecto", "prospectId, documento, nombre y datos de contacto.", "El identificador se genera en el dispositivo, incluso sin conexión."),
        ("4", FIELD, AGENT, "Respuesta", "Prospecto registrado", "prospectId y estado de sincronización pendiente.", "El registro cumple los datos obligatorios."),
        ("5", AGENT, FIELD, "Comando", "Registrar separación de lote", "reservationId, lotId, prospectId, agentId, precio acordado, inicial, moneda, plazo y tasa.", "El lote figura disponible localmente y las condiciones acordadas son válidas."),
        ("6", FIELD, VOUCHER, "Evento", "Lote separado", "reservationId, lotId y prospectId; reservationId será el operationId de la evidencia.", "Se guarda una separación local provisional; no una reserva central confirmada."),
    ]),
    flow("1B", "Captura y revisión de la evidencia en campo", [AGENT, VOUCHER],
         "Si la imagen es ilegible, se repite la captura. Los pasos 5–6 solo se ejecutan si hay correcciones.", [
        ("1", AGENT, VOUCHER, "Comando", "Capturar voucher de pago", "voucherId, imagen y operationId = reservationId de campo.", "Existe una separación local a la que asociar la evidencia."),
        ("2", VOUCHER, AGENT, "Respuesta", "Resultado de captura del voucher", "voucherId, operationId y resultado de legibilidad; motivo si requiere recaptura.", "Una imagen ilegible vuelve al paso 1; solo una captura aceptada continúa."),
        ("3", VOUCHER, VOUCHER, "Comando", "Extraer datos del voucher", "voucherId e imagen aceptada.", "Procesamiento interno en el dispositivo, sin depender de conectividad."),
        ("4", VOUCHER, AGENT, "Respuesta", "Datos del voucher extraídos", "voucherId, monto, moneda, fecha y código de operación.", "El agente revisa la lectura; una falla de OCR habilita el ingreso manual."),
        ("5", AGENT, VOUCHER, "Comando", "Corregir datos del voucher", "voucherId, monto, moneda, fecha y código de operación corregidos.", "Opcional: la lectura automática es incorrecta o incompleta."),
        ("6", VOUCHER, AGENT, "Respuesta", "Datos del voucher corregidos", "voucherId, datos finales y marca de corrección manual.", "Se conservan los datos finales para la sincronización de evidencia."),
    ]),
    flow("1C", "Consolidación de campo y entrega de comprobantes", [FIELD, FINANCE, VOUCHER_FIELD, VOUCHER_SERVER],
         "2A y 2B son alternativas por reserva. Solo los vouchers de reservas sincronizadas continúan en 3–5.", [
        ("1", FIELD, FINANCE, "Comando", "Sincronizar registros pendientes", "Prospectos con prospectId y versión; reservas con reservationId, lotId, prospectId, agentId y condiciones acordadas.", "Se recupera conectividad; se valida el lote completo antes de conciliar cada reserva."),
        ("2A", FINANCE, FIELD, "Evento", "Registros sincronizados", "reservationId, lotId, resultado de consolidación y fecha; confirmación individual de prospectos.", "El lote admite el bloqueo central; se confirma esa reserva sin duplicar reenvíos."),
        ("2B", FINANCE, FIELD, "Evento", "Conflicto de disponibilidad detectado", "reservationId, lotId y motivo de conflicto.", "Alternativa a 2A: el lote ya está tomado; el prospecto se conserva y se informa al agente."),
        ("3", VOUCHER_FIELD, VOUCHER_SERVER, "Comando", "Sincronizar comprobantes de campo", "voucherId, operationId, monto, moneda, fecha, código de operación, archivo, tipo y marca de corrección.", "La reserva local ya está sincronizada; las reservas en conflicto no envían vouchers."),
        ("4", VOUCHER_SERVER, VOUCHER_FIELD, "Respuesta", "Comprobantes registrados en servidor", "Resultado por voucherId y estado de recepción; los no confirmados permanecen pendientes.", "Se conserva cada voucher y su entrega pendiente; repetir voucherId no crea otra evidencia."),
        ("5", VOUCHER_SERVER, FINANCE, "Evento", "Comprobante de pago recibido", "voucherId, operationId, canal FIELD, monto, moneda, fecha, código, archivo, tipo, corrección y receivedAt.", "La evidencia queda disponible para revisión; si aún no existe su reserva, se retiene por operationId."),
    ]),
    flow("2A", "Exploración y cotización web", [BUYER, DIGITAL, FINANCE],
         "La consulta de exhibición no autoriza una reserva. El bloqueo se valida de nuevo en el subflujo 2B.", [
        ("1", BUYER, DIGITAL, "Consulta", "Consultar proyectos y lotes disponibles", "projectId opcional y filtros de área, precio o ubicación.", "El comprador explora alternativas desde el portal."),
        ("2", DIGITAL, FINANCE, "Consulta", "Consultar catálogo y disponibilidad central", "Proyecto y filtros solicitados.", "Cotización consume la fuente central y traduce el resultado a su propio modelo."),
        ("3", FINANCE, DIGITAL, "Respuesta", "Catálogo y disponibilidad central", "Proyectos, lotId, estado, área, precio, moneda, ubicación y polígono.", "Se obtiene información de exhibición; la disponibilidad puede cambiar después."),
        ("4", DIGITAL, BUYER, "Respuesta", "Proyectos y lotes para evaluación", "Ficha de proyecto, lotId, precio, moneda, ubicación y disponibilidad informada.", "Se presenta el resultado de la consulta iniciada en 1."),
        ("5", BUYER, DIGITAL, "Comando", "Simular financiamiento", "lotId, cuota inicial y plazo.", "Se valida la inicial mínima vigente; 20 % es el valor por defecto documentado, configurable."),
        ("6", DIGITAL, BUYER, "Respuesta", "Presentar simulación de financiamiento", "quotationId, lotId, precio, moneda, inicial, plazo, tasa, cronograma y vigencia; o motivo de rechazo.", "Una simulación válida registra la cotización; una inicial insuficiente requiere ajustar los datos."),
    ]),
    flow("2B", "Solicitud web y autorización del bloqueo", [BUYER, DIGITAL, FINANCE, VOUCHER],
         "Ruta aceptada: 1 → 2 → 3A → 4A → 5A. Ruta rechazada: 1 → 2 → 3B → 4B. No se ejecutan ambas.", [
        ("1", BUYER, DIGITAL, "Comando", "Solicitar separación de lote", "lotId, quotationId, perfil del comprador y clave de la intención de solicitud.", "La cotización corresponde al comprador y lote, y sigue vigente; se fija requestId antes del bloqueo."),
        ("2", DIGITAL, FINANCE, "Comando", "Solicitar bloqueo temporal del lote", "requestId, lotId, cuenta y perfil del comprador, quotationId, condiciones acordadas y vigencia de una hora.", "La autoridad central resuelve la concurrencia; un reintento conserva el mismo requestId."),
        ("3A", FINANCE, DIGITAL, "Respuesta", "Bloqueo temporal confirmado", "requestId, referencia de reserva central, lotId y blockedUntil.", "El lote estaba disponible; las condiciones financieras quedan congeladas en la reserva."),
        ("3B", FINANCE, DIGITAL, "Respuesta", "Bloqueo rechazado por indisponibilidad", "requestId, lotId y motivo de indisponibilidad.", "Alternativa a 3A: otro actor ya bloqueó o adquirió el lote."),
        ("4A", DIGITAL, VOUCHER, "Evento", "Solicitud de separación registrada", "requestId, lotId y referencia de reserva; requestId será el operationId de la evidencia.", "Solo después de 3A: la solicitud queda bloqueada y habilita la asociación del comprobante."),
        ("5A", DIGITAL, BUYER, "Respuesta", "Solicitud de separación confirmada", "requestId, lotId, estado y blockedUntil.", "Se comunica el plazo disponible para entregar la evidencia."),
        ("4B", DIGITAL, BUYER, "Respuesta", "Solicitud de separación rechazada", "requestId, lotId, estado de rechazo y motivo.", "Solo después de 3B: no se publica el evento 4A ni se habilita una reserva inexistente."),
    ]),
    flow("2C", "Recepción web y espera de verificación", [BUYER, VOUCHER, FINANCE],
         "La recepción de evidencia no aprueba el pago. Su puntualidad se determina por receivedAt.", [
        ("1", BUYER, VOUCHER, "Comando", "Adjuntar comprobante de pago", "operationId = requestId, archivo y tipo, monto, moneda, fecha y código de operación declarados.", "El comprador entrega evidencia para su solicitud; el canal web no realiza OCR."),
        ("2", VOUCHER, BUYER, "Respuesta", "Comprobante registrado", "voucherId, operationId y receivedAt; o motivo de rechazo de la carga.", "Archivo y datos válidos; un reintento de la misma carga devuelve el mismo voucherId."),
        ("3", VOUCHER, FINANCE, "Evento", "Comprobante de pago recibido", "voucherId, operationId, canal WEB, monto, moneda, fecha, código, archivo, tipo y receivedAt.", "Se comunica evidencia persistida; la entrega puede ocurrir después de la confirmación al comprador."),
        ("4", FINANCE, BUYER, "Evento", "Lote en espera de verificación financiera", "reservationId, lotId y estado pendiente de verificación.", "Se asocia evidencia recibida a tiempo a la reserva; aún no habilita la emisión del contrato."),
    ]),
    flow("2D", "Aprobación financiera y emisión contractual", [ADMIN, FINANCE, DIGITAL, BUYER],
         "La aprobación habilita la emisión. El contrato preliminar y la firma legal son hechos distintos.", [
        ("1", ADMIN, FINANCE, "Comando", "Aprobar comprobante de pago", "reservationId, voucherId, reviewerId y nota de verificación.", "US-54: se contrasta monto, cuenta y plazo; la evidencia aprobada debe cubrir la inicial acordada."),
        ("2", FINANCE, ADMIN, "Respuesta", "Resultado de verificación financiera", "voucherId, reservationId y decisión; reserva verificada si la evidencia cubre la inicial.", "Se conserva la revisión; solo una reserva verificada continúa con la emisión."),
        ("3", ADMIN, FINANCE, "Comando", "Emitir contrato preliminar", "reservationId y datos o documentos contractuales requeridos.", "La reserva está verificada; se usan sus condiciones financieras congeladas."),
        ("4", FINANCE, DIGITAL, "Consulta", "Consultar plan de financiamiento de cotización", "quotationId de la reserva web.", "Se recupera el cronograma pactado para generar el estado de cuenta del contrato."),
        ("5", DIGITAL, FINANCE, "Respuesta", "Plan de financiamiento de la cotización", "quotationId, precio, moneda, inicial, plazo, tasa e importes del cronograma.", "Se devuelve el plan aunque la cotización haya vencido; las fechas reales parten de la emisión."),
        ("6", FINANCE, BUYER, "Evento", "Contrato emitido", "contractId, reservationId y referencias del contrato preliminar y anexos.", "El back-office emite el contrato después de verificar el pago; habilita la consulta en 2G."),
    ]),
    flow("2E", "Rechazo financiero y comprobante sustituto", [ADMIN, FINANCE, BUYER, VOUCHER],
         "Un sustituto tiene nuevo voucherId y el mismo operationId. La evidencia previa se conserva.", [
        ("1", ADMIN, FINANCE, "Comando", "Rechazar comprobante de pago", "reservationId, voucherId, reviewerId y motivo.", "US-54: la evidencia no corresponde al monto, cuenta o plazo esperado."),
        ("2", FINANCE, ADMIN, "Respuesta", "Resultado del rechazo financiero", "voucherId, decisión, motivo y resubmissionDeadline cuando corresponde.", "La reserva pasa a rechazada solo si no está verificada ni tiene otra evidencia pendiente o aprobada."),
        ("3", BUYER, FINANCE, "Consulta", "Consultar decisión sobre comprobantes", "reservationId de una operación accesible a la cuenta.", "El comprador consulta el resultado sin necesitar un contrato emitido."),
        ("4", FINANCE, BUYER, "Respuesta", "Decisión financiera y plazo de subsanación", "voucherId, decisión, motivo, estado de reserva y plazo de subsanación; 24 horas por defecto, configurable.", "Se habilita el sustituto cuando la reserva requiere subsanación."),
        ("5", BUYER, VOUCHER, "Comando", "Adjuntar comprobante sustituto", "Nuevo voucherId, mismo operationId, archivo, monto, moneda, fecha y código de operación.", "La nueva evidencia se recibe antes del plazo de subsanación."),
        ("6", VOUCHER, FINANCE, "Evento", "Comprobante de pago recibido", "Nuevo voucherId, operationId, datos completos del comprobante y receivedAt.", "La evidencia se incorpora al historial; nunca se reemplaza ni se pierde la anterior."),
        ("7", FINANCE, BUYER, "Evento", "Lote en espera de verificación financiera", "reservationId, lotId y estado pendiente de verificación.", "El sustituto puntual devuelve la reserva a revisión; retoma 2D o un nuevo rechazo."),
    ]),
    flow("2F", "Vencimiento y eventual restablecimiento", [CLOCK, FINANCE, DIGITAL, BUYER, VOUCHER],
         "Vencimiento: 1 → 2 → 5 → 6A. Si llega evidencia puntual con retraso: 1 → 2 → 3 → 4 → 5 → 6B.", [
        ("1", CLOCK, FINANCE, "Comando", "Liberar bloqueos vencidos", "Instante de evaluación y plazos de bloqueo o subsanación.", "El plazo más el margen de entrega venció y no hay evidencia retenida; no expira una reserva verificada."),
        ("2", FINANCE, DIGITAL, "Evento", "Reserva expirada", "reservationId, lotId, canal WEB, sourceEventId = requestId y fecha del hecho.", "Se libera el lote y Cotización marca la solicitud como expirada."),
        ("3", VOUCHER, FINANCE, "Evento", "Comprobante de pago recibido", "voucherId, operationId = requestId, datos de la evidencia y receivedAt original.", "Opcional: entrega retrasada de evidencia guardada antes del vencimiento; la reserva ya está expirada."),
        ("4", FINANCE, DIGITAL, "Evento", "Reserva restablecida", "reservationId, lotId, requestId, voucherId y fecha del hecho.", "Solo después de 3 si el lote sigue disponible; la reserva vuelve a revisión financiera."),
        ("5", BUYER, DIGITAL, "Consulta", "Consultar estado de solicitud de separación", "requestId de la solicitud.", "El comprador revisa el resultado de su solicitud."),
        ("6A", DIGITAL, BUYER, "Respuesta", "Solicitud expirada", "requestId, estado expirado y motivo.", "Después de 2, si no hubo restablecimiento."),
        ("6B", DIGITAL, BUYER, "Respuesta", "Solicitud con bloqueo restablecido", "requestId y estado de bloqueo restablecido.", "Alternativa a 6A después de 4; la revisión financiera continúa en el contexto financiero."),
    ]),
    flow("2G", "Consulta contractual y estado de cuenta", [BUYER, FINANCE],
         "Las consultas devuelven información de operaciones autorizadas; no cambian el estado del lote.", [
        ("1", BUYER, FINANCE, "Consulta", "Consultar contrato digital", "contractId de una operación accesible a la cuenta.", "El contrato ya fue emitido."),
        ("2", FINANCE, BUYER, "Respuesta", "Contrato digital y anexos", "contractId, versión, estado y referencias de los documentos disponibles.", "Se entrega el preliminar o la versión firmada que corresponda al estado contractual."),
        ("3", BUYER, FINANCE, "Consulta", "Consultar estado de cuenta", "accountStatementId de la adquisición autorizada.", "Existe un estado de cuenta generado para el contrato."),
        ("4", FINANCE, BUYER, "Respuesta", "Estado de cuenta del comprador", "Importe programado de cuotas, pagos a cuotas, saldo con mora, cronograma y avance de pago.", "La inicial ya verificada no se suma de nuevo; el avance excluye la mora, según 2.6.4."),
    ]),
    flow("3", "Alta y publicación del inventario inmobiliario", [CAT_ADMIN, CATALOG, FINANCE],
         "Publicar la ficha y disponer del lote centralmente son hitos distintos. La disponibilidad pertenece a Control.", [
        ("1", CAT_ADMIN, CATALOG, "Comando", "Crear proyecto", "Nombre, ubicación y etapas con sus identificadores.", "El administrador inicia el alta de un proyecto."),
        ("2", CATALOG, CAT_ADMIN, "Respuesta", "Proyecto registrado", "projectId, etapas y estado inicial.", "Los datos obligatorios son válidos."),
        ("3", CATALOG, FINANCE, "Evento", "Proyecto creado", "projectId, nombre, ubicación y etapas con id, número y nombre.", "Se registra la proyección del proyecto; Control no adquiere autoridad sobre su alta."),
        ("4", CAT_ADMIN, CATALOG, "Comando", "Crear lote", "projectId, stageId, código, dimensiones, precio, moneda y polígono catastral.", "El proyecto y la etapa existen."),
        ("5", CATALOG, CAT_ADMIN, "Respuesta", "Lote registrado", "lotId, projectId y estado no publicado.", "La ficha del lote cumple los datos obligatorios."),
        ("6", CAT_ADMIN, CATALOG, "Comando", "Publicar lote al catálogo", "lotId del lote a publicar.", "Proyecto asociado, polígono y precio base están completos y válidos."),
        ("7", CATALOG, FINANCE, "Evento", "Lote publicado en catálogo", "lotId, projectId, stageId, código, área, precio, moneda, polígono y publishedAt.", "La ficha publicada permite incorporar el lote, conservando el lotId de origen."),
        ("8", CATALOG, FINANCE, "Evento", "Proyecto activado", "projectId y activatedAt.", "Solo si este es el primer lote publicado del proyecto; actualiza su proyección."),
        ("9", FINANCE, FINANCE, "Comando", "Incorporar lote publicado al inventario", "Ficha completa recibida en 7 y lotId canónico.", "Se aplica el alta sin duplicar lotes; entonces el inventario central queda disponible para bloqueo."),
    ]),
]


GROUPS = [
    dict(number=1, table="2.64", figure="2.25", title="Separación de lote en campo, evidencia y sincronización",
         codes=["1A", "1B", "1C"],
         intro="El agente registra un prospecto y una separación provisional con las condiciones financieras acordadas, captura la evidencia y, al recuperar conectividad, consolida primero la reserva y después sus comprobantes. El cierre comercial de campo es una reserva sincronizada o un conflicto comunicado; entregar la evidencia inicia una revisión financiera posterior.",
         end="Control Financiero y Documental es la única autoridad sobre la disponibilidad central. Ante conflicto, Gestión Comercial en Campo conserva el prospecto y marca la reserva en conflicto; sus vouchers permanecen visibles localmente y no se envían como si la reserva estuviera confirmada. Una falla técnica mantiene los registros pendientes para reintento. La validación estructural del lote de sincronización es completa; los conflictos de disponibilidad se resuelven individualmente por reserva.\n\nLa descarga de catálogo previa a la jornada tiene como proveedor a Control Financiero y Documental; el subflujo 1A consulta esa copia local. En 1C, campo y servidor son dos ubicaciones del mismo Bounded Context Gestión de Comprobantes. La correlación usa `operationId = reservationId` generado en el dispositivo. El servidor deduplica por `voucherId` y conserva el `receivedAt` original; si la evidencia llega antes que la reserva, la retiene por `operationId` y la adjunta cuando esta se consolida. La verificación, el rechazo y el contrato posteriores siguen las mismas reglas de 2D–2E, con el agente consultando sus decisiones y pudiendo aportar un sustituto desde campo; el plan de cuotas FIELD se calcula desde las condiciones acordadas, sin consultar una cotización web."),
    dict(number=2, table="2.65", figure="2.26", title="Cotización, separación web y seguimiento financiero-documental",
         codes=["2A", "2B", "2C", "2D", "2E", "2F", "2G"],
         intro="El comprador explora el catálogo, registra una cotización y solicita una separación. Cotización y Separación Digital pide a Control Financiero y Documental el bloqueo temporal; solo al confirmarse habilita la asociación de evidencia. La recepción del comprobante, su aprobación, la emisión del contrato y las consultas posteriores se modelan como escenarios distintos. Un bloqueo rechazado, una evidencia rechazada o un vencimiento tienen cierres propios.",
         end="En 2B, la cotización vigente se valida antes del bloqueo y sus condiciones quedan congeladas en la reserva. Una falla técnica deja la solicitud pendiente: el reintento reutiliza `requestId`, sin crear otra reserva. La consulta de exhibición de 2A nunca sustituye la autorización de bloqueo.\n\nLa evidencia web se correlaciona mediante `operationId = requestId`; `voucherId` identifica cada comprobante y permite conservar sustitutos sin duplicar reenvíos. El hecho **Comprobante de pago recibido** corresponde a `VoucherSyncedEvent` en 2.6.2. Los eventos dirigidos al comprador representan hechos visibles en el portal, sin asumir que el usuario consume un bus de mensajes. Los eventos internos `PaymentVerifiedEvent` y `PaymentRejectedEvent` permanecen en el contexto financiero; las respuestas y consultas muestran sus resultados.\n\nEn 2D se explicita la consulta inversa al plan de cotización prevista por el Context Map. Se conserva el cronograma pactado aunque la cotización ya haya vencido y se recalculan sus fechas desde la emisión contractual. El contrato preliminar no significa que el lote ya esté vendido ni que exista firma legal.\n\nEn 2E, el rechazo conserva el historial y solo abre subsanación si la reserva no está verificada ni mantiene otra evidencia pendiente o aprobada. El plazo por defecto es de 24 horas, configurable. El sustituto recibido a tiempo devuelve la reserva a revisión; una reserva ya verificada no retrocede por el rechazo de otra evidencia.\n\nEn 2F, **después del vencimiento del plazo más el margen de entrega**, y sin evidencia retenida, se libera el lote. El margen documentado es de 15 minutos, configurable. La puntualidad del comprobante depende de `receivedAt`, no de la hora de procesamiento. Una evidencia puntual entregada con retraso restablece la reserva si el lote sigue disponible; si otro comprador ya lo tomó, se conserva la evidencia y se abre revisión prioritaria para devolución. Una evidencia realmente tardía se conserva para revisión sin reabrir automáticamente la reserva. Estas condiciones también aplican al canal FIELD, cuyo agente consulta el resultado y actualiza su catálogo en la siguiente sincronización."),
    dict(number=3, table="2.66", figure="2.27", title="Alta de proyecto y publicación de lotes al catálogo",
         codes=["3"],
         intro="El administrador origina proyectos y lotes en Catálogo Inmobiliario. Este contexto publica la ficha y los hechos de creación y activación del proyecto; Control Financiero y Documental mantiene sus proyecciones e incorpora el lote como inventario canónico. El escenario termina cuando la incorporación central se ha aplicado, no únicamente cuando Catálogo emite la publicación.",
         end="Catálogo Inmobiliario decide la calidad y publicación de la ficha; Control Financiero y Documental decide disponibilidad, bloqueo, reserva y venta después de incorporarla. **Proyecto creado** y **Proyecto activado** corresponden a `ProjectCreatedEvent` y `ProjectActivatedEvent`; **Lote publicado en catálogo** corresponde a `LotPublishedToCatalogEvent`. El paso 9 explicita la reacción interna `OnboardLotFromCatalogCommand`, sin inventar un evento de confirmación externo. El paso 8 es condicional al primer lote publicado y no se repite por cada lote. Un alta incompleta o una publicación sin los datos requeridos se rechaza con su motivo y no produce los eventos de publicación. La recepción repetida de un mismo `lotId` no duplica el inventario."),
]


COLORS = {"Comando": ("#1857A4", "#EEF4FC"), "Consulta": ("#087D78", "#ECF8F5"),
          "Respuesta": ("#465466", "#F1F4F7"), "Evento": ("#7145AD", "#F4EFFA")}


class Drawing:
    """One set of layout primitives renders both PNG and editable SVG."""

    def __init__(self, width, height):
        self.width, self.height = width, height
        self.image = Image.new("RGB", (width, height), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
                    '<rect width="100%" height="100%" fill="white"/>']

    @staticmethod
    def font(size, bold=False):
        candidates = [Path("C:/Windows/Fonts") / ("segoeuib.ttf" if bold else "segoeui.ttf"),
                      Path("/usr/share/fonts/truetype/dejavu") / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")]
        for candidate in candidates:
            if candidate.exists():
                return ImageFont.truetype(str(candidate), size)
        return ImageFont.load_default(size=size)

    def wrap(self, value, width, size=23, bold=False):
        font = self.font(size, bold)
        lines = [""]
        for word in value.split():
            test = (lines[-1] + " " + word).strip()
            if font.getlength(test) <= width:
                lines[-1] = test
            else:
                assert font.getlength(word) <= width, f"Unbreakable text: {word}"
                lines.append(word)
        return lines

    def text(self, x, y, value, size=23, color="#233044", bold=False, centered=False):
        font = self.font(size, bold)
        assert y >= 0 and y + size + 6 <= self.height, f"Vertical overflow: {value}"
        length = font.getlength(value)
        left = x - length / 2 if centered else x
        assert left >= 0 and left + length <= self.width, f"Horizontal overflow: {value}"
        self.draw.text((left, y), value, font=font, fill=color, anchor="lt")
        self.svg.append(f'<text x="{x}" y="{y}" font-family="Segoe UI,DejaVu Sans,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}" dominant-baseline="text-before-edge" text-anchor="{"middle" if centered else "start"}">{escape(value)}</text>')

    def rect(self, x, y, w, h, fill, border=None, radius=10):
        self.draw.rounded_rectangle((x, y, x+w, y+h), radius, fill=fill, outline=border, width=2)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{border or "none"}" stroke-width="2"/>')

    def line(self, x1, y1, x2, y2, color, dashed=False, width=3):
        if dashed:
            length = math.hypot(x2-x1, y2-y1)
            for start in range(0, math.ceil(length), 16):
                end = min(start+9, length)
                if length:
                    self.draw.line((x1+(x2-x1)*start/length, y1+(y2-y1)*start/length,
                                    x1+(x2-x1)*end/length, y1+(y2-y1)*end/length), fill=color, width=width)
        else:
            self.draw.line((x1, y1, x2, y2), fill=color, width=width)
        self.svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"' + (' stroke-dasharray="9 7"' if dashed else '') + '/>')

    def arrowhead(self, x, y, direction, color):
        points = [(x, y), (x-direction*12, y-7), (x-direction*12, y+7)]
        self.draw.polygon(points, fill=color)
        self.svg.append('<polygon points="' + ' '.join(f'{a},{b}' for a,b in points) + f'" fill="{color}"/>')

    def arrow(self, x1, x2, y, kind):
        color = COLORS[kind][0]
        dashed = kind in ("Evento", "Respuesta")
        if x1 == x2:
            self.line(x1, y-12, x1+60, y-12, color, dashed)
            self.line(x1+60, y-12, x1+60, y+12, color, dashed)
            self.line(x1+60, y+12, x1, y+12, color, dashed)
            self.arrowhead(x1, y+12, -1, color)
        else:
            self.line(x1, y, x2, y, color, dashed)
            self.arrowhead(x2, y, 1 if x2 > x1 else -1, color)


def render_flow(item):
    width = 1600
    measuring = Drawing(width, 100)
    layouts = []
    for row in item["messages"]:
        label = f'{item["code"]}.{row["step"]}  ·  {row["kind"]}  ·  {row["name"]}'
        title = measuring.wrap(label, width-160, 25, True)
        data = measuring.wrap("Datos: " + row["data"], width-160, 23)
        condition = measuring.wrap("Condición: " + row["condition"], width-160, 22)
        height = 74 + len(title)*34 + len(data)*31 + len(condition)*30
        layouts.append((title, data, condition, height))
    note = measuring.wrap(item["note"], width-100, 23)
    header = 255
    height = header + sum(x[3] for x in layouts) + len(note)*32 + 80
    canvas = Drawing(width, height)
    canvas.text(50, 25, "DOMAIN MESSAGE FLOW  /  " + item["code"], 20, "#627086", True)
    canvas.text(50, 61, item["title"], 34, bold=True)
    canvas.text(50, 115, "Comando: acción   ·   Consulta: información   ·   Respuesta: resultado   ·   Evento: hecho ocurrido", 21, "#627086")
    participants = item["participants"]
    centers = {p: 200 + i*(width-400)/(len(participants)-1) for i,p in enumerate(participants)}
    box_width = min(340, (width-100)/len(participants)-18)
    actors = {AGENT, BUYER, ADMIN, CAT_ADMIN, CLOCK}
    for participant, center in centers.items():
        actor = participant in actors
        canvas.rect(center-box_width/2, 159, box_width, 80, "#EAF1FB" if actor else "#F5F2EC", "#CBD4DF")
        lines = canvas.wrap(participant, box_width-22, 22, True)
        for index, line in enumerate(lines):
            canvas.text(center, 165+index*24, line, 22, bold=True, centered=True)
        canvas.line(center, 240, center, height-len(note)*32-55, "#DAE0E7", True, 1)
    y = header
    for row, (title, data, condition, block_height) in zip(item["messages"], layouts):
        canvas.arrow(centers[row["sender"]], centers[row["receiver"]], y+18, row["kind"])
        canvas.rect(50, y+39, width-100, block_height-53, COLORS[row["kind"]][1], radius=8)
        position = y+49
        for line in title:
            canvas.text(75, position, line, 25, COLORS[row["kind"]][0], True)
            position += 34
        for line in data:
            canvas.text(75, position, line, 23)
            position += 31
        for line in condition:
            canvas.text(75, position, line, 22, "#526074")
            position += 30
        y += block_height
    for index, line in enumerate(note):
        canvas.text(50, y+20+index*32, line, 23, "#526074")
    canvas.svg.append('</svg>')
    png = io.BytesIO()
    canvas.image.save(png, format="PNG", optimize=True)
    return png.getvalue(), ("\n".join(canvas.svg)+"\n").encode("utf-8")


def section_markdown():
    content = ["#### 2.5.1.2. Domain Message Flows Modeling", "",
        "Los Domain Message Flows representan los comandos, eventos y consultas intercambiados entre actores, Bounded Contexts y sistemas para un escenario de negocio. Se aplica la técnica [Domain Message Flow Modelling de DDD Crew](https://github.com/ddd-crew/domain-message-flow-modelling), relacionada con Domain Storytelling, pero con énfasis explícito en el nombre, orden y datos significativos de cada mensaje.", "",
        "Los tres recorridos generales se dividen en subflujos de 4 a 9 mensajes para facilitar su lectura. Las tablas y figuras utilizan los mismos identificadores, participantes, nombres y datos. **Comando** solicita una acción; **consulta** solicita información; **respuesta** devuelve el resultado; **evento** comunica un hecho ya ocurrido. Cada consulta muestra su respuesta. Las flechas siguen emisor → receptor; un retorno al mismo participante indica una acción interna. Los mensajes de un subflujo se leen por su número y los sufijos A/B indican rutas alternativas, según su condición, no pasos que deban ejecutarse juntos.", "",
        "Los nombres describen contratos de negocio sin imponer transporte ni asincronía. Las condiciones de conectividad, legibilidad y tiempo se muestran como condiciones del flujo; no se confunden con eventos de negocio. El Context Map de 2.5.2 y las reglas de 2.6 determinan la autoridad sobre cada decisión. Los subflujos son recortes de escenarios: no incluyen todas las funciones del sistema.", "",
        "**[Abrir todos los flujos paso a paso en HTML](../assets/cap2/domain-message-flows/index.html).** Cada subflujo tiene una versión interactiva para avanzar, retroceder y revisar emisor, receptor, mensaje, datos y condición. Las rutas alternativas se seleccionan por separado. Los HTML funcionan directamente en el navegador, sin servidor; en GitHub, descarga el archivo HTML y ábrelo para usar los controles.", ""]
    by_code = {item["code"]: item for item in FLOWS}
    for group in GROUPS:
        content += [f'**Escenario {group["number"]}: {group["title"]}**', "", group["intro"], "",
                    f'La [Tabla {group["table"]}](#tabla-{group["table"].replace(".", "-")}) detalla los mensajes de cada subflujo; la [Figura {group["figure"]}](#figura-{group["figure"].replace(".", "-")}) los representa con la misma numeración.', "",
                    f'<a id="tabla-{group["table"].replace(".", "-")}"></a>', "", f'**Tabla {group["table"]}**', "",
                    f'*Mensajes de {group["title"].lower()}*', ""]
        for code in group["codes"]:
            item = by_code[code]
            content += [f'**Subflujo {code}: {item["title"]}**', "", item["note"], "",
                        "| Paso | Emisor | Receptor | Tipo | Mensaje | Datos significativos | Disparador o condición |",
                        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |"]
            for row in item["messages"]:
                values = [f'{code}.{row["step"]}', row["sender"], row["receiver"], row["kind"], row["name"], row["data"], row["condition"]]
                content.append("| " + " | ".join(values) + " |")
            content += [""]
        content += [group["end"], "", f'<a id="figura-{group["figure"].replace(".", "-")}"></a>', "",
                    f'**Figura {group["figure"]}**', "", f'*{group["title"]}: diagramas por subflujo*', ""]
        for code in group["codes"]:
            item = by_code[code]
            content += [f'**{code}. {item["title"]}**', "",
                        f'[Recorrer el subflujo {code} paso a paso en HTML](../assets/cap2/domain-message-flows/flow-{code}.html)', "",
                        f'![Subflujo {code}: {item["title"]}](../assets/cap2/domain-message-flows/flow-{code}.png)', ""]
        content += ["Las versiones vectoriales editables y el generador están disponibles en `assets/cap2/domain-message-flows/` y `scripts/generate_domain_message_flows.py`.", ""]
    return "\n".join(content) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    ids = set()
    for item in FLOWS:
        assert 4 <= len(item["messages"]) <= 9
        assert len(set(item["participants"])) == len(item["participants"])
        for index, row in enumerate(item["messages"]):
            identifier = item["code"] + "." + row["step"]
            assert identifier not in ids
            ids.add(identifier)
            assert row["sender"] in item["participants"] and row["receiver"] in item["participants"]
            assert row["kind"] in COLORS
            assert all(row.values()) and all("|" not in value for value in row.values())
            if row["kind"] == "Consulta":
                assert any(reply["kind"] == "Respuesta" and reply["sender"] == row["receiver"]
                           and reply["receiver"] == row["sender"] for reply in item["messages"][index+1:]), f"Missing query response: {identifier}"
    target = ROOT / "docs/Chapter-02.md"
    original = target.read_bytes()
    newline = "\r\n" if b"\r\n" in original else "\n"
    report = original.decode("utf-8").replace("\r\n", "\n")
    start = report.index("#### 2.5.1.2. Domain Message Flows Modeling\n")
    end = report.index("#### 2.5.1.3. Bounded Context Canvases\n", start)
    replacement = section_markdown()
    for item in FLOWS:
        expected_link = f'../assets/cap2/domain-message-flows/flow-{item["code"]}.png'
        assert replacement.count(expected_link) == 1
    for group in GROUPS:
        for number, prefix in ((group["table"], "tabla"), (group["figure"], "figura")):
            anchor = f'{prefix}-{number.replace(".", "-")}'
            assert replacement.count(f'<a id="{anchor}">') == 1
            assert f'](#{anchor})' in replacement
    report = report[:start] + replacement + report[end:]
    report = report.replace("Domain Storytelling representa la colaboración entre contextos en escenarios de mayor valor", "Domain Message Flow Modelling representa los mensajes intercambiados entre actores y contextos en escenarios de mayor valor")
    outputs = {target: report.replace("\n", newline).encode("utf-8")}
    directory = ROOT / "assets/cap2/domain-message-flows"
    for filename, content in html_outputs(FLOWS, GROUPS).items():
        outputs[directory / filename] = content
    for item in FLOWS:
        png, svg = render_flow(item)
        outputs[directory / f'flow-{item["code"]}.png'] = png
        outputs[directory / f'flow-{item["code"]}.svg'] = svg
    mismatches = []
    for path, data in outputs.items():
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                mismatches.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            if not path.exists() or path.read_bytes() != data:
                path.write_bytes(data)
    if mismatches:
        raise SystemExit("Generated artifacts differ: " + ", ".join(mismatches))
    print(f'{"Verified" if args.check else "Generated"}: {len(FLOWS)} diagrams and HTML walkthroughs, {len(ids)} messages, 3 report tables; PNG/SVG/HTML and Markdown share one definition.')


if __name__ == "__main__":
    main()
