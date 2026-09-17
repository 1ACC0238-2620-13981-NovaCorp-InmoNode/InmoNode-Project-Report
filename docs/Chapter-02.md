# Capítulo II: Requirements Development and Software Solution Design

## 2.1. Competidores

En el contexto actual del ecosistema inmobiliario y PropTech, existen diversas plataformas que abordan la gestión comercial y operativa desde distintos enfoques tecnológicos. A continuación, se presentan los principales competidores de InmoNode, considerando su propuesta de valor y alcance funcional:

- **HubSpot CRM:** El líder global en automatización de marketing y gestión de clientes. Su principal fortaleza radica en la integración multicanal y analítica avanzada de embudos de venta, aunque carece de operatividad sin internet y requiere un alto grado de personalización para adaptarse a la venta de lotes.
- **AppFolio:** Corporación global de software PropTech enfocada en la gestión de carteras y administración de propiedades a gran escala. Destaca por su ecosistema impulsado por IA y flujos de trabajo corporativos, pero su arquitectura centralizada y altos costos excluyen a promotoras emergentes y operativas de campo en zonas desconectadas.
- **Wasi CRM:** Plataforma masiva en Latinoamérica enfocada en el efecto de red y la bolsa inmobiliaria compartida entre corredores. Facilita la adopción rápida mediante planes de suscripciones; sin embargo, no considera la digitalización automatizada de pagos ni la sincronización offline necesarias para los procesos de habilitación urbana y comercialización de lotes.

Estas soluciones representan enfoques dependientes de la nube o genéricos, lo que evidencia una oportunidad para InmoNode de incorporar una resiliencia offline estricta, trazabilidad y gestión documental financiera, y agilidad operativa en el lugar de trabajo.

### 2.1.1. Análisis competitivo

<table border="1" cellspacing="0" cellpadding="5">
  <tr>
    <th colspan="7">Competitive Analysis Landscape</th>
  </tr>

  <tr>
    <td colspan="2" rowspan="2"><b>¿Por qué llevar a cabo este análisis?</b></td>
    <td colspan="5">
      Identificar las fortalezas, debilidades y oportunidades de las plataformas inmobiliarias y CRMs actuales, con el fin de comprender el posicionamiento de inmoNode dentro del nicho de venta de lotes y trabajo de campo.
    </td>
  </tr>
  <tr>
    <td colspan="5">
      Validar la ventaja de una arquitectura offline-first y la extracción de datos mediante OCR frente a infraestructuras genéricas dependientes de conectividad.
    </td>
  </tr>

   <tr>
    <td colspan="3"></td>
    <td align="center">
      <b>inmoNode</b><br>
      <img src="../assets/inmonode_logo.png" alt="inmoNode" height="80">
    </td>
    <td align="center">
      <b>HubSpot CRM</b><br>
      <img src="../assets/hubspot_logo.jpg" alt="HubSpot CRM" height="80">
    </td>
    <td align="center">
      <b>AppFolio</b><br>
      <img src="../assets/appfolio_logo.png" alt="AppFolio" height="80">
    </td>
    <td align="center">
      <b>Wasi CRM</b><br>
      <img src="../assets/wasi_logo.jpg" alt="Wasi CRM" height="80">
    </td>
  </tr>

  <tr>
    <td rowspan="2"><b>Perfil</b></td>
    <td colspan="2">Overview</td>
    <td>Plataforma PropTech offline-first que integra CRM, ventas en campo y digitalización OCR de comprobantes.</td>
    <td>Gigante tecnológico global de CRM y automatización de marketing (Inbound).</td>
    <td>Líder mundial en software PropTech para la gestión operativa de bienes raíces a gran escala.</td>
    <td>Plataforma masiva de gestión inmobiliaria y red de negocios (Brokerage Network).</td>
  </tr>

  <tr>
    <td colspan="2">Ventaja competitiva ¿Qué valor ofrece a los clientes?</td>
    <td>Procesamiento local, sincronización diferida y digitalización automatizada de vouchers in situ mediante OCR.</td>
    <td>Ecosistema masivo de integraciones omnicanal y análisis de marketing de primer nivel.</td>
    <td>Ecosistema unificado para gestionar operaciones y contabilidad corporativa de forma centralizada.</td>
    <td>Efecto de red masivo que permite a agentes compartir inventario instantáneamente en LATAM.</td>
  </tr>

  <tr>
    <td rowspan="2"><b>Perfil de Marketing</b></td>
    <td colspan="2">Mercado objetivo</td>
    <td>Agentes de campo, promotoras de lotes, empresas de habilitación urbana y analistas financieros.</td>
    <td>Empresas de múltiples sectores; en real estate, agencias con fuerte enfoque digital.</td>
    <td>Propietarios institucionales y grandes desarrolladores (principalmente en Norteamérica).</td>
    <td>Agentes independientes y pequeñas/medianas agencias dispersas en Latinoamérica.</td>
  </tr>

  <tr>
    <td colspan="2">Estrategias de marketing</td>
    <td>Enfoque B2B demostrando empíricamente la operatividad sin internet y la extracción ágil del OCR.</td>
    <td>Estrategia Inbound masiva, certificaciones gratuitas y modelo freemium agresivo.</td>
    <td>Venta consultiva corporativa basada en liderazgo tecnológico e integración de flujos de trabajo.</td>
    <td>Modelo de suscripción escalonado para captura en la base de la pirámide y capacitación digital.</td>
  </tr>

  <tr>
    <td rowspan="3"><b>Perfil de Producto</b></td>
    <td colspan="2">Productos & Servicios</td>
    <td>App móvil nativa con base de datos local, sincronización automatizada y motor OCR para comprobantes.</td>
    <td>Suite en la nube (Marketing, Sales, Service) con profunda personalización.</td>
    <td>Plataforma en la nube integral para gestión, mantenimiento y contabilidad avanzada.</td>
    <td>CRM web ligero, creador de páginas inmobiliarias y bolsa de propiedades compartidas.</td>
  </tr>

  <tr>
    <td colspan="2">Precios & Costos</td>
    <td>Modelo SaaS escalado por número de agentes de campo o por volumen de documentos procesados.</td>
    <td>Versión gratuita muy básica; escala a miles de dólares para automatización avanzada.</td>
    <td>Altos costos de licenciamiento (SaaS B2B corporativo) inalcanzables para pymes.</td>
    <td>Plan "Inicio" ($27 USD/mes) limitado y Plan "Pro" ($48 USD/mes) con funciones completas.</td>
  </tr>

  <tr>
    <td colspan="2">Canales de distribución (Web y/o Móvil)</td>
    <td>Aplicación móvil nativa optimizada para funcionamiento offline y portal web de gestión.</td>
    <td>Distribución eminentemente web (SaaS cloud-first).</td>
    <td>Plataforma web corporativa centralizada que requiere conectividad continua.</td>
    <td>Plataforma web y app móvil dependiente de conexión a red constante.</td>
  </tr>

  <tr>
    <td rowspan="5"><b>Análisis SWOT</b></td>
  </tr>

  <tr>
    <td colspan="2">Fortalezas</td>
    <td>Capacidad operativa ininterrumpida offline. Automatización de la extracción de datos (OCR).</td>
    <td>Integración omnicanal insuperable y capacidad de seguimiento del prospecto.</td>
    <td>Absoluto dominio en la gestión integral del activo corporativo y grandes portafolios.</td>
    <td>Enorme base de usuarios, interfaz probada y alta liquidez de inventario cruzado.</td>
  </tr>

  <tr>
    <td colspan="2">Debilidades</td>
    <td>Marca emergente sin trayectoria. Retos de legibilidad en el OCR ante vouchers deteriorados.</td>
    <td>Requiere semanas de configuración. Presenta limitaciones para operar sin conexión a internet.</td>
    <td>Alto costo. Orientado más a la administración de edificios que a las ventas de lotes en campo.</td>
    <td>Baja especialización técnica para flujos financieros; aplicación móvil sin capacidades offline reales.</td>
  </tr>

  <tr>
    <td colspan="2">Oportunidades</td>
    <td>Expansión de la habilitación urbana hacia zonas periurbanas sin cobertura de red.</td>
    <td>Agencias que buscan centralizar todo su pautaje digital en un solo panel.</td>
    <td>Consolidación de portafolios que demandan automatización para reportes gerenciales.</td>
    <td>Crecimiento de la economía gig impulsa la incursión de agentes libres.</td>
  </tr>

  <tr>
    <td colspan="2">Amenazas</td>
    <td>Inercia y resistencia tecnológica en el sector construcción para abandonar el papel.</td>
    <td>Proliferación de CRMs genéricos de bajo costo.</td>
    <td>Diferencias regulatorias en LATAM que dificultan estandarizar la contabilidad.</td>
    <td>Integración de catálogos y CRM directamente en aplicaciones como WhatsApp.</td>
  </tr>

</table>

### 2.1.2. Estrategias y tácticas frente a competidores

A partir del análisis competitivo y del análisis SWOT realizado, se definen estrategias y tácticas preliminares que permitirán a InmoNode afrontar las fortalezas de sus competidores, aprovechar sus debilidades y capitalizar las oportunidades del entorno, mitigando a su vez las amenazas del mercado.

#### Estrategias

- **Estrategia de diferenciación frente a fortalezas de competidores:**
  Mientras aplicaciones como HubSpot destacan por su marketing automatizado, AppFolio por su robustez corporativa y Wasi por su alcance masivo, InmoNode propone una diferenciación técnica basada en la resiliencia operativa (*offline-first*) y la digitalización móvil. Esto permite ofrecer una experiencia de trabajo en campo sin interrupciones, algo que las infraestructuras de la competencia no están orientadas a brindar de forma nativa.

- **Estrategia de aprovechamiento de debilidades del mercado:**
  Se identificó que los competidores presentan limitaciones funcionales significativas sin conexión a internet y dependen de la transcripción manual de los comprobantes de pago. InmoNode capitaliza esta debilidad integrando una base de datos local sólida y un motor OCR capaz de extraer la información de los vouchers en segundos directamente desde el dispositivo.

- **Estrategia de explotación de oportunidades:**
  El déficit habitacional ha desplazado los proyectos inmobiliarios hacia zonas periurbanas con baja o nula cobertura de red. InmoNode se posiciona estratégicamente como la herramienta indispensable de productividad ininterrumpida y trazabilidad documental frente a este escenario.

- **Estrategia de mitigación de amenazas:**
  Frente a la inercia institucional del sector y la presencia de marcas establecidas, se prioriza la venta consultiva demostrativa (pruebas empíricas de registro sin conexión) y una barrera de adopción mínima mediante un modelo de suscripción escalable, alineando el costo con la reducción de la fricción operativa del cliente.

#### Tácticas

- **Frente a fortalezas de competidores:**
    - Diseñar una interfaz móvil nativa de extrema fluidez que priorice la rapidez de captura de datos en el dispositivo por encima de menús corporativos complejos.
    - Incorporar herramientas de consulta de inventario local (ej. disponibilidad de lotes) accesibles incluso sin internet.

- **Frente a debilidades de competidores:**
    - Implementar un sistema de sincronización asíncrona que consolide los datos recolectados en campo hacia el repositorio web central tan pronto se recupere la señal.
    - Desarrollar un flujo de cámara optimizado para que el OCR extraiga el monto, fecha y código de operación del voucher, reduciendo el error de tipeo.

- **Frente a oportunidades del entorno:**
    - Crear contenido demostrativo enfocado en la eliminación del riesgo de pérdida de documentos físicos (vouchers de papel) y el ahorro de horas administrativas.
    - Promover pilotos operativos gratuitos directamente en los proyectos de lotización alejados de la ciudad.

- **Frente a amenazas del mercado:**
    - Garantizar la integridad de las transacciones registradas localmente mediante validaciones estructuradas antes de su sincronización a la nube.
    - Estructurar el portal web de modo que la integración inicial no requiera que la Inmobiliaria abandone por completo sus sistemas contables preexistentes, funcionando como un complemento de primera línea.

#### Enfoque estratégico

NovaCorp adopta con InmoNode una estrategia de especialización enfocada en el entorno físico de ventas. A diferencia de sus competidores, que abordan el sector desde el escritorio y la conectividad perpetua, InmoNode desplaza la autonomía operativa directamente al campo. Al combinar almacenamiento local robusto con la digitalización automatizada de comprobantes, la solución se posiciona como el pilar indispensable para el ciclo de venta en terrenos, resolviendo la fricción documental que los CRMs tradicionales no pueden atender por diseño.

## 2.2. Entrevistas

### 2.2.1. Diseño de entrevistas

#### Preguntas Demográficas y Contextuales (Todos los segmentos)
1. ¿Cuál es su nombre completo, edad, ocupación y distrito de residencia?

#### Preguntas para Segmento 1: Agentes Comerciales de Campo

1. ¿Cómo es un día típico de trabajo cuando acompañas a un cliente a visitar los terrenos en la zona del proyecto?
2. ¿Con qué frecuencia encuentras problemas de señal o cobertura móvil mientras estás mostrando lotes en campo?
3. Al estar parado en el terreno, ¿cómo verificas en tiempo real si un lote específico está disponible, separado o vendido? 
4. ¿Qué dificultades se te presentan al momento de mostrarle al cliente la ubicación exacta, dimensiones o linderos de una parcela?
5. ¿Cómo registras actualmente la separación de un lote o el recibo de un comprobante de pago cuando estás en el terreno?
6. ¿Qué sucede si recibes un voucher de depósito en físico o por foto en una zona sin internet? ¿Cómo evitas que se pierda o traspase?
7. ¿Cuánto tiempo tardas en enviar la información recolectada en campo a la oficina central para validar una reserva o pago?

#### Preguntas Principales para Segmento 2: Compradores e Inversionistas

1. Si estuvieras buscando invertir en un lote cerca a zonas de alto desarrollo, ¿cuáles son los primeros datos que buscarías en internet antes de contactar a un vendedor?
2. ¿Qué factores o elementos te transmiten mayor confianza al evaluar la compra de un terreno en planos?
3. En tus experiencias previas de compra o financiamiento, ¿qué tan fácil o difícil ha sido acceder a tus documentos legales (contratos, escrituras, cartas de separación)? 
4. ¿Te resultaría útil contar con un portal web donde puedas previsualizar y descargar tus documentos digitalizados en cualquier momento?
5. Si adquieres un lote al crédito, ¿cómo te gustaría visualizar el estado de tu cuenta, las cuotas pendientes y las alertas de vencimiento?
6. ¿Qué tan cómodo te sentirías adjuntando tus comprobantes de pago digitales a través de una plataforma web en lugar de enviarlos por correo o mensajería instantánea?
7. ¿Qué herramientas o secciones considerarías indispensables en una página web inmobiliaria para decidirte a solicitar una cotización formal?

### 2.2.2. Registro de entrevistas

#### Segmento 1: Agentes Comerciales de Campo

##### Entrevista 1
* **Nombre y Apellidos:** Azbel Capillo Varillas
* **Edad:** 42
* **Distrito:** Norte chico
* **URL del Video Evidencia:** [Entrevista 1](https://upcedupe-my.sharepoint.com/:v:/g/personal/u20241c101_upc_edu_pe/IQAxtrlWYi1wTo2_5Rs2I34mAZWtQH9UEHl9WsnKoMgTDMI?e=oiJRM2)
* **Timestamp de Inicio:** `hh:mm:ss`
* **Duración:** `11:58`

![Screenshot Entrevista 1](/assets/screenshot_entrevista1.png)

* **Resumen Descriptivo de la Entrevista:**
La entrevista realizada al supervisor comercial de campo expuso la dinámica operativa y las complejidades de atender visitas en proyectos urbanos con baja cobertura de red, donde el trayecto supera las 2 horas y la verificación de lotes depende de llamados verbales o grupos de WhatsApp coordinados desde Lima. Ante la desactualización de herramientas como Google Maps que solo muestran arenales, el equipo recurre a imágenes estáticas para proyectar el proyecto sin generar desconfianza en el comprador. En el plano financiero, la falta de equipamiento portátil obliga a emitir recibos provisionales a mano y recabar vouchers en papel térmico que suelen extraviarse o borrarse con rapidez. El entrevistado enfatizó que en las etapas iniciales de un proyecto o durante la incorporación de asesores junior, es muy común cometer errores por inexperiencia y falta de flujos estandarizados, tales como olvidar tomar fotografías del DNI, omitir la verificación del estado civil para la firma de cónyuges, o no registrar variaciones en la inicial y cuotas acordadas. Estos desaciertos iniciales provocan que el envío de información a la oficina y la emisión formal de la boleta o reserva se retrasen de 2 a 4 días debido a la necesidad de recontactar al cliente. Asimismo, el asesor experimenta el estrés constante de garantizar la seguridad de la transacción in situ, resolver la pérdida de comprobantes mediante conciliaciones bancarias manuales y mantener la fluidez de la venta sin depender de la señal móvil.
---

##### Entrevista 2
* **Nombre y Apellidos:**
* **Edad:**
* **Distrito:**
* **URL del Video Evidencia:**
* **Timestamp de Inicio:** `hh:mm:ss`
* **Duración:** `mm:ss`

![Screenshot Entrevista 2](/assets/screenshot_entrevista2.png)

* **Resumen Descriptivo de la Entrevista:**

La segunda entrevista realizada evidenció la dinámica diaria de guiar al cliente a través de la ruta, los alrededores y la ubicación estratégica del proyecto para transmitir el concepto inmobiliario. En cuanto a la conectividad, se resaltó la brecha de señal entre operadores, donde mientras la red principal del asesor se mantiene estable, la mayoría de competidores o clientes quedan incomunicados en el terreno. La verificación del inventario y el registro de ventas se gestionan mediante un grupo de WhatsApp, donde el asesor envía la fotografía del voucher de depósito con su descripción y el área correspondiente responde con el plano actualizado en el que se respeta la hora exacta de la transacción como respaldo en caso de falta de señal. No obstante, el principal problema operativo radica en la consulta de precios, linderos, metrajes, frentes, fondos y bonos de descuento, ya que contrastar el plano físico con las listas impresas demora la atención y ralentiza el cierre. Esta situación expone la necesidad de contar con una herramienta interactiva donde seleccionar un lote en el plano despliegue inmediatamente toda su ficha técnica y comercial, agilizando el flujo de cotización y asegurando la captura del comprobante sin depender exclusivamente de aplicaciones de mensajería instantánea. 

---

##### Entrevista 3
* **Nombre y Apellidos:**
* **Edad:**
* **Distrito:**
* **URL del Video Evidencia:**
* **Timestamp de Inicio:** `hh:mm:ss`
* **Duración:** `mm:ss`

![Screenshot Entrevista 3](/assets/screenshot_entrevista3.png)

* **Resumen Descriptivo de la Entrevista:**

---

#### Segmento 2: Compradores e Inversionistas

##### Entrevista 4
* **Nombre y Apellidos:** 
* **Edad:** 
* **Distrito:** 
* **URL del Video Evidencia:** 
* **Timestamp de Inicio:** `hh:mm:ss`
* **Duración:** `mm:ss`

![Screenshot Entrevista 4](/assets/screenshot_entrevista4.png)

* **Resumen Descriptivo de la Entrevista:**

---

##### Entrevista 5
* **Nombre y Apellidos:**
* **Edad:**
* **Distrito:**
* **URL del Video Evidencia:**
* **Timestamp de Inicio:** `hh:mm:ss`
* **Duración:** `mm:ss`

![Screenshot Entrevista 5](/assets/screenshot_entrevista5.png)

* **Resumen Descriptivo de la Entrevista:**


---

##### Entrevista 6
* **Nombre y Apellidos:**
* **Edad:**
* **Distrito:**
* **URL del Video Evidencia:**
* **Timestamp de Inicio:** `hh:mm:ss`
* **Duración:** `mm:ss`

![Screenshot Entrevista 6](/assets/screenshot_entrevista6.png)

* **Resumen Descriptivo de la Entrevista:**

### 2.2.3. Análisis de entrevistas

#### Segmento 1: Agentes Comerciales de Campo

#### Segmento 2: Compradores e Inversionistas

## 2.3. Needfinding

### 2.3.1. User Personas

### 2.3.2. User Task Matrix

### 2.3.3. User Journey Mapping

### 2.3.4. Empathy Mapping

### 2.3.5. Big Picture EventStorming

El equipo llevó a cabo una sesión colaborativa de Big Picture Event Storming utilizando la herramienta Miro, con el objetivo de explorar el dominio del negocio de la comercialización y gestión de lotes inmobiliarios a alto nivel. A diferencia de un flujo técnico o de registro de usuarios, el Big Picture Event Storming se enfoca en capturar el flujo de negocio completo que ocurre en el mundo real, desde la prospección y venta en el terreno hasta la conciliación financiera y emisión de contratos.

Durante la sesión, se identificaron los eventos significativos que ocurren en el ciclo de vida de la venta de un lote y la interacción con los distintos actores del ecosistema. El proceso permitió visualizar el flujo completo del negocio inmobiliario, exponiendo las relaciones entre los eventos clave, los actores involucrados (agente de campo, comprador, back-office, herramientas de IA y red) y las políticas de negocio que rigen el comportamiento del sistema.

A continuación, se presentan los principales elementos identificados en el Big Picture Event Storming:

**Domain Events (Eventos de Dominio):** Eventos en tiempo pasado que ocurren en el proceso de negocio.
*   Catalog Downloaded (Catálogo descargado)
*   Prospect Registered (Prospecto registrado)
*   Financing Simulated (Financiamiento simulado)
*   Lot Reserved (Lote separado)
*   Voucher Captured (Voucher fotográfico capturado)
*   Voucher Data Extracted (Datos del voucher extraídos)
*   Offline Data Synchronized (Datos offline sincronizados)
*   Concurrency Conflict Detected (Conflicto de concurrencia detectado)
*   Payment Reconciled (Pago financiero conciliado)
*   Digital Contract Generated (Contrato digital generado)
*   Contract Terms Accepted (Términos del contrato aceptados)
*   Installment Paid (Cuota mensual pagada)
*   Lot Fully Paid (Lote totalmente pagado)
*   Clearance Certificate Generated (Certificado de no adeudo generado)

**Actors (Actores):** Personas o sistemas que ejecutan comandos o generan eventos.
*   **Field Sales Agent (Agente Comercial de Campo)** - Actor principal que prospecta, cotiza, separa lotes y captura vouchers directamente en el terreno (con o sin internet).
*   **Buyer / Investor (Comprador / Inversionista)** - Actor que evalúa lotes, simula financiamientos de forma autónoma, firma contratos y realiza pagos de cuotas.
*   **Financial Back-Office (Back-Office Financiero)** - Actor administrativo que recibe las sincronizaciones, audita los vouchers y concilia los ingresos en las cuentas bancarias.
*   **OCR Engine (Motor OCR)** - Actor del sistema (IA) que procesa las imágenes de los vouchers para extraer automáticamente el monto, fecha y código de operación.
*   **Network Monitor (Monitor de Red)** - Actor del sistema que detecta las caídas y recuperaciones de conectividad a internet de los dispositivos móviles.

**Policies (Políticas):** Reglas de negocio que se disparan ante eventos específicos.
*   **When Network is Lost, trigger Offline Mode** (Cuando se pierde la conexión, disparar el almacenamiento en la base de datos local).
*   **When Network is Restored, trigger Automatic Synchronization** (Cuando se recupera la conexión, disparar la sincronización automática de las transacciones pendientes).
*   **When Voucher is Captured, trigger OCR Data Extraction** (Cuando se captura la foto de un comprobante, disparar la extracción de datos por visión artificial).
*   **When Offline Reservation Syncs and Lot is Sold, trigger Concurrency Alert** (Cuando una separación offline se sincroniza y el lote ya está vendido, disparar alerta de conflicto de concurrencia).
*   **When Payment is Reconciled, trigger Contract Generation** (Cuando el back-office concilia la separación, disparar la generación y visualización del contrato digital).
*   **When Installment Due Date is near (5 days), trigger Payment Alert** (Cuando faltan 5 días para el vencimiento de una cuota, disparar alerta de cobro al comprador).
*   **When Lot Debt reaches Zero, trigger Clearance Certificate Generation** (Cuando la deuda total del lote llega a cero, disparar la generación del certificado de no adeudo).

![Event Storming](../assets/cap2/Big_Picture_Event_Storming.jpg)

### 2.3.6. Ubiquitous Language

**Glosario de Términos del Dominio**

*   **Plot / Lot (Lote):** Unidad de terreno delimitada dentro de un proyecto inmobiliario, que representa el activo principal disponible para cotización, separación o compra.
*   **Real Estate Project (Proyecto Inmobiliario):** Conjunto de lotes urbanizados o semi-urbanizados organizados en etapas, que forman el catálogo de ventas expuesto en las plataformas.
*   **Field Sales Agent (Agente Comercial de Campo):** Asesor encargado de la prospección, cotización y venta *in situ* de los lotes, operando principalmente desde la aplicación móvil.
*   **Prospect / Lead (Prospecto):** Cliente potencial interesado en adquirir uno o varios lotes, cuya información de contacto e interacciones son registradas para seguimiento comercial.
*   **Buyer / Investor (Comprador / Inversionista):** Cliente final o entidad jurídica que adquiere lotes y utiliza la plataforma web de autoservicio para gestionar sus contratos y finanzas.
*   **Reservation (Separación):** Acción comercial de bloquear temporalmente la disponibilidad de un lote en el sistema mediante un pago inicial, asegurando la intención de compra del cliente.
*   **Financing Simulation (Simulación de Financiamiento):** Cálculo algorítmico que proyecta el desglose de cuotas mensuales, plazos y tasas de interés para la adquisición a crédito de un lote.
*   **Payment Voucher (Voucher / Comprobante de Pago):** Evidencia física o digital de una transacción bancaria (transferencia o depósito) realizada por el cliente para separar o amortizar un lote.
*   **OCR Extraction (Extracción OCR):** Proceso automatizado mediante visión artificial (Reconocimiento Óptico de Caracteres) que lee y extrae datos críticos (monto, fecha, N° de operación) directamente de la fotografía de un voucher.
*   **Offline Mode (Modo Offline / Sin Conexión):** Capacidad operativa de la aplicación móvil que permite a los agentes continuar registrando prospectos y separaciones en zonas rurales o de expansión urbana sin acceso a internet.
*   **Synchronization (Sincronización):** Proceso bidireccional de transferencia, resolución de conflictos y consolidación de datos entre la base local del dispositivo móvil (SQLite) y el repositorio central en la nube.
*   **Digital Contract (Contrato Digital):** Documento legal de compra-venta generado dinámicamente inyectando las variables del cliente y del lote, disponible para previsualización y firma.
*   **Electronic Signature (Firma Electrónica):** Mecanismo de validación criptográfica con valor legal cualificado que permite a los clientes aceptar y firmar sus contratos de manera 100% digital, eliminando el papel.
*   **Digital Repository (Repositorio Digital):** Espacio centralizado y seguro en la nube (ej. AWS S3) donde se indexan, almacenan y vinculan todos los documentos, contratos y comprobantes de un expediente.
*   **Account Statement (Estado de Cuenta):** Panel financiero consolidado que muestra el histórico de recibos validados, el saldo deudor, las próximas fechas de vencimiento y el porcentaje de amortización de un cliente.
*   **Interactive Map (Mapa Interactivo / Plano Catastral):** Representación visual de polígonos vectoriales georreferenciados que permite a los usuarios ver la ubicación, dimensiones y estado en tiempo real (disponible, separado, vendido) de cada lote.
*   **Financial Reconciliation (Conciliación Financiera):** Proceso administrativo de *back-office* donde el equipo contable audita y valida que la información extraída del voucher coincida con los ingresos reales en las cuentas bancarias de la empresa.
*   **Dashboard (Panel de Control):** Interfaz visual consolidada que permite a los agentes ver sus comisiones, a los compradores ver su patrimonio y a los administradores evaluar el rendimiento general de ventas.

## 2.4. Requirements specification

### 2.4.1. User Stories

Las *User Stories* expresan los requerimientos del producto a nivel funcional, desde la perspectiva del valor que recibe cada actor dentro del ecosistema multiplataforma de comercialización y gestión de lotes inmobiliarios. Los criterios de aceptación siguen estrictamente el formato Gherkin (Dado/Cuando/Entonces) y describen el comportamiento observable del sistema frente a múltiples escenarios, omitiendo detalles específicos de la interfaz de usuario o decisiones de implementación.

El detalle profundo de la arquitectura interna —protocolos, encriptación, estructuras de datos, integraciones de IA (OCR) y pasarelas de pago— se especifica de forma independiente mediante las *Technical Stories* y *Spikes*, dirigidas exclusivamente al equipo de desarrollo.

Para organizar el alcance del sistema, las historias se han clasificado en las siguientes cinco épicas principales:

*   **EP-01 | Gestión Operativa In Situ :** Funcionalidades enfocadas en la labor de campo del Agente Comercial sin conexión, como catálogos, mapas y registro de clientes.
*   **EP-02 | Captura y Digitalización Documental :** Capacidades del motor OCR, manejo de cámara, compresión de imágenes y validación visual de vouchers.
*   **EP-03 | Exploración y Cotización Autónoma :** Módulos para que el Comprador filtre lotes, vea planos y simule financiamientos de forma independiente.
*   **EP-04 | Autoservicio y Control Financiero :** Gestión centralizada de contratos, estados de cuenta, constancias y alertas de pago para clientes.
*   **EP-05 | Technical & Spike Stories :** Requerimientos técnicos del backend, integraciones, seguridad, endpoints y rendimiento dirigidos al equipo de desarrollo.


<!-- US-01 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-01</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-01</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Autenticación segura in situ</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero autenticar mi identidad en la aplicación móvil para acceder al portafolio de lotes asignados de manera segura.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Autenticación exitosa.</i><br><br>
      <b>Dado que</b> el agente comercial posee credenciales válidas,<br>
      <b>Cuando</b> el sistema recibe la solicitud de autenticación con conexión a internet,<br>
      <b>Entonces</b> el sistema valida las credenciales, otorga el token de acceso y permite la entrada al perfil.<br><br>
      <i>Escenario 2: Bloqueo por credenciales inválidas múltiples.</i><br><br>
      <b>Dado que</b> el agente comercial intenta iniciar sesión,<br>
      <b>Cuando</b> ingresa credenciales erróneas por quinta vez consecutiva,<br>
      <b>Entonces</b> el sistema bloquea temporalmente el acceso por 15 minutos y emite un registro de seguridad al backend.
  </td></tr>
</table>

<!-- US-02 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-02</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-01</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Descarga de portafolio para inicio de jornada</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero descargar el catálogo actualizado de lotes al iniciar sesión para asegurar la disponibilidad de la información durante el trabajo en campo sin internet.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Sincronización inicial completa.</i><br><br>
      <b>Dado que</b> el agente inicia sesión exitosamente con conexión a la red,<br>
      <b>Cuando</b> el sistema despliega la vista principal,<br>
      <b>Entonces</b> descarga y almacena en la base de datos local (SQLite) el estado actual del catálogo de lotes.<br><br>
      <i>Escenario 2: Interrupción de descarga por fallo de red.</i><br><br>
      <b>Dado que</b> la descarga del portafolio está en proceso,<br>
      <b>Cuando</b> el dispositivo pierde abruptamente la conexión a internet,<br>
      <b>Entonces</b> el sistema cancela la operación parcial, mantiene la última versión estable conocida y alerta sobre la sincronización incompleta.
  </td></tr>
</table>

<!-- US-03 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-03</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-01</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Detección automática de conectividad</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero que la aplicación detecte la pérdida de red para transicionar automáticamente al modo de trabajo offline sin interrumpir mi flujo.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Transición a modo offline.</i><br><br>
      <b>Dado que</b> el dispositivo móvil pierde el acceso a internet en zona de campo,<br>
      <b>Cuando</b> el listener de red del sistema detecta la ausencia de ping,<br>
      <b>Entonces</b> el sistema enruta todas las escrituras a la base local y expone un indicador visual de "Modo sin conexión".<br><br>
      <i>Escenario 2: Recuperación de estado online.</i><br><br>
      <b>Dado que</b> la aplicación opera en modo offline,<br>
      <b>Cuando</b> el dispositivo recupera acceso a una red estable,<br>
      <b>Entonces</b> el sistema remueve la alerta visual y reactiva las llamadas directas a la RESTful API.
  </td></tr>
</table>

<!-- US-04 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-04</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-01</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Registro de prospectos offline</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero registrar la información de nuevos clientes potenciales sin conexión para no perder oportunidades comerciales en zonas remotas.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Guardado local exitoso.</i><br><br>
      <b>Dado que</b> la aplicación opera en modo offline,<br>
      <b>Cuando</b> el agente registra nombre, documento y teléfono de un prospecto,<br>
      <b>Entonces</b> el sistema guarda el registro en la base de datos local y lo añade a la cola de sincronización.<br><br>
      <i>Escenario 2: Rechazo por campos requeridos ausentes.</i><br><br>
      <b>Dado que</b> el agente intenta registrar un prospecto offline,<br>
      <b>Cuando</b> omite el ingreso del documento de identidad obligatorio,<br>
      <b>Entonces</b> el sistema impide el guardado y exige completar la información faltante.
  </td></tr>
</table>

<!-- US-05 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-05</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-01</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Consulta del plano maestro catastral in situ</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero abrir el plano detallado de la etapa del proyecto para explicar colindancias y áreas verdes al prospecto.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Renderizado vectorial sin red.</i><br><br>
      <b>Dado que</b> el agente selecciona la vista del mapa general,<br>
      <b>Cuando</b> solicita su visualización,<br>
      <b>Entonces</b> el sistema lee los vectores geoespaciales almacenados en caché local y renderiza el polígono sin requerir carga externa.<br><br>
      <i>Escenario 2: Interacción espacial del lote.</i><br><br>
      <b>Dado que</b> el plano está renderizado,<br>
      <b>Cuando</b> el agente selecciona un lote específico en el mapa,<br>
      <b>Entonces</b> el sistema destaca el lote y expone en una superposición su área total y su estado (disponible/vendido).
  </td></tr>
</table>

<!-- US-06 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-06</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-01</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Registro de separación de lote offline con validación</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero registrar una separación de lote de forma local para asegurar la intención de compra del cliente en el terreno.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Separación temporal local.</i><br><br>
      <b>Dado que</b> el agente solicita la separación de un lote en modo offline,<br>
      <b>Cuando</b> procesa la reserva con los datos del prospecto,<br>
      <b>Entonces</b> el sistema marca el lote como "Separación pendiente" en la base local para prevenir dobles ventas desde el mismo dispositivo.<br><br>
      <i>Escenario 2: Lote no disponible en caché local.</i><br><br>
      <b>Dado que</b> el agente intenta separar un lote,<br>
      <b>Cuando</b> el estado del lote en la base local ya figura como "Separado" o "Vendido",<br>
      <b>Entonces</b> el sistema rechaza la transacción y alerta sobre la indisponibilidad del activo.
  </td></tr>
</table>

<!-- US-07 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-07</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-02</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Captura fotográfica del voucher de pago</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero utilizar la cámara para capturar la imagen del voucher físico de separación y adjuntarlo al expediente.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Captura y vinculación.</i><br><br>
      <b>Dado que</b> el sistema activa el flujo de evidencia de pago,<br>
      <b>Cuando</b> el agente captura y confirma la fotografía del documento,<br>
      <b>Entonces</b> el sistema guarda la imagen en el almacenamiento local y la asocia mediante ID foráneo a la separación actual.<br><br>
      <i>Escenario 2: Rechazo por falta de permisos.</i><br><br>
      <b>Dado que</b> el agente inicia el módulo de captura,<br>
      <b>Cuando</b> el dispositivo no tiene otorgados los permisos de hardware para la cámara,<br>
      <b>Entonces</b> el sistema detiene el proceso y emite un diálogo nativo solicitando los permisos requeridos.
  </td></tr>
</table>

<!-- US-08 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-08</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-02</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Compresión de imagen antes de sincronización</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero que la aplicación reduzca el tamaño de las fotografías para consumir menos ancho de banda de mis datos móviles al enviar vouchers.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Compresión exitosa dentro del límite.</i><br><br>
      <b>Dado que</b> existe una imagen original lista para sincronizar,<br>
      <b>Cuando</b> el agente recupera conexión a internet,<br>
      <b>Entonces</b> el sistema procesa el archivo reduciendo su peso por debajo de los 2MB garantizando la legibilidad antes de su transmisión a la nube.<br><br>
      <i>Escenario 2: Protección ante corrupción de imagen.</i><br><br>
      <b>Dado que</b> el sistema intenta comprimir el archivo,<br>
      <b>Cuando</b> el proceso falla y corrompe la salida resultante,<br>
      <b>Entonces</b> el sistema cancela la compresión, preserva la imagen original en el dispositivo y alerta sobre el fallo de preparación.
  </td></tr>
</table>

<!-- US-09 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-09</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-02</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Extracción automatizada de datos mediante OCR</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero que el sistema extraiga el monto, fecha y código de operación del voucher fotográfico para evitar errores de digitación manual.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Extracción limpia de metadatos.</i><br><br>
      <b>Dado que</b> el agente acepta la fotografía capturada,<br>
      <b>Cuando</b> el motor nativo de reconocimiento óptico de caracteres (OCR) procesa la imagen,<br>
      <b>Entonces</b> identifica los patrones numéricos y rellena automáticamente los campos de Monto, Fecha y N° Operación en el formulario.<br><br>
      <i>Escenario 2: Imagen borrosa (Fallo de umbral).</i><br><br>
      <b>Dado que</b> el OCR analiza la fotografía,<br>
      <b>Cuando</b> el contraste del texto es inferior al 40% de legibilidad estructural,<br>
      <b>Entonces</b> el sistema interrumpe el procesamiento, notifica "Imagen ilegible" y exige capturar la foto nuevamente.
  </td></tr>
</table>

<!-- US-10 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-10</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-02</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Corrección manual de datos del voucher (Fallback)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero editar manualmente los datos pre-rellenados por el OCR en caso de que este haya cometido un error en la lectura de un número.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Sobrescritura manual permitida.</i><br><br>
      <b>Dado que</b> el OCR completó la extracción de datos y los expone en pantalla,<br>
      <b>Cuando</b> el agente detecta un dígito erróneo y lo modifica con el teclado del dispositivo,<br>
      <b>Entonces</b> el sistema acepta el cambio y prioriza la entrada humana para su guardado definitivo.<br><br>
      <i>Escenario 2: Auditoría de alteración manual.</i><br><br>
      <b>Dado que</b> el agente realiza una modificación manual sobre un campo pre-rellenado por OCR,<br>
      <b>Cuando</b> el sistema guarda la transacción,<br>
      <b>Entonces</b> adjunta un indicador lógico (flag = true) en el payload advirtiendo al back-office que los datos fueron alterados post-OCR.
  </td></tr>
</table>

<!-- US-11 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-11</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-01</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Sincronización automática de registros pendientes</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero que los registros locales se envíen al servidor automáticamente al recuperar conexión para asegurar la venta sin intervención manual.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Ejecución en segundo plano exitosa.</i><br><br>
      <b>Dado que</b> el dispositivo recupera acceso a internet y existen datos locales pendientes,<br>
      <b>Cuando</b> el proceso de sincronización inicia automáticamente,<br>
      <b>Entonces</b> el sistema transfiere las transacciones al repositorio central y marca los registros locales como "Sincronizados".<br><br>
      <i>Escenario 2: Pausa por red inestable (Timeout).</i><br><br>
      <b>Dado que</b> la sincronización de un lote está en curso,<br>
      <b>Cuando</b> la latencia de red supera los 15 segundos (timeout),<br>
      <b>Entonces</b> el sistema pausa la transmisión, mantiene el registro como pendiente y programa un reintento automático.
  </td></tr>
</table>

<!-- US-12 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-12</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-01</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Manejo de conflictos de concurrencia de lotes</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero ser notificado si un lote separado offline ya fue vendido por otro agente para reubicar al prospecto rápidamente.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Conflicto detectado en nube.</i><br><br>
      <b>Dado que</b> el sistema intenta sincronizar una separación offline,<br>
      <b>Cuando</b> el servidor central detecta que el lote ya figura como "Vendido" por otro usuario,<br>
      <b>Entonces</b> el sistema rechaza la sincronización, revierte el estado local y genera una alerta de conflicto al agente.<br><br>
      <i>Escenario 2: Reasignación posterior a conflicto.</i><br><br>
      <b>Dado que</b> un agente recibe una alerta de conflicto de disponibilidad,<br>
      <b>Cuando</b> visualiza el registro rechazado,<br>
      <b>Entonces</b> el sistema retiene los datos del prospecto y permite asignarle un nuevo lote disponible sin necesidad de digitar nuevamente.
  </td></tr>
</table>

<!-- US-13 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-13</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Agente Comercial de Campo</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-01</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Visualización de borrador de contrato in situ</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Agente Comercial de Campo, quiero proyectar el contrato preliminar para que el cliente valide las cláusulas y montos antes de la firma oficial.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Renderizado local exitoso.</i><br><br>
      <b>Dado que</b> se completó el registro financiero y de contacto de forma local,<br>
      <b>Cuando</b> el agente solicita la previsualización del documento,<br>
      <b>Entonces</b> el sistema renderiza la plantilla PDF inyectando las variables almacenadas en el dispositivo móvil.<br><br>
      <i>Escenario 2: Bloqueo por falta de datos.</i><br><br>
      <b>Dado que</b> el agente solicita previsualizar el contrato preliminar,<br>
      <b>Cuando</b> existen variables críticas vacías (ej. Estado civil del prospecto),<br>
      <b>Entonces</b> el sistema detiene el renderizado e indica el campo específico que debe completarse.
  </td></tr>
</table>

<!-- US-14 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-14</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-03</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Registro de cuenta de usuario web</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero crear una cuenta en la plataforma web para explorar proyectos, simular precios y gestionar mis adquisiciones inmobiliarias.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Creación de cuenta y validación.</i><br><br>
      <b>Dado que</b> el usuario proporciona información válida y un correo de contacto,<br>
      <b>Cuando</b> envía el formulario de registro web,<br>
      <b>Entonces</b> el sistema crea el perfil con estado "Inactivo" y envía un enlace de verificación de token único al correo indicado.<br><br>
      <i>Escenario 2: Correo electrónico ya registrado.</i><br><br>
      <b>Dado que</b> el usuario intenta registrarse,<br>
      <b>Cuando</b> ingresa un correo electrónico que ya existe en la base de datos,<br>
      <b>Entonces</b> el sistema rechaza el registro y sugiere derivar al flujo de recuperación de contraseña.
  </td></tr>
</table>

<!-- US-15 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-15</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-03</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Exploración del catálogo de proyectos inmobiliarios</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero visualizar la lista de proyectos disponibles para evaluar opciones de compra según ubicación geográfica y precios base.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Visualización general activa.</i><br><br>
      <b>Dado que</b> el usuario autenticado accede al portal web,<br>
      <b>Cuando</b> el sistema recupera la base de datos comercial,<br>
      <b>Entonces</b> expone los proyectos activos con miniaturas representativas, rango de precios y porcentaje de disponibilidad.<br><br>
      <i>Escenario 2: Indicador de proyectos sin stock.</i><br><br>
      <b>Dado que</b> el usuario revisa el portafolio global,<br>
      <b>Cuando</b> un proyecto específico alcanza el 100% de lotes vendidos,<br>
      <b>Entonces</b> el sistema lo mantiene visible en el catálogo pero le superpone una etiqueta inactiva de "Vendido Totalmente" (Sold Out).
  </td></tr>
</table>

<!-- US-16 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-16</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-03</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Filtrado interactivo de lotes en mapa</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero filtrar lotes específicos dentro de un proyecto por dimensiones, precio o ubicación para agilizar mi toma de decisiones.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Aplicación de filtros geométricos.</i><br><br>
      <b>Dado que</b> el sistema expone el mapa catastral del proyecto,<br>
      <b>Cuando</b> el usuario aplica un rango de metraje (ej. 120m2 a 150m2),<br>
      <b>Entonces</b> el sistema recalcula los polígonos y aísla visualmente únicamente los lotes que cumplen el parámetro.<br><br>
      <i>Escenario 2: Búsqueda sin resultados coincidentes.</i><br><br>
      <b>Dado que</b> el usuario manipula los controles de filtrado,<br>
      <b>Cuando</b> los parámetros ingresados no coinciden con ningún activo disponible,<br>
      <b>Entonces</b> el mapa muestra todos los lotes bloqueados (gris) y se despliega un mensaje indicando la ausencia de stock.
  </td></tr>
</table>

<!-- US-17 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-17</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-03</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Simulación de financiamiento autónoma</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero simular cronogramas de pago en la web para analizar la viabilidad financiera de mi inversión sin necesidad de contactar a un agente.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Cálculo con tasa estándar.</i><br><br>
      <b>Dado que</b> el usuario selecciona un lote disponible,<br>
      <b>Cuando</b> ingresa el monto de cuota inicial y selecciona el plazo de meses,<br>
      <b>Entonces</b> el algoritmo del sistema calcula y genera un desglose proyectado de cuotas mensuales y tasas de interés aplicadas.<br><br>
      <i>Escenario 2: Validación de inicial mínima requerida.</i><br><br>
      <b>Dado que</b> el usuario intenta simular un financiamiento,<br>
      <b>Cuando</b> el monto de la cuota inicial ingresada es inferior al porcentaje mínimo estipulado por las reglas de negocio (ej. 20%),<br>
      <b>Entonces</b> el sistema rechaza el cálculo y requiere ajustar el monto ingresado al umbral mínimo.
  </td></tr>
</table>

<!-- US-18 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-18</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-03</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Descarga de cotización de financiamiento PDF</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero descargar la simulación de financiamiento en formato PDF para mantener un registro documental de la evaluación.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Generación y exportación a PDF.</i><br><br>
      <b>Dado que</b> el sistema muestra el cronograma financiero en pantalla,<br>
      <b>Cuando</b> el usuario solicita la exportación documental,<br>
      <b>Entonces</b> el sistema compila y descarga un archivo PDF estructurado con la vigencia de la oferta, datos del lote y tabla de cuotas.<br><br>
      <i>Escenario 2: Prevención de manipulación de datos.</i><br><br>
      <b>Dado que</b> el sistema genera el archivo de exportación,<br>
      <b>Cuando</b> se compila el PDF,<br>
      <b>Entonces</b> el archivo generado se bloquea con permisos de solo lectura para evitar alteraciones por software externo.
  </td></tr>
</table>

<!-- US-19 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-19</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-03</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Solicitud formal de separación de lote desde web</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero solicitar la separación de un lote directamente desde la web para asegurar su adquisición rápidamente y retirarlo del mercado.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Bloqueo de lote exitoso.</i><br><br>
      <b>Dado que</b> el lote está disponible y la simulación fue aprobada por el usuario,<br>
      <b>Cuando</b> envía la intención formal de reserva,<br>
      <b>Entonces</b> el sistema bloquea temporalmente el lote (1 hora), genera un identificador de transacción y habilita la pasarela de pago o carga de voucher.<br><br>
      <i>Escenario 2: Lote tomado por concurrencia.</i><br><br>
      <b>Dado que</b> el usuario intenta iniciar la separación de un lote,<br>
      <b>Cuando</b> el servidor verifica y constata que el lote fue bloqueado milisegundos antes por otro actor,<br>
      <b>Entonces</b> el sistema rechaza la solicitud, revierte el proceso y notifica al usuario que debe seleccionar un nuevo lote.
  </td></tr>
</table>

<!-- US-20 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-20</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-04</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Carga manual de comprobante de pago web</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero adjuntar el comprobante de transferencia bancaria en la web para validar mi proceso de separación si decido no usar la pasarela online.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Recepción de evidencia exitosa.</i><br><br>
      <b>Dado que</b> existe una reserva pendiente dentro del marco de tiempo permitido,<br>
      <b>Cuando</b> el usuario sube un archivo válido (JPEG o PDF),<br>
      <b>Entonces</b> el sistema lo almacena, cambia el estado del lote a "Esperando verificación financiera" y notifica al área administrativa.<br><br>
      <i>Escenario 2: Rechazo por archivo inválido.</i><br><br>
      <b>Dado que</b> el usuario intenta adjuntar el comprobante de pago,<br>
      <b>Cuando</b> el archivo supera el límite de 5MB o no cumple con las extensiones permitidas,<br>
      <b>Entonces</b> el sistema interrumpe la subida y arroja una alerta de formato no admitido.
  </td></tr>
</table>

<!-- US-21 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-21</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-04</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Visualización centralizada de contratos</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero visualizar mi contrato de compra-venta y sus anexos de forma digital para verificar las cláusulas legales antes de la firma.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Disponibilidad de documentos aprobados.</i><br><br>
      <b>Dado que</b> el equipo de back-office emite el contrato preliminar,<br>
      <b>Cuando</b> el usuario ingresa al módulo documental de su perfil web,<br>
      <b>Entonces</b> el sistema expone el archivo PDF para lectura directa y descarga segura.<br><br>
      <i>Escenario 2: Contrato aún no emitido.</i><br><br>
      <b>Dado que</b> la separación del lote fue pagada pero no ha sido auditada,<br>
      <b>Cuando</b> el usuario ingresa al módulo documental,<br>
      <b>Entonces</b> el sistema muestra un indicador visual de estado "Contrato en elaboración" e inhabilita el área de descarga.
  </td></tr>
</table>

<!-- US-22 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-22</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-04</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Conformidad digital de términos contractuales</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero registrar mi conformidad preliminar con los términos del contrato en el portal web para agilizar el proceso administrativo de firmas.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Sello de tiempo de aceptación.</i><br><br>
      <b>Dado que</b> el sistema presenta el contrato legal digitalizado,<br>
      <b>Cuando</b> el usuario confirma la lectura mediante la acción designada (checkbox),<br>
      <b>Entonces</b> el sistema registra el timestamp de aceptación y notifica al área legal que el cliente está listo para la firma final.<br><br>
      <i>Escenario 2: Restricción de lectura previa.</i><br><br>
      <b>Dado que</b> el usuario ingresa a la vista del contrato,<br>
      <b>Cuando</b> intenta marcar la casilla de conformidad sin haber hecho scroll hasta el final del documento,<br>
      <b>Entonces</b> el sistema mantiene deshabilitado el control de aceptación obligando la navegación completa del documento.
  </td></tr>
</table>

<!-- US-23 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-23</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-04</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Visualización del estado de cuenta consolidado</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero visualizar un resumen de mi estado de cuenta para monitorear el saldo pendiente y el avance de pagos de mi lote.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Cálculos de amortización al día.</i><br><br>
      <b>Dado que</b> el usuario accede al módulo financiero,<br>
      <b>Cuando</b> el sistema recupera la información transaccional,<br>
      <b>Entonces</b> despliega dinámicamente el monto total pagado, la deuda restante y un gráfico circular con el porcentaje de avance de pago.<br><br>
      <i>Escenario 2: Lote cancelado al 100%.</i><br><br>
      <b>Dado que</b> el usuario ha finalizado de pagar todas sus cuotas,<br>
      <b>Cuando</b> revisa su estado de cuenta,<br>
      <b>Entonces</b> el sistema expone un indicador de saldo "0.00", llena el gráfico al 100% y cambia el estado del lote a "Cancelado".
  </td></tr>
</table>

<!-- US-24 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-24</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-04</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Notificaciones de vencimiento de cuotas</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero recibir alertas automatizadas sobre mis próximas fechas de pago para evitar recargos por mora y mantener un historial financiero sano.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Alerta preventiva de vencimiento.</i><br><br>
      <b>Dado que</b> el cronograma proyecta un vencimiento en los próximos 5 días,<br>
      <b>Cuando</b> el proceso programado diario (cron job) se ejecuta,<br>
      <b>Entonces</b> el sistema emite una alerta destacada en el dashboard web y despacha un recordatorio vía correo electrónico.<br><br>
      <i>Escenario 2: Vencimiento expirado con mora.</i><br><br>
      <b>Dado que</b> la fecha de vencimiento superó el día actual sin registrarse el pago,<br>
      <b>Cuando</b> se actualiza el estado de cuenta,<br>
      <b>Entonces</b> el sistema clasifica la cuota como "Vencida" y expone visualmente el recargo o penalidad acumulada según la tasa configurada.
  </td></tr>
</table>

<!-- US-25 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-25</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-04</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Historial de recibos financieros validados</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero acceder al repositorio histórico de vouchers que han sido verificados por administración como comprobante legal de mis aportes.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Acceso a repositorio de evidencias.</i><br><br>
      <b>Dado que</b> el equipo de back-office concilia un pago exitosamente,<br>
      <b>Cuando</b> el usuario navega a la sección de "Mis Pagos",<br>
      <b>Entonces</b> el sistema expone los comprobantes digitalizados con estado "Aprobado" y habilita su descarga en PDF/Imagen.<br><br>
      <i>Escenario 2: Comprobante rechazado u observado.</i><br><br>
      <b>Dado que</b> el equipo de back-office rechaza un comprobante (ej. ilegible o cuenta incorrecta),<br>
      <b>Cuando</b> el usuario ingresa al repositorio,<br>
      <b>Entonces</b> el sistema marca la evidencia como "Rechazada", expone el motivo administrativo y habilita un botón para cargar un nuevo voucher sustituto.
  </td></tr>
</table>

<!-- US-26 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-26</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-04</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Generación del certificado de no adeudo</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero generar y descargar un documento de "No Adeudo" automático al finalizar mis cuotas para iniciar los trámites de escrituración notarial.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Emisión por cancelación total.</i><br><br>
      <b>Dado que</b> el algoritmo valida que la deuda total de capital e intereses vinculada al lote es cero,<br>
      <b>Cuando</b> el usuario solicita la constancia de cancelación,<br>
      <b>Entonces</b> el sistema compila el PDF dinámicamente y otorga acceso al certificado con la firma digital representativa.<br><br>
      <i>Escenario 2: Restricción por deuda residual.</i><br><br>
      <b>Dado que</b> el usuario solicita la emisión del certificado de no adeudo,<br>
      <b>Cuando</b> el sistema detecta que existe un saldo deudor (así sea mínimo, por comisiones o moras),<br>
      <b>Entonces</b> bloquea la generación del documento e indica al cliente el monto exacto faltante a cancelar.
  </td></tr>
</table>

<!-- US-27 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-27</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-04</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Consolidación de múltiples activos (Dashboard)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero que el sistema consolide todos mis lotes adquiridos en una sola vista panorámica para facilitar la gestión global de mi patrimonio.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Agrupación de portafolio patrimonial.</i><br><br>
      <b>Dado que</b> el usuario posee múltiples contratos activos bajo la misma identificación (DNI/RUC),<br>
      <b>Cuando</b> el sistema renderiza el panel de inicio,<br>
      <b>Entonces</b> agrupa la información financiera totalizando la inversión acumulada y la deuda global de todas las propiedades.<br><br>
      <i>Escenario 2: Desglose individual de activos.</i><br><br>
      <b>Dado que</b> el dashboard exhibe el consolidado patrimonial,<br>
      <b>Cuando</b> el usuario selecciona un lote específico del listado inferior,<br>
      <b>Entonces</b> el sistema aplica un filtro sobre la vista principal y refresca las métricas para mostrar únicamente el comportamiento de ese lote.
  </td></tr>
</table>

<!-- US-28 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-28</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Comprador e Inversionista</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Baja</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-04</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Designación de co-propietario o cónyuge</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Comprador e Inversionista, quiero añadir los datos de un co-titular en la plataforma web para que los contratos emitidos incluyan ambos sujetos jurídicos en la transacción.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Inclusión de co-titular.</i><br><br>
      <b>Dado que</b> el usuario gestiona su perfil antes de emitirse un contrato,<br>
      <b>Cuando</b> ingresa y asocia un documento de identidad válido de un tercero,<br>
      <b>Entonces</b> el sistema adjunta los datos del co-propietario como variable activa para la compilación legal.<br><br>
      <i>Escenario 2: Restricción de modificación post-firma.</i><br><br>
      <b>Dado que</b> el contrato ya fue generado y se encuentra en estado "En curso",<br>
      <b>Cuando</b> el usuario intenta añadir o modificar un co-titular,<br>
      <b>Entonces</b> el sistema bloquea la acción y emite una alerta indicando que debe procesarse mediante una adenda legal a través de servicio al cliente.
  </td></tr>
</table>

<!-- US-29 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-29</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Spike: Estrategia de encriptación de base de datos local SQLite</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero investigar estrategias de cifrado (ej. SQLCipher) para asegurar que los datos financieros en los móviles offline estén protegidos ante robos o manipulación.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Benchmark de seguridad vs rendimiento.</i><br><br>
      <b>Dado que</b> el sistema almacena información crítica (datos de prospectos y transacciones),<br>
      <b>Cuando</b> el desarrollador analiza los mecanismos de cifrado AES-256 integrables,<br>
      <b>Entonces</b> establece un entorno de prueba y verifica que la encriptación no degrade el rendimiento de consulta en más de un 15% frente a bases sin cifrar.<br><br>
      <i>Escenario 2: Manejo seguro de llaves maestras.</i><br><br>
      <b>Dado que</b> se requiere desencriptar la base al abrir la App,<br>
      <b>Cuando</b> el desarrollador define la arquitectura criptográfica,<br>
      <b>Entonces</b> provee un esquema documentado sobre cómo almacenar el passkey en el KeyStore (Android) o Keychain (iOS) evitando que quede expuesto en el código fuente.
  </td></tr>
</table>

<!-- US-30 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-30</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Spike: Evaluación de proveedores de firma electrónica cualificada</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero investigar APIs de soluciones de firma electrónica con valor legal para integrarlas en el flujo web y erradicar el papeleo en los contratos inmobiliarios.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Informe técnico y viabilidad comercial.</i><br><br>
      <b>Dado que</b> el proyecto busca un entorno 100% libre de papel con validez legal peruana,<br>
      <b>Cuando</b> el desarrollador compara a los proveedores del mercado (ej. Firmas Perú, DocuSign, TuFirma),<br>
      <b>Entonces</b> entrega una matriz técnica comparativa con costos transaccionales, facilidad de integración vía API y recomendación arquitectónica de uso.<br><br>
      <i>Escenario 2: Diseño de Webhook para callbacks.</i><br><br>
      <b>Dado que</b> el proveedor de firmas enviará notificaciones asíncronas sobre el estado del documento,<br>
      <b>Cuando</b> el desarrollador prototipa la arquitectura,<br>
      <b>Entonces</b> diseña el esquema del endpoint de tipo Webhook en el backend capaz de recibir e interpretar los callbacks de "Firmado exitosamente" emitidos por el proveedor externo.
  </td></tr>
</table>

<!-- US-31 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-31</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Implementación de seguridad JWT en la API RESTful</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero implementar la validación de JSON Web Tokens (JWT) en los endpoints protegidos para garantizar que solo usuarios autenticados accedan a la información del sistema.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Rechazo de token inválido o expirado.</i><br><br>
      <b>Dado que</b> el desarrollador recibe una petición HTTP a un endpoint comercial,<br>
      <b>Cuando</b> el token en la cabecera "Authorization" es inválido o ha superado su fecha de expiración,<br>
      <b>Entonces</b> el sistema rechaza la solicitud devolviendo un código HTTP 401 Unauthorized sin procesar la lógica de negocio.<br><br>
      <i>Escenario 2: Extracción exitosa de contexto.</i><br><br>
      <b>Dado que</b> una petición ingresa con un token firmado correctamente,<br>
      <b>Cuando</b> el middleware de seguridad valida la firma criptográfica,<br>
      <b>Entonces</b> el sistema extrae los identificadores del usuario (claims) y los inyecta en el flujo de la petición para las consultas a la base de datos.
  </td></tr>
</table>

<!-- US-32 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-32</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Desarrollo de API Endpoint para sincronización masiva (Bulk Upload)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero construir un endpoint capaz de recibir múltiples transacciones en un solo payload para que la aplicación móvil sincronice todos sus datos pendientes de un solo golpe.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Inserción de lote exitosa.</i><br><br>
      <b>Dado que</b> el endpoint recibe un arreglo JSON con 10 prospectos y 5 separaciones,<br>
      <b>Cuando</b> el backend procesa las transacciones y todas son válidas estructuralmente,<br>
      <b>Entonces</b> el sistema las guarda mediante una transacción de base de datos e informa HTTP 201 Created.<br><br>
      <i>Escenario 2: Integridad transaccional ante error (Rollback).</i><br><br>
      <b>Dado que</b> se procesa un arreglo de transacciones múltiples,<br>
      <b>Cuando</b> el elemento número 5 genera un error de llave foránea (ej. lote inexistente),<br>
      <b>Entonces</b> el sistema aborta toda la operación (Rollback), no guarda ningún elemento y retorna un HTTP 400 Bad Request detallando el índice problemático.
  </td></tr>
</table>

<!-- US-33 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-33</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Integración de almacenamiento cloud para vouchers (AWS S3)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero integrar el backend con un servicio de almacenamiento externo (S3) para descargar al servidor principal del peso de miles de fotos de comprobantes y PDFs.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Generación de URLs pre-firmadas.</i><br><br>
      <b>Dado que</b> un usuario o agente requiere subir un comprobante al sistema,<br>
      <b>Cuando</b> solicita la carga a través del endpoint de almacenamiento,<br>
      <b>Entonces</b> el sistema retorna una URL pre-firmada con un token temporal válido por 10 minutos para subir el archivo directamente al bucket externo.<br><br>
      <i>Escenario 2: Restricción de tamaño desde el origen.</i><br><br>
      <b>Dado que</b> se establece la conexión con el bucket,<br>
      <b>Cuando</b> un cliente intenta inyectar un archivo de 20MB a la URL pre-firmada,<br>
      <b>Entonces</b> el servicio cloud rechaza la carga basándose en la política estricta de tamaño máximo definida (ej. 5MB) en la firma.
  </td></tr>
</table>

<!-- US-34 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-34</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Endpoint de monitoreo y Health Check</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero crear una ruta de validación rápida `/health` para que los balanceadores de carga monitoreen si la API y sus conexiones a bases de datos están operativas.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Reporte de salud óptimo.</i><br><br>
      <b>Dado que</b> se realiza una petición GET a la ruta de salud,<br>
      <b>Cuando</b> el servidor responde y la base de datos devuelve un ping exitoso,<br>
      <b>Entonces</b> el sistema retorna un HTTP 200 OK estructurado en JSON con el estado de los servicios internos marcados como "UP".<br><br>
      <i>Escenario 2: Degradación de base de datos.</i><br><br>
      <b>Dado que</b> se consulta la ruta de salud,<br>
      <b>Cuando</b> el servidor principal no puede alcanzar el puerto de la base de datos (timeout),<br>
      <b>Entonces</b> el sistema retorna HTTP 503 Service Unavailable y expone un mensaje JSON indicando la desconexión del cluster principal.
  </td></tr>
</table>

<!-- US-35 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-35</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Automatización de backups de base de datos</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero programar volcados de la base de datos PostgreSQL diariamente para prevenir pérdidas masivas de información contractual o financiera ante fallos de hardware.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Volcado automático diario.</i><br><br>
      <b>Dado que</b> el reloj del servidor alcanza el horario de bajo tráfico (ej. 02:00 UTC),<br>
      <b>Cuando</b> el cronograma dispara la tarea (cron job),<br>
      <b>Entonces</b> el sistema ejecuta un volcado completo, lo comprime (GZIP) y lo envía automáticamente a una bóveda de almacenamiento externa.<br><br>
      <i>Escenario 2: Política de retención (Limpieza).</i><br><br>
      <b>Dado que</b> el sistema termina de subir un nuevo respaldo diario,<br>
      <b>Cuando</b> detecta copias que superan el límite máximo de retención configurado (ej. 7 días de antigüedad),<br>
      <b>Entonces</b> el script procede a borrar permanentemente el archivo más antiguo para evitar sobrecostos en almacenamiento.
  </td></tr>
</table>

<!-- US-36 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-36</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Implementación de Rate Limiting en API</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero limitar la cantidad de peticiones concurrentes por dirección IP para evitar ataques de denegación de servicio (DDoS) que tiren abajo la plataforma.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Bloqueo de tráfico malicioso.</i><br><br>
      <b>Dado que</b> una dirección IP emite más peticiones que el límite permitido en un minuto,<br>
      <b>Cuando</b> el middleware detecta el abuso,<br>
      <b>Entonces</b> devuelve un código HTTP 429 Too Many Requests para todas las consultas subsecuentes y congela la IP temporalmente.<br><br>
      <i>Escenario 2: Límite dinámico según criticidad.</i><br><br>
      <b>Dado que</b> existen rutas de distinto peso computacional,<br>
      <b>Cuando</b> se consulta una ruta de descarga de PDF frente a una consulta de listado,<br>
      <b>Entonces</b> el sistema aplica un límite más estricto a la ruta de PDF (ej. 10/min) que a la del catálogo (ej. 150/min).
  </td></tr>
</table>

<!-- US-37 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-37</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Spike: Arquitectura de colas de mensajes (RabbitMQ)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero investigar la implementación de una cola de mensajes asíncrona para que la generación de contratos PDF no congele los servidores principales bajo estrés.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Documentación de tolerancia a fallos.</i><br><br>
      <b>Dado que</b> 50 clientes solicitan su contrato al mismo tiempo,<br>
      <b>Cuando</b> el desarrollador propone el uso de colas (message broker),<br>
      <b>Entonces</b> entrega un esquema técnico demostrando que las solicitudes se encolan y se procesan por hilos independientes devolviendo un 202 Accepted inmediato.<br><br>
      <i>Escenario 2: Manejo de errores en cola (Dead Letter Queue).</i><br><br>
      <b>Dado que</b> una solicitud encolada falla varias veces durante su ejecución,<br>
      <b>Cuando</b> el desarrollador documenta el modelo,<br>
      <b>Entonces</b> incluye el envío de ese mensaje erróneo a una "Dead Letter Queue" para evitar que bloquee todo el proceso y pueda ser auditado manualmente.
  </td></tr>
</table>

<!-- US-38 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-38</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Configuración de CORS y cabeceras de seguridad</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero configurar las políticas de Cross-Origin Resource Sharing (CORS) para evitar que orígenes web externos intenten consumir o modificar la información de nuestra API.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Petición desde dominio autorizado.</i><br><br>
      <b>Dado que</b> el backend recibe una petición HTTP OPTIONS (Preflight),<br>
      <b>Cuando</b> la cabecera Origin coincide con los dominios oficiales de la empresa inmobiliaria,<br>
      <b>Entonces</b> el servidor responde con HTTP 200 y habilita los métodos GET, POST, PUT, DELETE.<br><br>
      <i>Escenario 2: Rechazo de orígenes no registrados.</i><br><br>
      <b>Dado que</b> una plataforma externa (ej. script malicioso local) intenta acceder a los endpoints,<br>
      <b>Cuando</b> el servidor evalúa la cabecera Origin que no figura en la lista de permitidos,<br>
      <b>Entonces</b> deniega el acceso y el navegador del cliente lanza un error de política CORS.
  </td></tr>
</table>

<!-- US-39 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-39</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Endpoint optimizado de polígonos GeoJSON</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero diseñar un endpoint de mapas geográficos que utilice compresión para enviar las coordenadas de los lotes sin colapsar el ancho de banda del celular de los agentes.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Compresión GZIP activa.</i><br><br>
      <b>Dado que</b> un dispositivo solicita la carga del mapa maestro (miles de coordenadas),<br>
      <b>Cuando</b> el payload supera los 10KB de texto crudo,<br>
      <b>Entonces</b> el servidor aplica automáticamente compresión GZIP reduciendo el tamaño del cuerpo de la respuesta en al menos un 60% antes del envío de red.<br><br>
      <i>Escenario 2: Caché distribuido (ETag).</i><br><br>
      <b>Dado que</b> un agente solicita el mapa por segunda vez,<br>
      <b>Cuando</b> envía el identificador de caché (ETag) y el mapa no ha cambiado en base de datos,<br>
      <b>Entonces</b> el servidor responde con un HTTP 304 Not Modified, evitando enviar el cuerpo del mensaje para ahorrar recursos de datos.
  </td></tr>
</table>

<!-- US-40 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-40</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Implementación de Logs Centralizados para Auditoría</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero crear un middleware que intercepte y guarde las peticiones críticas del sistema (pagos, contratos) para que administración tenga evidencia inmutable en auditorías.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Registro inmutable de transacciones.</i><br><br>
      <b>Dado que</b> un usuario ejecuta una solicitud POST/PUT en el módulo financiero o de separación,<br>
      <b>Cuando</b> el servidor procesa la respuesta,<br>
      <b>Entonces</b> graba de forma asíncrona un archivo de log indexado con el método, IP, usuario, fecha y respuesta entregada.<br><br>
      <i>Escenario 2: Ofuscamiento de datos sensibles.</i><br><br>
      <b>Dado que</b> el sistema intercepta las peticiones para su guardado en texto plano,<br>
      <b>Cuando</b> encuentra propiedades en el JSON como contraseñas, tokens o números de tarjetas,<br>
      <b>Entonces</b> ofusca su contenido (ej. reemplazando por `****`) antes de guardar el registro en el historial.
  </td></tr>
</table>

<!-- US-41 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-41</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Implementación de caché distribuido (Redis) para catálogo</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero implementar Redis para cachear el catálogo maestro de lotes y reducir el consumo de recursos de la base de datos principal ante tráfico intenso.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Cache Hit exitoso.</i><br><br>
      <b>Dado que</b> un usuario consulta el catálogo web,<br>
      <b>Cuando</b> los datos ya existen en la memoria de Redis,<br>
      <b>Entonces</b> el sistema retorna la respuesta directamente desde el caché (tiempo < 50ms) sin ejecutar la query SQL.<br><br>
      <i>Escenario 2: Invalidadación de caché por actualización (Cache Invalidation).</i><br><br>
      <b>Dado que</b> un lote es separado o vendido,<br>
      <b>Cuando</b> la transacción se confirma en la base de datos principal,<br>
      <b>Entonces</b> el sistema purga automáticamente la clave correspondiente en Redis para forzar una lectura fresca en la siguiente consulta.
  </td></tr>
</table>

<!-- US-42 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-42</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Sincronización de estados en tiempo real (WebSockets)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero implementar conexiones WebSockets para notificar instantáneamente a los usuarios web cuando un lote cambia su estado de disponibilidad.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Emisión (Broadcast) de evento.</i><br><br>
      <b>Dado que</b> un usuario está observando el mapa de lotes activo,<br>
      <b>Cuando</b> otro comprador concreta una separación en el backend,<br>
      <b>Entonces</b> el servidor emite un evento WebSocket y el frontend del primer usuario actualiza el lote a "Separado" sin recargar la página.<br><br>
      <i>Escenario 2: Manejo de desconexiones (Heartbeat).</i><br><br>
      <b>Dado que</b> la conexión del cliente es intermitente,<br>
      <b>Cuando</b> el servidor deja de recibir el "ping" del cliente por 30 segundos,<br>
      <b>Entonces</b> cierra el socket de manera segura y libera el hilo de conexión en el servidor.
  </td></tr>
</table>

<!-- US-43 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-43</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Control de versiones del esquema de base de datos</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero integrar herramientas de migración (ej. Flyway o Liquibase) para mantener la consistencia en la estructura de la base de datos entre los entornos de desarrollo, pruebas y producción.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Ejecución de nueva migración.</i><br><br>
      <b>Dado que</b> se despliega una nueva versión de la API que incluye una nueva tabla,<br>
      <b>Cuando</b> la aplicación arranca en producción,<br>
      <b>Entonces</b> el sistema ejecuta automáticamente el script SQL de migración e inserta el registro en la tabla de control de versiones.<br><br>
      <i>Escenario 2: Protección contra migraciones alteradas.</i><br><br>
      <b>Dado que</b> un script histórico fue modificado accidentalmente,<br>
      <b>Cuando</b> la herramienta calcula el Checksum y no coincide con el almacenado,<br>
      <b>Entonces</b> el sistema detiene el arranque del servidor para evitar la corrupción del esquema.
  </td></tr>
</table>

<!-- US-44 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-44</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Gestión centralizada de secretos y variables de entorno</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero implementar un gestor seguro para no exponer las credenciales de base de datos ni tokens de pasarelas de pago en el código fuente del repositorio.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Inyección dinámica en Runtime.</i><br><br>
      <b>Dado que</b> el contenedor del servidor inicializa sus procesos,<br>
      <b>Cuando</b> requiere conectar con servicios externos (AWS, Niubiz),<br>
      <b>Entonces</b> extrae las llaves directamente del sistema de variables de entorno del host, sin referenciar archivos estáticos.<br><br>
      <i>Escenario 2: Protección contra fugas en Logs.</i><br><br>
      <b>Dado que</b> el sistema emite errores a la consola,<br>
      <b>Cuando</b> falla la conexión a la base de datos,<br>
      <b>Entonces</b> el logger ofusca automáticamente las contraseñas inyectadas impidiendo que queden impresas en los registros.
  </td></tr>
</table>

<!-- US-45 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-45</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Microservicio de generación de documentos PDF</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero crear un servicio aislado de renderizado HTML a PDF para evitar que este procesamiento pesado afecte los tiempos de respuesta de la API principal.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Generación y almacenamiento asíncrono.</i><br><br>
      <b>Dado que</b> el backend recibe una petición para emitir un contrato de 10 páginas,<br>
      <b>Cuando</b> delega el payload JSON al microservicio de PDF,<br>
      <b>Entonces</b> el servicio principal responde rápido con un estado "En proceso" y el microservicio sube el PDF a S3 al terminar.<br><br>
      <i>Escenario 2: Timeout por plantilla corrupta.</i><br><br>
      <b>Dado que</b> el microservicio intenta renderizar la plantilla,<br>
      <b>Cuando</b> el proceso supera el límite de 30 segundos (loop infinito),<br>
      <b>Entonces</b> aborta la operación y envía una notificación de fallo crítico.
  </td></tr>
</table>

<!-- US-46 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-46</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Paginación optimizada de registros financieros</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero implementar paginación basada en cursor u offset en el listado de comprobantes para optimizar el consumo de memoria en la API y los clientes móviles.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Limitación por página.</i><br><br>
      <b>Dado que</b> un usuario posee un historial de 300 recibos,<br>
      <b>Cuando</b> solicita el endpoint GET con los parámetros `?limit=20&page=1`,<br>
      <b>Entonces</b> la base de datos transfiere exactamente 20 registros junto con el conteo total (Total-Count) en las cabeceras.<br><br>
      <i>Escenario 2: Protección de tamaño máximo.</i><br><br>
      <b>Dado que</b> el cliente solicita información,<br>
      <b>Cuando</b> inyecta el parámetro `?limit=5000` intentando causar un desbordamiento de memoria,<br>
      <b>Entonces</b> el servidor trunca el parámetro y devuelve únicamente el límite máximo seguro configurado (ej. 100 registros).
  </td></tr>
</table>

<!-- US-47 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-47</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Spike: Precisión de librerías nativas OCR (Vision API)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero investigar y prototipar herramientas como Google ML Kit Vision para evaluar si la extracción offline de vouchers cumple con la precisión financiera requerida.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Prototipo y Benchmark funcional.</i><br><br>
      <b>Dado que</b> el equipo requiere extraer montos sin conexión a internet,<br>
      <b>Cuando</b> el desarrollador evalúa las librerías nativas,<br>
      <b>Entonces</b> entrega un documento con pruebas sobre 50 vouchers de muestra, confirmando una tasa de acierto (accuracy) superior al 85%.<br><br>
      <i>Escenario 2: Validación de hardware (Consumo de RAM).</i><br><br>
      <b>Dado que</b> el procesamiento de imágenes es pesado,<br>
      <b>Cuando</b> el prototipo se ejecuta en dispositivos de gama media-baja,<br>
      <b>Entonces</b> documenta si el proceso arroja errores de "Out Of Memory" (OOM) o se mantiene estable.
  </td></tr>
</table>

<!-- US-48 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-48</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Spike: Integración de pasarela de pagos web (Niubiz/Stripe)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero investigar la API del procesador de pagos para documentar la arquitectura necesaria que permita el abono de cuotas con tarjeta de crédito/débito de manera segura.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Flujo de tokenización PCI-DSS.</i><br><br>
      <b>Dado que</b> se requiere alta seguridad en los cobros web,<br>
      <b>Cuando</b> el desarrollador evalúa el SDK web de la pasarela,<br>
      <b>Entonces</b> entrega un diagrama garantizando que los datos de la tarjeta viajan directamente del cliente al proveedor sin tocar nuestro backend (Tokenización).<br><br>
      <i>Escenario 2: Diseño del receptor de Webhooks.</i><br><br>
      <b>Dado que</b> el proveedor confirmará el cobro de forma asíncrona,<br>
      <b>Cuando</b> se presenta la arquitectura,<br>
      <b>Entonces</b> incluye el diseño del endpoint que recibirá e interpretará los eventos POST (Webhooks) de pago exitoso.
  </td></tr>
</table>

<!-- US-49 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-49</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Media</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Generación automatizada de documentación de API (Swagger)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero integrar herramientas de especificación OpenAPI para generar documentación viva facilitando el consumo por parte del equipo Frontend y Mobile.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Autogeneración tras despliegue.</i><br><br>
      <b>Dado que</b> se añaden o modifican endpoints en el código backend,<br>
      <b>Cuando</b> el servidor compila y arranca en el entorno de desarrollo,<br>
      <b>Entonces</b> actualiza automáticamente la interfaz gráfica de Swagger UI en la ruta `/api-docs`.<br><br>
      <i>Escenario 2: Restricción de interfaz en producción.</i><br><br>
      <b>Dado que</b> se despliega la aplicación final para los clientes,<br>
      <b>Cuando</b> la variable de entorno indique "producción",<br>
      <b>Entonces</b> la ruta de documentación de Swagger UI quedará deshabilitada por motivos de seguridad.
  </td></tr>
</table>

<!-- US-50 -->
<table style="width:100%; border-collapse: collapse; border: 1px solid black; margin-bottom: 20px; font-family: sans-serif;">
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center; width: 15%;">Story ID</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 35%;">User</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Priority</th><th style="border: 1px solid black; padding: 8px; text-align: center; width: 25%;">Epic</th></tr>
  <tr><td style="border: 1px solid black; padding: 8px; text-align: center;">US-50</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Developer</td><td style="border: 1px solid black; padding: 8px; text-align: center;">Alta</td><td style="border: 1px solid black; padding: 8px; text-align: center;">EP-05</td></tr>
  <tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Title</th><td colspan="3" style="border: 1px solid black; padding: 8px;">Configuración del Pipeline de Integración Continua (CI/CD)</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Description</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">Como Developer, quiero configurar un pipeline de GitHub Actions o GitLab CI automatizado para compilar código y ejecutar pruebas antes de mezclar a la rama principal.</td></tr>
  <tr><th colspan="4" style="border: 1px solid black; padding: 8px; text-align: center;">Acceptance Criteria</th></tr>
  <tr><td colspan="4" style="border: 1px solid black; padding: 8px;">
      <i>Escenario 1: Ejecución de Test Suite en PR.</i><br><br>
      <b>Dado que</b> un desarrollador abre un Pull Request hacia la rama `main`,<br>
      <b>Cuando</b> se dispara el evento en el repositorio remoto,<br>
      <b>Entonces</b> el servidor de CI instala dependencias y ejecuta toda la suite de pruebas unitarias automáticamente.<br><br>
      <i>Escenario 2: Prevención de código fallido.</i><br><br>
      <b>Dado que</b> el pipeline ejecuta la suite de pruebas,<br>
      <b>Cuando</b> uno o más tests unitarios fallan (código de salida != 0),<br>
      <b>Entonces</b> el flujo de CI se marca como rojo y el repositorio bloquea el botón de "Merge" hasta que el código sea arreglado.
  </td></tr>
</table>

### 2.4.2. Impact Mapping

### 2.4.3. Product Backlog
El Product Backlog traduce las necesidades de agentes comerciales de campo, compradores e inversionistas, y áreas de control financiero en una lista de trabajo ordenada por valor para el negocio. En el caso de inmoNode, el mayor valor se concentra inicialmente en reducir la pérdida de oportunidades comerciales y la dependencia del papel durante la prospección, separación de lotes y captura de comprobantes en zonas con conectividad limitada.

El orden propuesto no corresponde a una secuencia técnica de implementación. Se priorizan primero las capacidades que permiten mostrar la propuesta de valor, capturar información comercial relevante, proteger la disponibilidad del lote y conservar evidencia documental.

| Orden | User Story ID | Título | User Story | Story Points (1 / 2 / 3 / 5 / 8) | Sprint |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | US-P01 | Landing Page informativa | Como Comprador e Inversionista, quiero acceder a una Landing Page informativa sobre inmoNode y los proyectos disponibles para conocer la propuesta de valor y las alternativas de cotización. | 3 | Sprint 1 |
| 2 | US-15 | Explorar proyectos inmobiliarios | Como Comprador e Inversionista, quiero visualizar la lista de proyectos disponibles para evaluar opciones de compra según ubicación geográfica y precios base. | 3 | Sprint 1 |
| 3 | US-04 | Registrar prospectos offline | Como Agente Comercial de Campo, quiero registrar la información de nuevos clientes potenciales sin conexión para no perder oportunidades comerciales en zonas remotas. | 5 | Sprint 1 |
| 4 | US-05 | Consultar plano del proyecto | Como Agente Comercial de Campo, quiero abrir el plano detallado de la etapa del proyecto para explicar colindancias y áreas verdes al prospecto. | 5 | Sprint 1 |
| 5 | US-06 | Registrar separación offline | Como Agente Comercial de Campo, quiero registrar una separación de lote de forma local para asegurar la intención de compra del cliente en el terreno. | 8 | Sprint 1 |
| 6 | US-07 | Capturar voucher de separación | Como Agente Comercial de Campo, quiero utilizar la cámara para capturar la imagen del voucher físico de separación y adjuntarlo al expediente. | 5 | Sprint 2 |
| 7 | US-09 | Extraer datos del voucher | Como Agente Comercial de Campo, quiero que el sistema extraiga el monto, fecha y código de operación del voucher fotográfico para evitar errores de digitación manual. | 8 | Sprint 2 |
| 8 | US-10 | Corregir datos extraídos | Como Agente Comercial de Campo, quiero editar manualmente los datos pre-rellenados por el OCR en caso de que este haya cometido un error en la lectura de un número. | 3 | Sprint 2 |
| 9 | US-11 | Sincronizar registros pendientes | Como Agente Comercial de Campo, quiero que los registros locales se envíen al servidor automáticamente al recuperar conexión para asegurar la venta sin intervención manual. | 8 | Sprint 2 |
| 10 | US-12 | Resolver conflictos de disponibilidad | Como Agente Comercial de Campo, quiero ser notificado si un lote separado offline ya fue vendido por otro agente para reubicar al prospecto rápidamente. | 8 | Sprint 2 |
| 11 | US-17 | Simular financiamiento | Como Comprador e Inversionista, quiero simular cronogramas de pago en la web para analizar la viabilidad financiera de mi inversión sin necesidad de contactar a un agente. | 5 | Sprint 3 |
| 12 | US-19 | Solicitar separación web | Como Comprador e Inversionista, quiero solicitar la separación de un lote directamente desde la web para asegurar su adquisición rápidamente y retirarlo del mercado. | 8 | Sprint 3 |
| 13 | US-20 | Adjuntar comprobante web | Como Comprador e Inversionista, quiero adjuntar el comprobante de transferencia bancaria en la web para validar mi proceso de separación si decido no usar la pasarela online. | 5 | Sprint 3 |
| 14 | US-21 | Consultar contratos digitales | Como Comprador e Inversionista, quiero visualizar mi contrato de compra-venta y sus anexos de forma digital para verificar las cláusulas legales antes de la firma. | 5 | Sprint 3 |
| 15 | US-23 | Consultar estado de cuenta | Como Comprador e Inversionista, quiero visualizar un resumen de mi estado de cuenta para monitorear el saldo pendiente y el avance de pagos de mi lote. | 5 | Sprint 4 |
| 16 | US-24 | Recibir alertas de cuotas | Como Comprador e Inversionista, quiero recibir alertas automatizadas sobre mis próximas fechas de pago para evitar recargos por mora y mantener un historial financiero sano. | 5 | Sprint 4 |
| 17 | US-13 | Previsualizar contrato preliminar | Como Agente Comercial de Campo, quiero proyectar el contrato preliminar para que el cliente valide las cláusulas y montos antes de la firma oficial. | 5 | Sprint 4 |
| 18 | US-16 | Filtrar lotes en mapa | Como Comprador e Inversionista, quiero filtrar lotes específicos dentro de un proyecto por dimensiones, precio o ubicación para agilizar mi toma de decisiones. | 5 | Sprint 4 |
| 19 | US-18 | Descargar cotización | Como Comprador e Inversionista, quiero descargar la simulación de financiamiento en formato PDF para mantener un registro documental de la evaluación. | 3 | Sprint 4 |
| 20 | US-22 | Registrar conformidad contractual | Como Comprador e Inversionista, quiero registrar mi conformidad preliminar con los términos del contrato en el portal web para agilizar el proceso administrativo de firmas. | 3 | Sprint 4 |
| 21 | US-03 | Detectar conectividad | Como Agente Comercial de Campo, quiero que la aplicación detecte la pérdida de red para transicionar automáticamente al modo de trabajo offline sin interrumpir mi flujo. | 5 | Sprint 2 |
| 22 | US-02 | Descargar portafolio | Como Agente Comercial de Campo, quiero descargar el catálogo actualizado de lotes al iniciar sesión para asegurar la disponibilidad de la información durante el trabajo en campo sin internet. | 5 | Sprint 2 |
| 23 | US-08 | Comprimir imágenes | Como Agente Comercial de Campo, quiero que la aplicación reduzca el tamaño de las fotografías para consumir menos ancho de banda de mis datos móviles al enviar vouchers. | 3 | Sprint 3 |
| 24 | US-14 | Crear cuenta web | Como Comprador e Inversionista, quiero crear una cuenta en la plataforma web para explorar proyectos, simular precios y gestionar mis adquisiciones inmobiliarias. | 5 | Sprint 3 |
| 25 | US-01 | Autenticar acceso in situ | Como Agente Comercial de Campo, quiero autenticar mi identidad en la aplicación móvil para acceder al portafolio de lotes asignados de manera segura. | 5 | Sprint 2 |

La priorización propuesta utiliza como criterio principal el valor de negocio asociado a la continuidad de la venta en campo, la preservación de evidencia de pago y la reducción de errores que retrasan la formalización de separaciones. Por ello, las historias iniciales permiten informar al prospecto, registrar sus datos, consultar el lote y registrar la separación incluso cuando no existe conectividad.

Las capacidades de captura de voucher, extracción OCR y sincronización se ubican en una fase temprana porque materializan la diferenciación de inmoNode frente a procesos basados en papel. Luego se incorporan las capacidades de autoservicio web, cotización, reserva, contratos y seguimiento financiero, las cuales incrementan la transparencia para compradores e inversionistas. La autenticación se mantiene como una dependencia relevante, pero no encabeza automáticamente el backlog, pues su orden debe justificarse por el valor de la operación comercial y no únicamente por razones técnicas.

**Enlace público del Product Backlog:**  
[Ver Product Backlog en Miro](URL_PÚBLICA_DEL_PRODUCT_BACKLOG)

## 2.5. Strategic-Level Domain-Driven Design

El diseño estratégico basado en Domain-Driven Design se emplea en inmoNode para ordenar un dominio que reúne ventas de lotes en campo, gestión documental, validación de comprobantes, cotización, contratos y seguimiento financiero. El análisis parte de los procesos y requerimientos documentados, con énfasis en la continuidad operativa sin conexión, la disminución del uso de papel y la transparencia requerida por compradores e inversionistas.

La descomposición propuesta busca identificar subconjuntos del negocio con responsabilidades y lenguaje ubicuo propios, sin equipararlos automáticamente con pantallas o componentes técnicos. El trabajo sigue una secuencia: EventStorming permite explorar hechos relevantes del dominio; Candidate Context Discovery agrupa dichos hechos para proponer límites naturales; Domain Storytelling representa la colaboración entre contextos en escenarios de mayor valor; finalmente, los Bounded Context Canvases profundizan propósitos, reglas, capacidades, dependencias y puntos de validación de cada contexto candidato.

### 2.5.1. EventStorming

EventStorming se aplica para construir una primera representación compartida del dominio de comercialización de lotes, con foco en el recorrido que inicia cuando un agente comercial atiende a un prospecto en campo y continúa hasta la sincronización, verificación del comprobante y disponibilidad de información para el comprador. El propósito es hacer visibles los cambios de estado que actualmente se gestionan con registros manuales, vouchers físicos y comunicación no centralizada, identificando los momentos donde inmoNode aporta continuidad y trazabilidad.

El alcance abarca la exploración del lote, el registro del prospecto, la separación, la captura y digitalización del voucher, la sincronización de registros, el manejo de conflictos de disponibilidad, la recepción de comprobantes y la disponibilidad de contratos o estados de cuenta. La sesión de EventStorming tuvo una duración de 2 horas. 

El proceso se desarrolló de forma secuencial. Primero se identificaron los eventos de dominio redactados como hechos ya ocurridos. Luego se ordenaron temporalmente y se incorporaron comandos que expresan la intención previa a cada hecho. Sobre esa base se registraron actores, políticas, consultas de información, reglas y hotspots vinculados a conectividad, legibilidad del voucher, conflicto de disponibilidad y validación financiera. Finalmente, se revisó la secuencia para evitar duplicidades y diferenciar los eventos propios del negocio de los detalles de implementación.

| Orden | Tipo de elemento | Nombre | Propósito o descripción | Evidencia o justificación |
| :---: | :---: | :---: | :---: | :---: |
| 1 | Actor | Agente Comercial de Campo | Atiende al prospecto, consulta lotes y registra información durante el trabajo en terreno. | épica de Gestión Operativa In Situ. |
| 2 | Actor | Comprador e Inversionista | Explora proyectos, simula financiamiento, solicita separación, adjunta comprobantes y consulta documentos. | épicas EP-03 y EP-04. |
| 3 | Actor | Área administrativa o control financiero | Recibe información y requiere validar comprobantes para avanzar la separación y documentación. | US-20. |
| 4 | Consulta | Consultar disponibilidad y ficha del lote | Permite conocer el estado, área y demás información comercial disponible del lote antes de la separación. | US-05, US-15 y US-16. |
| 5 | Comando | Registrar prospecto | Expresa la intención de almacenar los datos de un nuevo cliente potencial. | US-04. |
| 6 | Evento de dominio | Prospecto registrado | Confirma que la información del prospecto fue registrada para continuar la gestión comercial. | US-04. |
| 7 | Comando | Registrar separación de lote | Expresa la intención de reservar un lote para el prospecto o comprador. | US-06 y US-19. |
| 8 | Regla de negocio | Lote disponible para separación | Un lote no debe separarse si ya figura como separado o vendido en la información disponible. | US-06 y US-19. |
| 9 | Evento de dominio | Lote separado | Representa el registro de la intención de separación del lote. En modo offline, queda pendiente de sincronización. | US-06. |
| 10 | Comando | Capturar voucher de pago | Expresa la intención de registrar evidencia documental de una separación. | US-07. |
| 11 | Evento de dominio | Voucher capturado | Confirma que la fotografía del comprobante fue asociada a la separación. | US-07. |
| 12 | Comando | Extraer datos del voucher | Solicita identificar monto, fecha y código de operación a partir de la imagen capturada. | US-09. |
| 13 | Evento de dominio | Datos del voucher extraídos | Indica que el OCR obtuvo datos del comprobante para su revisión o corrección. | US-09. |
| 14 | Política | Cuando la imagen sea ilegible, entonces solicitar una nueva captura | Evita continuar con información insuficiente para sustentar el comprobante. | US-09. |
| 15 | Comando | Corregir datos del voucher | Permite que el agente ajuste los datos extraídos cuando identifique una lectura incorrecta. | US-10. |
| 16 | Evento de dominio | Datos del voucher corregidos | Registra que los valores extraídos fueron modificados manualmente antes de su guardado. | US-10. |
| 17 | Evento de dominio | Conectividad recuperada | Señala que existe la condición necesaria para remitir los registros pendientes. | US-03 y US-11. |
| 18 | Comando | Sincronizar registros pendientes | Expresa la intención de transferir registros locales al repositorio central. | US-11. |
| 19 | Evento de dominio | Registros sincronizados | Confirma que los registros locales fueron transferidos y reconocidos como sincronizados. | US-11. |
| 20 | Política | Cuando una separación sincronizada entre en conflicto, entonces notificar conflicto de disponibilidad | Responde a la existencia de un lote vendido o separado por otro actor antes de consolidar la operación. | US-12. |
| 21 | Evento de dominio | Conflicto de disponibilidad detectado | Comunica que una separación no puede consolidarse por discrepancia con la disponibilidad central. | US-12. |
| 22 | Comando | Solicitar separación de lote | Expresa la intención del comprador de iniciar una reserva mediante el portal web. | US-19. |
| 23 | Evento de dominio | Solicitud de separación registrada | Confirma que se registró la intención formal de separar el lote desde la web. | US-19. |
| 24 | Comando | Adjuntar comprobante de pago | Expresa la intención del comprador de entregar evidencia de transferencia bancaria. | US-20. |
| 25 | Evento de dominio | Comprobante de pago recibido | Confirma que la evidencia fue recibida para el proceso de verificación. | US-20. |
| 26 | Evento de dominio | Lote en espera de verificación financiera | Indica que la separación requiere revisión financiera antes de avanzar. | US-20. |
| 27 | Evento de dominio | Contrato emitido | Representa que el back-office emitió el contrato preliminar disponible para el comprador. | US-21. |
| 28 | Consulta | Consultar contrato digital | Permite al comprador revisar contrato y anexos cuando estén emitidos. | US-21. |
| 29 | Consulta  | Consultar estado de cuenta | Permite visualizar monto pagado, deuda restante y avance de pago. | US-23. |
| 30 | Evento de dominio | Cuota vencida | Representa el cambio de estado de una cuota no registrada dentro de su fecha de vencimiento. | US-24. |
| 31 | Política | Cuando una cuota venza sin pago registrado, entonces clasificarla como vencida | Permite reflejar el estado de pago en el seguimiento financiero. | US-24. |

| Orden | Acción o comando | Evento de dominio resultante | Regla, decisión u observación |
| :---: | :---: | :---: | :---: |
| 1 | Consultar disponibilidad y ficha del lote | Información de lote consultada | La consulta debe diferenciar lotes disponibles, separados y vendidos según la información disponible. |
| 2 | Registrar prospecto | Prospecto registrado | El documento indica que ciertos datos, como documento de identidad, son obligatorios para el registro. |
| 3 | Registrar separación de lote | Lote separado | La separación offline queda pendiente de sincronización y no evita por sí sola conflictos con otros dispositivos. |
| 4 | Capturar voucher de pago | Voucher capturado | La evidencia debe asociarse a la separación correspondiente. |
| 5 | Extraer datos del voucher | Datos del voucher extraídos | Se obtienen monto, fecha y código de operación; la lectura requiere validación si existen errores. |
| 6 | Corregir datos del voucher | Datos del voucher corregidos | La corrección manual se contempla como alternativa ante limitaciones del OCR. |
| 7 | Sincronizar registros pendientes | Registros sincronizados | El flujo depende de la recuperación de conectividad. |
| 8 | Sincronizar separación pendiente | Conflicto de disponibilidad detectado | Si el lote ya fue vendido por otro actor, la separación local debe ser revisada y el agente debe ser notificado. |
| 9 | Solicitar separación de lote | Solicitud de separación registrada | La solicitud web depende de que el lote esté disponible y puede ser rechazada por concurrencia. |
| 10 | Adjuntar comprobante de pago | Comprobante de pago recibido | La recepción deriva en un estado de espera de verificación financiera. |
| 11 | Emitir contrato preliminar | Contrato emitido | La disponibilidad del contrato se vincula con la emisión por el back-office; sus reglas completas deben validarse. |
| 12 | Actualizar estado de cuenta | Cuota vencida | El documento indica que una cuota sin pago registrado puede clasificarse como vencida. |

**Figura. EventStorming del dominio**

![EventStorming del dominio](../assets/EventStorming.jpg)

#### 2.5.1.1. Candidate Context Discovery

La técnica aplicada es **Look-for-pivotal-events**, porque el flujo documentado presenta cambios de estado y de responsabilidad que permiten distinguir etapas de negocio: la separación de un lote, la captura y digitalización de un voucher, la sincronización de registros pendientes, la recepción de un comprobante para validación financiera y la emisión de un contrato. Estos eventos pivote modifican el tratamiento del lote, del comprobante y de la información del comprador, por lo que constituyen una base razonable para proponer límites de contexto.

Los eventos se agruparon considerando propósito de negocio, responsables, reglas, lenguaje ubicuo y transición de estados. La sesión de descubrimiento de contextos no se excedió de 2 horas.

| Contexto candidato | Propósito de negocio | Eventos asociados | Conceptos del lenguaje ubicuo | Actores | Responsabilidades | Justificación del límite | Clasificación estratégica |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Gestión Comercial en Campo | Permitir que el agente mantenga la continuidad de la atención comercial y registre información en lugares con conectividad limitada. | Prospecto registrado; Lote separado; Conectividad recuperada; Registros sincronizados; Conflicto de disponibilidad detectado. | Prospecto, lote, disponibilidad, separación, agente comercial, sincronización, conflicto. | Agente Comercial de Campo. | Consultar información de lote, registrar prospectos, registrar separaciones locales y gestionar registros pendientes de sincronización. | Su lenguaje se centra en la operación comercial in situ y en la continuidad de la venta, con reglas específicas de disponibilidad y operación offline. | Core, como propuesta sujeta a validación. |
| Gestión de Comprobantes | Digitalizar la evidencia de pago y obtener datos relevantes para reducir errores de transcripción y pérdida documental. | Voucher capturado; Datos del voucher extraídos; Datos del voucher corregidos; Comprobante de pago recibido. | Voucher, comprobante, monto, fecha, código de operación, OCR, corrección. | Agente Comercial de Campo; Comprador e Inversionista; área administrativa. | Capturar o recibir evidencia documental, extraer información, permitir corrección y entregar la evidencia para revisión. | El comprobante posee reglas, riesgos y terminología propios, especialmente por la legibilidad de la imagen y la corrección de datos extraídos. | Core, como propuesta sujeta a validación. |
| Cotización y Separación Digital | Facilitar que el comprador explore proyectos, revise lotes, simule financiamiento e inicie una solicitud de separación desde el canal web. | Solicitud de separación registrada. | Proyecto inmobiliario, lote, cotización, financiamiento, cuota inicial, solicitud de separación. | Comprador e Inversionista. | Exponer proyectos y lotes, permitir filtros, generar simulaciones y registrar la intención de separación. | El objetivo es apoyar la decisión y la adquisición autónoma del comprador, con reglas comerciales sobre disponibilidad e inicial mínima. | Supporting, como propuesta sujeta a validación. |
| Control Financiero y Documental | Verificar el avance de pagos y habilitar información contractual y financiera para el comprador. | Lote en espera de verificación financiera; Contrato emitido; Cuota vencida. | Verificación financiera, contrato, anexo, estado de cuenta, pago, cuota, vencimiento. | Área administrativa o control financiero; back-office; Comprador e Inversionista; área legal. | Gestionar el estado de verificación, disponibilizar contratos emitidos, consolidar estados de cuenta y reflejar cuotas vencidas. | El lenguaje y las decisiones se orientan a la trazabilidad financiera y documental posterior a la separación, diferenciándose de la operación comercial en campo. | Supporting, como propuesta sujeta a validación. |

**Gestión Comercial en Campo**

* Propósito: sostener la atención comercial y el registro de prospectos y separaciones en campo, incluso cuando la conectividad sea limitada.  
* Alcance: consulta de información del lote, registro de prospectos, separación local, identificación de registros pendientes y tratamiento del resultado de sincronización.  
* Elementos incluidos: prospecto, lote, estado de disponibilidad, separación, agente comercial, conectividad y conflicto de disponibilidad.  
* Elementos excluidos: extracción OCR del voucher, validación financiera, emisión de contratos, cálculo detallado de financiamiento y cobranza.  
* Eventos y reglas asociados: Prospecto registrado, Lote separado, Conectividad recuperada, Registros sincronizados y Conflicto de disponibilidad detectado; un lote separado o vendido no debe volver a separarse.  
* Razón de la delimitación: el contexto posee un propósito coherente centrado en evitar que la venta se interrumpa por falta de señal y en conservar la información comercial originada en el terreno.  
* Dependencias con otros contextos: entrega información de separación y prospecto a Gestión de Comprobantes y requiere la información consolidada de disponibilidad para identificar conflictos.

**Gestión de Comprobantes**

* Propósito: transformar una evidencia física o digital de pago en información trazable y disponible para el proceso de verificación.  
* Alcance: captura del voucher, recepción de comprobantes adjuntados, extracción OCR, revisión de legibilidad y corrección manual de datos.  
* Elementos incluidos: voucher, comprobante, imagen, monto, fecha, código de operación, datos extraídos y datos corregidos.  
* Elementos excluidos: decisión definitiva de aprobación financiera, cálculo de cuotas, emisión contractual y disponibilidad comercial del lote.  
* Eventos y reglas asociados: Voucher capturado, Datos del voucher extraídos, Datos del voucher corregidos y Comprobante de pago recibido; ante una imagen ilegible debe solicitarse una nueva captura.  
* Razón de la delimitación: el comprobante tiene una semántica propia y concentra el principal riesgo documental identificado en el caso: pérdida, deterioro, lectura deficiente o digitación errónea.  
* Dependencias con otros contextos: recibe la referencia de separación desde Gestión Comercial en Campo o Cotización y Separación Digital; entrega evidencia e información extraída a Control Financiero y Documental.

**Cotización y Separación Digital**

* Propósito: brindar al comprador e inversionista un canal de autoservicio para explorar alternativas de lote, evaluar financiamiento e iniciar una separación.  
* Alcance: catálogo de proyectos, información de lotes, filtros, simulación, descarga de cotización y solicitud formal de separación.  
* Elementos incluidos: proyecto inmobiliario, lote, cotización, financiamiento, cuota inicial, plazo, solicitud de separación y disponibilidad.  
* Elementos excluidos: registro offline en campo, procesamiento OCR de vouchers, validación administrativa del pago y emisión de contratos.  
* Eventos y reglas asociados: Solicitud de separación registrada; la solicitud depende de la disponibilidad del lote y la simulación debe respetar la inicial mínima documentada.  
* Razón de la delimitación: el lenguaje se enfoca en explorar, evaluar y solicitar, actividades orientadas a la decisión autónoma del comprador antes de la formalización administrativa.  
* Dependencias con otros contextos: consulta disponibilidad de lote; remite la solicitud de separación y el comprobante recibido a Gestión de Comprobantes y a Control Financiero y Documental.

**Control Financiero y Documental**

* Propósito: mantener la trazabilidad de pagos, verificación financiera, contratos y estados de cuenta que respaldan la relación posterior a la separación.  
* Alcance: estado de espera de verificación financiera, emisión y disponibilidad de contratos, consulta de estado de cuenta y tratamiento de cuotas vencidas.  
* Elementos incluidos: verificación financiera, contrato, anexos, estado de cuenta, pago registrado, saldo, cuota y vencimiento.  
* Elementos excluidos: captura inicial del voucher, lectura OCR, prospección, consulta de plano y simulación de financiamiento previa a la separación.  
* Eventos y reglas asociados: Lote en espera de verificación financiera, Contrato emitido y Cuota vencida; un contrato no debe mostrarse como disponible si aún no fue emitido.  
* Razón de la delimitación: el contexto agrupa decisiones de seguimiento financiero y documental que ocurren después de la recepción de evidencia y que involucran responsables administrativos y de back-office.  
* Dependencias con otros contextos: requiere comprobantes y datos de separación; comunica la emisión de contratos y la información de estado de cuenta a los canales de autoservicio.

**Figura. EventStorming inicial antes de la delimitación de contextos.**

![EventStorming del dominio](../assets/EventStorming.jpg)

**Figura. Candidate Context Discovery con agrupación de eventos y contextos candidatos.**

![Candidate Context Discovery](../assets/Candidate-Context-Discovery.jpg)

#### 2.5.1.2. Domain Message Flows Modeling

Los Domain Message Flows se elaboran mediante Domain Storytelling para representar cómo los contextos candidatos colaboran en escenarios de mayor valor. El objetivo no es describir interfaces técnicas, sino visibilizar qué actor inicia una interacción, qué información o mensaje se intercambia y qué responsabilidad de negocio asume cada contexto durante el flujo.

**Escenario: Separación de lote en campo con comprobante y sincronización**

* Objetivo de negocio: permitir que un agente comercial registre un prospecto, separe un lote y preserve la evidencia de pago aun cuando opere sin conexión.
* Actor iniciador: Agente Comercial de Campo.
* Evento o acción de inicio: registrar prospecto y seleccionar un lote disponible.
* Condición o evento de cierre: Registros sincronizados o Conflicto de disponibilidad detectado.
* Bounded Contexts participantes: Gestión Comercial en Campo, Gestión de Comprobantes y Control Financiero y Documental.
* Información o reglas relevantes: el lote debe encontrarse disponible según la información consultada; el voucher debe asociarse a la separación; si se recupera conectividad, los registros pendientes se sincronizan; puede ocurrir un conflicto de disponibilidad si el lote fue gestionado por otro actor.

| Paso | Emisor | Receptor | Tipo de mensaje | Nombre del mensaje | Propósito | Datos significativos | Disparador o condición |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Agente Comercial de Campo | Gestión Comercial en Campo | Consulta | Consultar disponibilidad y ficha del lote | Obtener información comercial para atender al prospecto. | Lote, estado de disponibilidad, área y datos del proyecto disponibles. | El prospecto solicita información sobre un lote. |
| 2 | Agente Comercial de Campo | Gestión Comercial en Campo | Comando | Registrar prospecto | Crear el registro comercial del potencial comprador. | Datos de contacto y documento de identidad requerido. | El agente recopila datos del prospecto. |
| 3 | Gestión Comercial en Campo | Agente Comercial de Campo | Evento | Prospecto registrado | Comunicar que el prospecto fue almacenado. | Referencia del prospecto registrado. | El registro cumple los datos obligatorios. |
| 4 | Agente Comercial de Campo | Gestión Comercial en Campo | Comando | Registrar separación de lote | Marcar la intención de separación del lote para el prospecto. | Lote, prospecto y estado de separación. | El lote figura disponible en la información local. |
| 5 | Gestión Comercial en Campo | Gestión de Comprobantes | Evento | Lote separado | Informar que existe una separación a la cual se asociará la evidencia de pago. | Referencia de separación y lote. | Se registró la separación en campo. |
| 6 | Agente Comercial de Campo | Gestión de Comprobantes | Comando | Capturar voucher de pago | Registrar la fotografía del comprobante de separación. | Imagen del voucher y referencia de separación. | El agente recibe la evidencia de pago. |
| 7 | Gestión de Comprobantes | Gestión de Comprobantes | Evento | Voucher capturado | Confirmar que la evidencia fue asociada a la separación. | Voucher y referencia de separación. | Se acepta la captura de la imagen. |
| 8 | Gestión de Comprobantes | Gestión de Comprobantes | Comando | Extraer datos del voucher | Obtener monto, fecha y código de operación del comprobante. | Imagen del voucher. | El voucher ha sido capturado. |
| 9 | Gestión de Comprobantes | Agente Comercial de Campo | Evento | Datos del voucher extraídos | Presentar los datos reconocidos para revisión. | Monto, fecha y código de operación. | El OCR procesa la imagen. |
| 10 | Agente Comercial de Campo | Gestión de Comprobantes | Comando | Corregir datos del voucher | Ajustar datos cuando el agente identifique una lectura incorrecta. | Datos corregidos del voucher. | El agente detecta una inconsistencia. |
| 11 | Gestión Comercial en Campo | Gestión Comercial en Campo | Evento | Conectividad recuperada | Indicar que existe condición para remitir datos pendientes. | Estado de conectividad. | El dispositivo recupera acceso a red. |
| 12 | Gestión Comercial en Campo | Control Financiero y Documental | Comando | Sincronizar registros pendientes | Transferir la separación y referencias asociadas para su consolidación. | Prospecto, lote, separación y estado pendiente. | Hay conectividad y registros pendientes. |
| 13 | Control Financiero y Documental | Gestión Comercial en Campo | Evento | Registros sincronizados | Confirmar que los registros fueron reconocidos por la información central. | Referencias sincronizadas. | No existe inconsistencia de disponibilidad. |
| 14 | Control Financiero y Documental | Gestión Comercial en Campo | Evento | Conflicto de disponibilidad detectado | Comunicar que el lote no puede consolidarse por una discrepancia de disponibilidad. | Lote y referencia de separación rechazada. | El lote ya figura vendido o separado por otro actor. |

El flujo respalda la separación entre Gestión Comercial en Campo y Gestión de Comprobantes: el primer contexto concentra la continuidad de la venta y la disponibilidad del lote, mientras que el segundo trata la evidencia de pago y su lectura. Control Financiero y Documental aparece cuando la información requiere consolidación o validación posterior. El principal punto de validación es determinar cómo se resolverá, a nivel de negocio, una separación offline que entra en conflicto después de sincronizarse.

**Figura. Domain Storytelling del escenario “Separación de lote en campo con comprobante y sincronización”.**

![Domain Message Flows 1](../assets/Domain-Message-Flows-1.jpg)

**Escenario: Solicitud web de separación y seguimiento documental**

* Objetivo de negocio: permitir que un comprador o inversionista explore un lote, solicite su separación, adjunte un comprobante y posteriormente acceda a información contractual y financiera.
* Actor iniciador: Comprador e Inversionista.
* Evento o acción de inicio: consultar proyectos, lotes y condiciones de financiamiento.
* Condición o evento de cierre: Contrato emitido o Lote en espera de verificación financiera, según el avance de la validación.
* Bounded Contexts participantes: Cotización y Separación Digital, Gestión de Comprobantes y Control Financiero y Documental.
* Información o reglas relevantes: el lote debe estar disponible; la simulación considera una inicial mínima; la solicitud puede ser rechazada por concurrencia; el comprobante se recibe para verificación financiera; el contrato solo se visualiza cuando ha sido emitido.

| Paso | Emisor | Receptor | Tipo de mensaje | Nombre del mensaje | Propósito | Datos significativos | Disparador o condición |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Comprador e Inversionista | Cotización y Separación Digital | Consulta | Consultar proyectos y lotes disponibles | Explorar alternativas de compra. | Proyecto, lote, precio base, disponibilidad y ubicación disponible. | El comprador ingresa al portal web. |
| 2 | Comprador e Inversionista | Cotización y Separación Digital | Comando | Simular financiamiento | Evaluar la viabilidad de compra de un lote seleccionado. | Lote, cuota inicial y plazo. | El comprador selecciona un lote. |
| 3 | Cotización y Separación Digital | Comprador e Inversionista | Respuesta | Presentar simulación de financiamiento | Mostrar el cronograma proyectado de cuotas. | Cuota inicial, cuotas y condiciones disponibles. | La simulación cumple la regla de inicial mínima. |
| 4 | Comprador e Inversionista | Cotización y Separación Digital | Comando | Solicitar separación de lote | Registrar la intención formal de reservar el lote. | Lote y datos de la solicitud. | El comprador decide iniciar la separación. |
| 5 | Cotización y Separación Digital | Gestión de Comprobantes | Evento | Solicitud de separación registrada | Comunicar que existe una solicitud a la que se puede asociar evidencia de pago. | Referencia de solicitud y lote. | El lote se encuentra disponible al registrar la solicitud. |
| 6 | Comprador e Inversionista | Gestión de Comprobantes | Comando | Adjuntar comprobante de pago | Entregar el comprobante de transferencia para la separación. | Archivo del comprobante y referencia de solicitud. | Existe una reserva pendiente dentro del plazo permitido. |
| 7 | Gestión de Comprobantes | Control Financiero y Documental | Evento | Comprobante de pago recibido | Informar que existe evidencia documental por verificar. | Comprobante y referencia de separación. | El archivo cumple las condiciones documentadas. |
| 8 | Control Financiero y Documental | Comprador e Inversionista | Evento | Lote en espera de verificación financiera | Comunicar que la evidencia ingresó al proceso de revisión. | Estado de separación. | Se recibió el comprobante. |
| 9 | Control Financiero y Documental | Comprador e Inversionista | Evento | Contrato emitido | Comunicar que el contrato preliminar está disponible. | Contrato y anexos emitidos. | El back-office emite el contrato. |
| 10 | Comprador e Inversionista | Control Financiero y Documental | Consulta | Consultar contrato digital | Acceder al contrato y anexos disponibles. | Contrato de compra-venta y anexos. | El contrato fue emitido. |
| 11 | Comprador e Inversionista | Control Financiero y Documental | Consulta | Consultar estado de cuenta | Revisar pagos, deuda restante y avance de pago. | Total pagado, saldo y estado de cuotas. | El comprador requiere seguimiento de su adquisición. |

Este flujo delimita con claridad la fase de decisión y solicitud respecto de la recepción del comprobante y del seguimiento financiero-documental. Cotización y Separación Digital no debería asumir la verificación de pago ni la emisión del contrato; su responsabilidad termina al registrar la solicitud y comunicarla. Gestión de Comprobantes conserva la responsabilidad sobre la evidencia, mientras que Control Financiero y Documental comunica estados posteriores que afectan la confianza y transparencia percibida por el comprador.

**Figura. Domain Storytelling del escenario “Solicitud web de separación y seguimiento documental”.**

![Domain Message Flows 2](../assets/Domain-Message-Flows-2.jpg)

#### 2.5.1.3. Bounded Context Canvases

Los Bounded Context Canvases se elaboran de manera iterativa. El proceso comienza con la definición del contexto y su propósito de negocio; luego se condensan reglas y términos del lenguaje ubicuo; se identifican capacidades; se agrupan por capas solo cuando la evidencia lo permite; se registran dependencias; y, finalmente, se realiza una crítica de diseño.

##### Bounded Context Canvas: Gestión Comercial en Campo

###### 1. Context Overview Definition

| Campo | Desarrollo |
| :---: | :---: |
| Nombre del Bounded Context | Gestión Comercial en Campo |
| Propósito de negocio | Permitir que el Agente Comercial de Campo mantenga la atención comercial y registre información de prospectos y separaciones de lote en zonas con conectividad limitada. |
| Problema o necesidad atendida | La dependencia del papel, la falta de señal y la posterior digitación manual ocasionan pérdida de información, retrasos y riesgo de perder oportunidades comerciales. |
| Actores que reciben valor | Agente Comercial de Campo; de forma indirecta, prospecto, comprador e inmobiliaria. |
| Alcance y responsabilidades | Consultar información del lote disponible, registrar prospectos, registrar separaciones locales, conservar registros pendientes y comunicar el resultado de sincronización. |
| Elementos explícitamente excluidos | Captura y OCR de vouchers, validación financiera, emisión de contratos, cálculo de financiamiento y gestión detallada del estado de cuenta. |
| Clasificación estratégica | Core, como propuesta sujeta a validación, debido a que aborda la operación offline que diferencia a inmoNode. |

###### 2. Business Rules Distillation & Ubiquitous Language Capture

| Campo | Desarrollo |
| :---: | :---: |
| Regla de negocio o política | Un lote que figure como separado o vendido no debe aceptar una nueva separación desde la información disponible para el agente. |
| Decisión de negocio que controla | Determinar si la intención de separación puede registrarse o debe rechazarse por indisponibilidad. |
| Término del lenguaje ubicuo | Lote disponible |
| Definición contextual del término | Lote cuya información disponible permite iniciar una separación; su condición puede cambiar al sincronizarse la operación con información central. |
| Regla de negocio o política | Cuando se recupera conectividad y existen registros pendientes, entonces se deben sincronizar los registros. |
| Decisión de negocio que controla | Determinar cuándo remitir la información registrada en campo para su consolidación. |
| Término del lenguaje ubicuo | Registro pendiente |
| Definición contextual del término | Información registrada localmente que aún no ha sido reconocida como sincronizada por la información central. |
| Regla de negocio o política | Cuando la separación sincronizada entra en conflicto, entonces se debe notificar al agente. |
| Decisión de negocio que controla | Determinar cómo comunicar la imposibilidad de consolidar una separación por discrepancia de disponibilidad. |
| Término del lenguaje ubicuo | Conflicto de disponibilidad |
| Definición contextual del término | Situación en la que una separación registrada en campo no puede consolidarse porque el lote figura como vendido o gestionado por otro actor. |

###### 3. Capability Analysis

| Capacidad de negocio | Descripción | Valor aportado | Relación con requerimientos, procesos o eventos |
| :---: | :---: | :---: | :---: |
| Consultar información de lote | Permitir al agente revisar disponibilidad y datos disponibles del lote durante la atención. | Reduce demoras al explicar el proyecto y mejora la calidad de la orientación comercial. | US-05; consulta de disponibilidad y ficha del lote. |
| Registrar prospecto | Conservar la información del cliente potencial aunque no exista conexión. | Evita pérdida de oportunidades comerciales y reduce la doble digitación posterior. | US-04; Prospecto registrado. |
| Registrar separación local | Registrar la intención de separación de un lote en campo. | Permite continuar la venta sin depender de conectividad inmediata. | US-06; Lote separado. |
| Sincronizar registros pendientes | Remitir información local cuando se recupera conectividad. | Centraliza la información y reduce el retraso administrativo. | US-11; Conectividad recuperada y Registros sincronizados. |
| Notificar conflicto de disponibilidad | Informar al agente si la separación no puede consolidarse. | Permite reorientar la atención del prospecto sin perder los datos recopilados. | US-12; Conflicto de disponibilidad detectado. |

###### 4. Dependencies Capture

| Tipo | Origen o destino | Mensaje, dato, evento o dependencia | Propósito | Riesgo o punto de validación |
| :---: | :---: | :---: | :---: | :---: |
| Saliente | Gestión de Comprobantes | Evento: Lote separado | Proveer la referencia de separación para asociar evidencia de pago. | Validar que exista una identificación de negocio suficiente para asociar correctamente la evidencia. |
| Saliente | Control Financiero y Documental | Comando: Sincronizar registros pendientes | Consolidar prospectos y separaciones registradas en campo. | Definir la regla de resolución cuando existan separaciones concurrentes. |
| Entrante | Control Financiero y Documental | Evento: Registros sincronizados | Confirmar la consolidación de la información. | Validar qué información queda visible al agente después de sincronizar. |
| Entrante | Control Financiero y Documental | Evento: Conflicto de disponibilidad detectado | Informar que una separación no se consolidó. | Determinar el tratamiento comercial posterior para el prospecto. |
| Datos requeridos | Información de lotes | Disponibilidad y ficha del lote | Informar la consulta y controlar el inicio de una separación. | La información local puede no reflejar cambios recientes cuando no existe conexión. |

Gestión Comercial en Campo mantiene cohesión porque concentra el ciclo de atención comercial iniciado por el agente y afectado por la falta de conectividad. Se diferencia de Gestión de Comprobantes al no procesar la evidencia de pago y de Control Financiero y Documental al no validar pagos ni emitir contratos. Su interacción más relevante ocurre cuando una separación y sus registros deben sincronizarse o cuando surge un conflicto de disponibilidad.

**Figura. Bounded Context Canvas de “Gestión Comercial en Campo”.**

![Bounded Context Canvas de Gestión Comercial en Campo](../assets/Bounded-Context-Canvas-Gestion-Comercial-en-Campo.jpg)

##### Bounded Context Canvas: Gestión de Comprobantes

###### 1. Context Overview Definition

| Campo | Desarrollo |
| :---: | :---: |
| Nombre del Bounded Context | Gestión de Comprobantes |
| Propósito de negocio | Digitalizar y organizar la evidencia de pago para disminuir la pérdida de vouchers físicos y reducir errores de digitación. |
| Problema o necesidad atendida | Los vouchers físicos pueden extraviarse, deteriorarse o resultar ilegibles; su transcripción manual ocasiona demoras y errores. |
| Actores que reciben valor | Agente Comercial de Campo, Comprador e Inversionista, área administrativa y control financiero. |
| Alcance y responsabilidades | Capturar vouchers en campo, recibir comprobantes adjuntados en web, extraer monto, fecha y código de operación, permitir la corrección de datos y comunicar la recepción de evidencia. |
| Elementos explícitamente excluidos | Aprobación definitiva del pago, resolución de conflictos de disponibilidad, emisión de contratos, cálculo de cuotas y gestión comercial de prospectos. |
| Clasificación estratégica | Core, como propuesta sujeta a validación, porque la digitalización documental y la extracción OCR forman parte de la diferenciación propuesta de inmoNode. |

###### 2. Business Rules Distillation & Ubiquitous Language Capture

| Campo | Desarrollo |
| :---: | :---: |
| Regla de negocio o política | Cuando la imagen del voucher sea ilegible, entonces se debe solicitar una nueva captura. |
| Decisión de negocio que controla | Determinar si la evidencia puede continuar hacia la extracción de datos o requiere ser recapturada. |
| Término del lenguaje ubicuo | Voucher |
| Definición contextual del término | Comprobante de pago físico o digital que sirve como evidencia de una separación o pago asociado. |
| Regla de negocio o política | La evidencia capturada debe asociarse a una separación o solicitud correspondiente. |
| Decisión de negocio que controla | Mantener la trazabilidad entre comprobante y operación comercial. |
| Término del lenguaje ubicuo | Comprobante de pago |
| Definición contextual del término | Evidencia documental que puede ser capturada por el agente o adjuntada por el comprador para ser revisada. |
| Regla de negocio o política | Los datos extraídos por OCR pueden ser corregidos manualmente cuando se identifique una lectura incorrecta. |
| Decisión de negocio que controla | Determinar el valor que debe conservarse como dato de comprobante antes de su envío a revisión. |
| Término del lenguaje ubicuo | Datos del voucher extraídos |
| Definición contextual del término | Monto, fecha y código de operación identificados desde la imagen del comprobante. |

###### 3. Capability Analysis

| Capacidad de negocio | Descripción | Valor aportado | Relación con requerimientos, procesos o eventos |
| :---: | :---: | :---: | :---: |
| Capturar voucher en campo | Registrar fotográficamente la evidencia de pago recibida por el agente. | Reduce el riesgo de pérdida o deterioro del comprobante físico. | US-07; Voucher capturado. |
| Extraer datos del voucher | Obtener automáticamente monto, fecha y código de operación desde la imagen. | Disminuye la digitación manual y el riesgo de error. | US-09; Datos del voucher extraídos. |
| Corregir datos extraídos | Permitir revisión humana cuando el OCR no represente correctamente la información. | Mantiene la continuidad operativa frente a limitaciones de legibilidad. | US-10; Datos del voucher corregidos. |
| Recibir comprobante web | Registrar evidencia adjuntada por el comprador desde el portal. | Ofrece una alternativa de entrega documental para la separación web. | US-20; Comprobante de pago recibido. |
| Comunicar recepción de evidencia | Informar que el comprobante está disponible para verificación financiera. | Da trazabilidad al inicio de la revisión administrativa. | US-20; Lote en espera de verificación financiera. |

###### 4. Dependencies Capture

| Tipo | Origen o destino | Mensaje, dato, evento o dependencia | Propósito | Riesgo o punto de validación |
| :---: | :---: | :---: | :---: | :---: |
| Entrante | Gestión Comercial en Campo | Evento: Lote separado | Vincular el voucher capturado con una separación registrada en campo. | Validar la referencia compartida de la separación. |
| Entrante | Cotización y Separación Digital | Evento: Solicitud de separación registrada | Vincular el comprobante adjuntado con la solicitud web. | Definir el tratamiento si el plazo de reserva expira antes de la recepción. |
| Saliente | Control Financiero y Documental | Evento: Comprobante de pago recibido | Comunicar que existe evidencia disponible para revisión financiera. | Definir qué campos son necesarios para la verificación. |
| Entrante | Agente Comercial de Campo | Comando: Capturar voucher de pago | Iniciar la digitalización de la evidencia física. | La calidad de imagen puede impedir el procesamiento. |
| Entrante | Comprador e Inversionista | Comando: Adjuntar comprobante de pago | Recibir evidencia documental desde la web. | Validar formatos y condiciones de aceptación sin introducir detalles técnicos no documentados. |

Gestión de Comprobantes se distingue porque administra el ciclo de vida de la evidencia de pago, desde su captura hasta la comunicación de su recepción. No decide la disponibilidad del lote ni valida definitivamente el pago; esas responsabilidades pertenecen a Gestión Comercial en Campo y Control Financiero y Documental, respectivamente. Su interacción esencial consiste en recibir referencias de separación y entregar comprobantes digitalizados para revisión.

**Figura. Bounded Context Canvas de “Gestión de Comprobantes”.**

![Bounded Context Canvas de Gestión de Comprobantes](../assets/Bounded-Context-Canvas-Gestion-de-Comprobantes.jpg)

##### Bounded Context Canvas: Cotización y Separación Digital

###### 1. Context Overview Definition

| Campo | Desarrollo |
| :---: | :---: |
| Nombre del Bounded Context | Cotización y Separación Digital |
| Propósito de negocio | Permitir que el Comprador e Inversionista explore proyectos, evalúe lotes y financiamiento, y registre una solicitud formal de separación desde el portal web. |
| Problema o necesidad atendida | Los compradores enfrentan procesos lentos y opacos para cotizar lotes y evaluar alternativas sin depender de la atención inmediata de un agente. |
| Actores que reciben valor | Comprador e Inversionista; de forma indirecta, agentes comerciales y empresas inmobiliarias. |
| Alcance y responsabilidades | Visualizar proyectos, consultar lotes, aplicar filtros, simular financiamiento, descargar cotizaciones y registrar solicitudes de separación. |
| Elementos explícitamente excluidos | Captura OCR de vouchers, validación financiera, emisión contractual, estado de cuenta y registro offline de campo. |
| Clasificación estratégica | Supporting, como propuesta sujeta a validación, pues habilita la experiencia de autoservicio y captación, pero el principal diferenciador declarado se concentra en la operación offline y digitalización documental. |

###### 2. Business Rules Distillation & Ubiquitous Language Capture

| Campo | Desarrollo |
| :---: | :---: |
| Regla de negocio o política | La simulación debe rechazar una cuota inicial inferior al porcentaje mínimo estipulado por las reglas de negocio. |
| Decisión de negocio que controla | Determinar si se puede presentar una simulación de financiamiento bajo las condiciones ingresadas. |
| Término del lenguaje ubicuo | Cuota inicial |
| Definición contextual del término | Monto ingresado por el comprador como parte inicial de la evaluación de financiamiento de un lote. |
| Regla de negocio o política | Una solicitud de separación se registra únicamente si el lote se encuentra disponible al momento de la validación. |
| Decisión de negocio que controla | Determinar si el comprador puede iniciar la reserva del lote seleccionado. |
| Término del lenguaje ubicuo | Solicitud de separación |
| Definición contextual del término | Intención formal del comprador de reservar un lote desde el portal web. |
| Regla de negocio o política | Cuando dos actores intentan separar el mismo lote, la solicitud posterior debe ser rechazada si el lote ya fue bloqueado. |
| Decisión de negocio que controla | Resolver la concurrencia de solicitudes sobre un mismo lote. |
| Término del lenguaje ubicuo | Lote disponible |
| Definición contextual del término | Lote visible para selección cuya disponibilidad debe ser confirmada al iniciar una solicitud de separación. |

###### 3. Capability Analysis

| Capacidad de negocio | Descripción | Valor aportado | Relación con requerimientos, procesos o eventos |
| :---: | :---: | :---: | :---: |
| Explorar proyectos | Mostrar proyectos inmobiliarios disponibles para evaluación. | Incrementa la transparencia y facilita el inicio de la decisión de compra. | US-15. |
| Filtrar lotes | Permitir buscar lotes por dimensiones, precio o ubicación. | Agiliza la identificación de opciones relevantes. | US-16. |
| Simular financiamiento | Generar un cronograma proyectado según lote, inicial y plazo. | Permite evaluar viabilidad financiera antes de contactar a un agente. | US-17. |
| Descargar cotización | Proporcionar un registro documental de la simulación. | Facilita la evaluación autónoma y la comunicación de la alternativa elegida. | US-18. |
| Solicitar separación | Registrar una intención formal de reserva del lote. | Acerca el proceso de exploración a la conversión comercial. | US-19; Solicitud de separación registrada. |

###### 4. Dependencies Capture

| Tipo | Origen o destino | Mensaje, dato, evento o dependencia | Propósito | Riesgo o punto de validación |
| :---: | :---: | :---: | :---: | :---: |
| Datos requeridos | Gestión Comercial en Campo o información consolidada de lotes | Disponibilidad, datos de lote y proyecto | Mostrar alternativas y validar la solicitud de separación. | La disponibilidad debe verificarse para evitar reservas concurrentes. |
| Saliente | Gestión de Comprobantes | Evento: Solicitud de separación registrada | Permitir asociar un comprobante de pago a la solicitud web. | Validar la referencia de negocio de la solicitud. |
| Saliente | Control Financiero y Documental | Información: solicitud de separación | Informar el inicio de un proceso que puede requerir seguimiento financiero. | Precisar cuándo corresponde remitir la información a revisión. |
| Entrante | Comprador e Inversionista | Comando: Simular financiamiento | Iniciar la evaluación de una alternativa de compra. | La regla exacta de inicial mínima debe ser validada. |
| Entrante | Comprador e Inversionista | Comando: Solicitar separación de lote | Iniciar una reserva desde el canal web. | Definir el comportamiento de negocio ante concurrencia. |

Cotización y Separación Digital conserva una responsabilidad clara: ayudar al comprador a descubrir, evaluar y solicitar un lote. Su límite se diferencia de Gestión Comercial en Campo por el canal y el propósito de autoservicio, y de Control Financiero y Documental porque no verifica pagos ni gestiona contratos. La interacción clave consiste en comunicar una solicitud de separación hacia los contextos que administran evidencia y seguimiento posterior.

**Figura. Bounded Context Canvas de “Cotización y Separación Digital”.**

![Bounded Context Canvas de Cotización y Separación Digital](../assets/Bounded-Context-Canvas-Cotizacion-y-Separacion-Digital.jpg)

##### Bounded Context Canvas: Control Financiero y Documental

###### 1. Context Overview Definition

| Campo | Desarrollo |
| :---: | :---: |
| Nombre del Bounded Context | Control Financiero y Documental |
| Propósito de negocio | Dar seguimiento a comprobantes pendientes de verificación, disponibilizar documentos contractuales emitidos y ofrecer transparencia sobre el estado de cuenta del comprador. |
| Problema o necesidad atendida | La dependencia de archivos físicos y conciliaciones manuales genera demoras, pérdida de trazabilidad y poca visibilidad para compradores e inversionistas. |
| Actores que reciben valor | Área administrativa, control financiero, back-office, área legal, Comprador e Inversionista y empresas inmobiliarias. |
| Alcance y responsabilidades | Recibir información de comprobantes para verificación, reflejar estados de espera, comunicar contratos emitidos, exponer estado de cuenta y registrar el estado de cuotas vencidas. |
| Elementos explícitamente excluidos | Captura de vouchers, extracción OCR, consulta inicial de proyectos, simulación de financiamiento, registro de prospectos y separación offline. |
| Clasificación estratégica | Supporting, como propuesta sujeta a validación, porque respalda la operación central mediante control, transparencia y documentación posterior a la separación. |

###### 2. Business Rules Distillation & Ubiquitous Language Capture

| Campo | Desarrollo |
| :---: | :---: |
| Regla de negocio o política | Cuando se recibe un comprobante de pago para una reserva pendiente, entonces el lote pasa al estado de espera de verificación financiera. |
| Decisión de negocio que controla | Determinar el estado visible de la operación mientras la evidencia aún no ha sido revisada. |
| Término del lenguaje ubicuo | Verificación financiera |
| Definición contextual del término | Revisión administrativa requerida después de recibir evidencia de pago antes de avanzar con información contractual. |
| Regla de negocio o política | El contrato se visualiza como disponible cuando ha sido emitido por el back-office. |
| Decisión de negocio que controla | Determinar la disponibilidad del contrato para consulta del comprador. |
| Término del lenguaje ubicuo | Contrato emitido |
| Definición contextual del término | Contrato preliminar y anexos que han sido generados por el back-office y pueden ponerse a disposición del comprador. |
| Regla de negocio o política | Cuando una cuota supera su vencimiento sin pago registrado, entonces se clasifica como vencida. |
| Decisión de negocio que controla | Actualizar el estado de cuenta y reflejar la situación de pago pendiente. |
| Término del lenguaje ubicuo | Cuota vencida |
| Definición contextual del término | Cuota cuyo vencimiento ya ocurrió sin que exista un pago registrado en la información disponible. |

###### 3. Capability Analysis

| Capacidad de negocio | Descripción | Valor aportado | Relación con requerimientos, procesos o eventos |
| :---: | :---: | :---: | :---: |
| Registrar espera de verificación financiera | Reflejar que se recibió evidencia de pago y que debe revisarse. | Da trazabilidad y transparencia sobre el avance de la separación. | US-20; Lote en espera de verificación financiera. |
| Disponibilizar contratos emitidos | Permitir que el comprador visualice contratos y anexos una vez emitidos. | Reduce dependencia de documentos físicos y mejora confianza. | US-21; Contrato emitido. |
| Registrar conformidad preliminar | Recoger la aceptación preliminar de términos contractuales en el portal. | Apoya la agilización del proceso administrativo de firmas. | US-22. |
| Exponer estado de cuenta | Mostrar monto pagado, saldo pendiente y avance de pagos. | Incrementa la transparencia financiera para el comprador. | US-23. |
| Comunicar vencimiento de cuotas | Reflejar cuotas vencidas y habilitar alertas de pago. | Facilita el seguimiento de obligaciones pendientes. | US-24; Cuota vencida. |

###### 4. Dependencies Capture

| Tipo | Origen o destino | Mensaje, dato, evento o dependencia | Propósito | Riesgo o punto de validación |
| :---: | :---: | :---: | :---: | :---: |
| Entrante | Gestión de Comprobantes | Evento: Comprobante de pago recibido | Iniciar el estado de espera de verificación financiera. | No se documentan los criterios definitivos de aprobación o rechazo. |
| Entrante | Gestión Comercial en Campo | Comando: Sincronizar registros pendientes | Consolidar información comercial originada en campo. | Validar la información necesaria para mantener trazabilidad. |
| Entrante | Cotización y Separación Digital | Información: solicitud de separación | Conocer la intención de reserva generada desde la web. | Determinar cuándo la solicitud debe pasar a seguimiento financiero. |
| Saliente | Comprador e Inversionista | Evento: Lote en espera de verificación financiera | Informar el estado posterior a la recepción de evidencia. | Validar el nivel de detalle que debe exponerse al comprador. |
| Saliente | Comprador e Inversionista | Evento: Contrato emitido | Comunicar la disponibilidad del contrato preliminar. | Confirmar reglas y responsables de emisión. |
| Saliente | Comprador e Inversionista | Respuesta: estado de cuenta | Permitir consulta de pagos, saldo y cuotas. | Validar la fuente de datos y reglas de actualización sin definir tecnología. |
| Saliente | Gestión Comercial en Campo | Evento: Registros sincronizados o Conflicto de disponibilidad detectado | Comunicar el resultado de consolidación de operaciones originadas offline. | Definir la autoridad que resuelve la disponibilidad final del lote. |

Control Financiero y Documental mantiene cohesión al reunir los estados y documentos que sustentan la relación posterior a la separación. Se diferencia de Gestión de Comprobantes porque no captura ni extrae información del voucher, y se diferencia de Cotización y Separación Digital porque no participa en la exploración ni en la decisión inicial de compra. Sus interacciones más relevantes parten de la recepción de comprobantes y culminan en la transparencia ofrecida al comprador mediante contratos y estados de cuenta.

**Figura. Bounded Context Canvas de “Control Financiero y Documental”.**

![Bounded Context Canvas de Control Financiero y Documental](../assets/Bounded-Context-Canvas-Control-Financiero-y-Documental.jpg)

### 2.5.2. Context Mapping

El Context Map define cómo se relacionan los cuatro Bounded Contexts identificados en los canvases y, sobre todo, quién se adapta a quién cuando dos contextos necesitan comunicarse. Antes de fijarlo, el equipo evaluó cuatro alternativas de partición siguiendo las preguntas del proceso de Context Mapping: qué pasaría si se unen dos contextos, si se parte uno, si se mueve una capability a otro contexto o si se crea un shared service.

|                                            Alternativa evaluada                                             |           Pregunta de diseño            |                                  Ventaja                                   |                                                                                                                                                                                Motivo del descarte                                                                                                                                                                                |
|:-----------------------------------------------------------------------------------------------------------:|:---------------------------------------:|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Unir Gestión Comercial en Campo y Cotización y Separación Digital en un solo contexto "Separación de Lotes" |   ¿Qué pasa si se unen dos contextos?   |     Un único modelo de separación y una sola regla de disponibilidad.      |                                               Los dos contextos atienden actores, canales y reglas distintas: el agente opera offline y sincroniza después, mientras que el comprador opera en línea con bloqueo inmediato por concurrencia. Unirlos mezclaría el modelo offline, que es el diferenciador, con el autoservicio web.                                               |
|                   Dejar Gestión de Comprobantes dentro de Control Financiero y Documental                   |  ¿Qué pasa si se mueve una capability?  | Evita una relación entre contextos: el comprobante nace donde se verifica. |                                                               La captura y la lectura OCR ocurren en campo, sin conexión y con reglas de legibilidad propias; la verificación es una decisión del back-office. Juntarlos llevaría la lógica de OCR a un contexto financiero y ataría dos ciclos de vida distintos.                                                                |
|               Extraer un contexto "Inventario de Lotes" como shared service de disponibilidad               | ¿Qué pasa si se crea un shared service? |           Una sola autoridad explícita sobre el estado del lote.           | El estado del lote solo cambia por separaciones y por la verificación del pago. Crear un contexto aparte duplicaría el modelo de lote y agregaría un salto en cada separación. Se asigna la autoridad a Control Financiero y Documental, porque la separación solo se consolida cuando existe evidencia verificada. Si la gestión de etapas y precios crece, se extraerá después. |
|           Partir Control Financiero y Documental en "Control Financiero" y "Gestión Contractual"            |   ¿Qué pasa si se parte un contexto?    |        Aísla la integración con el proveedor de firma electrónica.         |                                                         La emisión del contrato se dispara por la verificación financiera y la ejecuta el mismo back-office. Separarlos crearía una relación muy conversacional entre dos contextos pequeños. Es el primer candidato a extraerse cuando se integre la firma electrónica.                                                          |

A partir de estas decisiones se obtiene el siguiente mapa de contextos.

![Context Map de inmoNode](../assets/cap2/Context-Map.png)

### 2.5.3. Software Architecture

#### 2.5.3.1. Software Architecture Context Level Diagrams

#### 2.5.3.2. Software Architecture Container Level Diagrams

#### 2.5.3.3. Software Architecture Deployment Diagrams

## 2.6. Tactical-Level Domain-Driven Design

### 2.6.x. Bounded Context: <Bounded Context Name>

#### 2.6.x.1. Domain Layer

#### 2.6.x.2. Interface Layer

#### 2.6.x.3. Application Layer

#### 2.6.x.4 Infrastructure Layer

#### 2.6.x.5. Bounded Context Software Architecture Component Level Diagrams

#### 2.6.x.6. Bounded Context Software Architecture Code Level Diagrams

##### 2.6.x.6.1. Bounded Context Domain Layer Class Diagrams

##### 2.6.x.6.2. Bounded Context Database Design Diagram
