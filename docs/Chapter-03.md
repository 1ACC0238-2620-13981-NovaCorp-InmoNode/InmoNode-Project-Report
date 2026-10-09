# Capítulo III: Solution UI/UX Design

## 3.1. Product design

### 3.1.1. Style Guidelines

A continuación se presentan los styles guidelines, los cuales contemplan fuentes tipográficas, componentes gráficos y reglas visuales, con el objetivo de mantener una presentación consistente, coherente y enfocada en la usabilidad en todos los productos digitales del ecosistema **InmoNode**.

#### 3.1.1.1. General Style Guidelines

#### Branding y Tono de Comunicación
La [Figura 3.1](#figura-3-1) identifica el isotipo y logotipo corporativo de InmoNode. La [Figura 3.2](#figura-3-2) identifica las dimensiones del tono de comunicación y lenguaje aplicado en las plataformas.

<a id="figura-3-1"></a>
![Branding de InmoNode](../assets/cap3/branding.png)  
**Figura 3.1**  
*Branding oficial de InmoNode*

<a id="figura-3-2"></a>
![Tono de Lenguaje](../assets/cap3/language.png)  
**Figura 3.2**  
*Tono de comunicación y lenguaje aplicado*

* **Branding:** La identidad visual combina una mapa dividida en lotes con un puntero de ubicación. Las capas lineales inferiores simbolizan la infraestructura en varios niveles, mientras que las tonalidades verdes de los bloques representan el estado de disponibilidad y el crecimiento patrimonial de los proyectos.
* **Language (Serio - Formal):** Al tratarse de contratos legales y seguimiento de cuotas, el lenguaje utilizado es técnico, preciso y profesional. Se eliminan la ambigüedad y los modismos, priorizando la claridad conceptual en las etiquetas del sistema (como "Estado de Cuenta", "Mis Contratos", "Separar Lote" o "Escanear Voucher").

#### Paleta de Colores (Colors)
La [Figura 3.3](#figura-3-3) identifica la paleta de colores corporativa. La [Tabla 3.1](#tabla-3-1) permite comparar los códigos hexadecimales, roles y la justificación de uso en la interfaz.

<a id="figura-3-3"></a>
![Paleta de Colores](../assets/cap3/colors.png)  
**Figura 3.3**  
*Paleta de colores oficial de InmoNode*

<a id="tabla-3-1"></a>

##### Tabla 3.1
*Especificación de la Paleta de Colores de InmoNode*

| Nombre / Tono | Código Hex | Rol en el Sistema | Justificación y Aplicación |
| :--- | :--- | :--- | :--- |
| **Verde Claro (Light Green)** | `#87C757` | Color Secundario / Acento | Representa frescura, dinamismo y la disponibilidad de lotes. Se aplica en etiquetas de estado "Disponible", botones secundarios y elementos destacados de la app móvil. |
| **Verde Inmobiliario (Forest Green)** | `#319A4B` | Color Primario | Color institucional principal. Transmite crecimiento, seguridad y patrimonio. Utilizado en botones de acción principal (CTA), como "Separar Lote", "Sincronizar" y en el isotipo de la marca. |
| **Negro Puro (Dark Black)** | `#020202` | Color de Estructura y Texto | Aporta contraste máximo, firmeza y elegancia. Utilizado en barras de navegación, encabezados (H1, H2) y textos de alta prioridad en ambas plataformas. |
| **Blanco Claro (Off-White)** | `#F7F8F5` | Color de Fondo / Superficie | Fondo suave que reduce la fatiga visual en jornadas de trabajo prolongadas. Se utiliza como contenedor base para tarjetas del catálogo, formularios y módulos web. |
| **Amarillo Alerta (Yellow Alert)** | `#F0F66E` | Estado de Advertencia | Diseñado para llamar la atención sin transmitir error crítico. Se utiliza en el banner de "Modo sin conexión", alertas de cuotas próximas a vencer y estado "En espera de verificación". |
| **Naranja Terracota (Terracotta)** | `#E4572E` | Estado de Ocupado / Error | Aporta visibilidad inmediata sobre restricciones. Utilizado para marcar lotes "Vendidos" o "Bloqueados" en el mapa catastral, cuotas vencidas y errores de sincronización OCR. |

#### Tipografía (Typography)
La [Figura 3.4](#figura-3-4) identifica la especificación tipográfica adoptada para la Plataforma Web y la Aplicación Móvil (Android).

<a id="figura-3-4"></a>
![Especificación Tipográfica](../assets/cap3/typography.png)  
**Figura 3.4**  
*Reglas tipográficas para Web y Android*

* **Plataforma Web (Josefin Sans):** Se utiliza la fuente **Josefin Sans** para la jerarquía completa de la versión Web.
  * **Heading One:** Josefin Sans - 40 px. Títulos de secciones principales, portadas de proyectos y contadores del Dashboard.
  * **Heading Two:** Josefin Sans - 32 px. Títulos de módulos como "Estado de Cuenta", "Mis Contratos" y "Simulador".
  * **Body Regular / Bold:** Josefin Sans - 16 px. Párrafos, tablas de amortización, cláusulas de contratos y descripciones del catálogo.
* **Aplicación Móvil Android (Josefin Sans & Montserrat):** Combina la elegancia de Josefin Sans en encabezados con la alta legibilidad en pantallas pequeñas de Montserrat en cuerpos de texto.
  * **Heading One:** Josefin Sans - 40 px.
  * **Heading Two:** Josefin Sans - 32 px.
  * **Body Regular / Bold:** Montserrat - 14 px. Diseñada para formularios de registro in situ de prospectos, tarjetas de la cola de sincronización y datos extraídos por el motor OCR.

#### Espaciado y Retícula (Spacing)
La [Figura 3.5](#figura-3-5) identifica la unidad base de espaciado implementada en los componentes del sistema.

<a id="figura-3-5"></a>
![Unidad de Espaciado](../assets/cap3/spacing.png)  
**Figura 3.5**  
*Unidad base de espaciado (8 px)*

* **Grid System (8 px):** Todo el diseño de componentes, *paddings*, márgenes y áreas táctiles se calcula en múltiplos de **8 px** (8px, 16px, 24px, 32px, 48px). Esto garantiza que los botones e insumos interactivos en la App Móvil cumplan con las dimensiones mínimas de accesibilidad táctil para el trabajo del agente en terreno.

---

### 3.1.2. Information Architecture

#### 3.1.2.1. Organization Systems

La organización del contenido en InmoNode se estructura para diferenciar claramente las herramientas operativas de campo de la aplicación móvil y el entorno de autoservicio de la plataforma web, garantizando que cada perfil (agente comercial, comprador/inversionista) encuentre la información de manera eficiente.

**Plataforma Web**

Se aplica principalmente una **categorización según audiencia** y una **organización por tópicos** para separar el contenido público (Landing Page) del contenido privado (Dashboard del cliente):
*   **Organización Jerárquica (Visual Hierarchy):** En el Landing Page y portal público, la información fluye desde la propuesta de valor de la inmobiliaria hasta el catálogo de proyectos. El orden prioriza: Catálogo de proyectos -> Detalles del terreno -> Simulador de financiamiento.
*   **Organización por Tópicos:** Dentro del perfil privado del comprador, la información se agrupa en módulos temáticos específicos: Estado de Cuenta, Mis Contratos y Mis Pagos.

**Aplicación Móvil**
Dentro de la aplicación nativa orientada a la operatividad sin conexión a internet, se utilizan sistemas especializados:
*   **Organización Secuencial:** Se aplica estrictamente en los flujos críticos de ventas en campo, guiando al agente paso a paso: Selección de lote en mapa -> Registro de datos del prospecto -> Captura fotográfica de voucher -> Extracción de datos vía OCR -> Confirmación de separación.
*   **Organización Matricial / Espacial:** Empleada en la visualización del plano maestro catastral, donde los lotes se distribuyen geográficamente y se distinguen por su estado (disponible o vendido).
*   **Categorización Cronológica:** Utilizada para la cola de sincronización de registros offline, ordenando las transacciones locales desde la más antigua hasta la más reciente para su envío a la nube cuando se recupera la conexión.

#### 3.1.2.2. Labelling Systems

Las etiquetas han sido estandarizadas para mantener un lenguaje ubicuo (Ubiquitous Language) del dominio inmobiliario, buscando simplicidad y evitando ambigüedades técnicas tanto para el comprador como para el vendedor de campo.

**Plataforma Web**
*   **Proyectos:** Catálogo general de los proyectos inmobiliarios disponibles.
*   **Simulador:** Herramienta para calcular cuotas, plazos y tasas de interés.
*   **Estado de Cuenta:** Panel financiero con el histórico de recibos, deuda restante y avance de pagos.
*   **Mis Pagos:** Repositorio histórico de comprobantes y vouchers validados.
*   **Mis Contratos:** Repositorio para previsualizar, aceptar y descargar documentos legales.
*   **Certificado de No Adeudo:** Documento emitido al cancelar el 100% del lote.

**Aplicación Móvil**
*   **Mapa Catastral:** Plano interactivo georreferenciado de los lotes.
*   **Nuevo Prospecto:** Formulario para registrar potenciales clientes in situ.
*   **Separar Lote:** Acción para bloquear temporalmente la disponibilidad de un terreno.
*   **Escanear Voucher:** Activación de la cámara y el motor OCR para leer comprobantes.
*   **Modo Offline:** Indicador visual de pérdida de red y trabajo local.
*   **Sincronizar:** Envío de transacciones locales a la base central en la nube.

#### 3.1.2.3. SEO Tags and Meta Tags

**Plataforma Web**
*   **Title:** InmoNode: Plataforma de Gestión Inmobiliaria y Venta de Lotes.
*   **Description:** Cotiza, simula tu financiamiento y gestiona la compra de tu lote con total transparencia. Accede a tus contratos y estado de cuenta inmobiliario 24/7.
*   **Keywords:** compra de lotes, proyectos inmobiliarios, simulación de crédito inmobiliario, terrenos, InmoNode, NovaCorp.
*   **Author:** NovaCorp

**Aplicación Móvil**
*   **App Title:** InmoNode App - Ventas en Campo.
*   **App Subtitle:** CRM Inmobiliario Offline y OCR.
*   **App Description:** Herramienta indispensable para agentes comerciales. Registra prospectos, separa lotes en el mapa interactivo y escanea vouchers de pago sin necesidad de conexión a internet.
*   **App Keywords:** crm offline, ventas inmobiliarias, escaner vouchers OCR, proptech, agentes de campo.

#### 3.1.2.4. Searching Systems

Para manejar eficientemente el catálogo de lotes y los flujos financieros, se implementan herramientas de búsqueda visuales y dinámicas:

*   **Filtros Geométricos y Visuales (Web y App):** Los usuarios pueden filtrar los lotes en el mapa interactivo estableciendo rangos de metraje (ej. 120m2 a 150m2). El sistema recalcula los polígonos y aísla visualmente solo los lotes que cumplen los parámetros.
*   **Búsqueda por Estados en Mapa:** Los resultados de búsqueda se representan directamente en el plano catastral mediante colores, indicando visualmente si un lote está "Disponible", "Separado" o "Vendido" (bloqueados en color gris cuando no hay stock).
*   **Filtros Financieros (Web):** El comprador puede buscar dentro de su historial en la sección "Mis Pagos", filtrando vouchers por su estado administrativo ("Aprobado" o "Rechazado").
*   **Indicadores de Falta de Resultados:** Si los filtros aplicados por el usuario web no coinciden con ningún lote, el mapa muestra los lotes inactivos y despliega un mensaje claro indicando la ausencia de stock.

#### 3.1.2.5. Navigation Systems

El sistema de navegación está diseñado para ser altamente resiliente en campo y transparente para el comprador:

*   **Navegación Persistente (Bottom Navigation en Móvil):** En la aplicación para agentes, se prioriza un menú inferior para acceso rápido a las tareas de mayor frecuencia: Mapa Catastral, Registro de Prospectos y Cola de Sincronización.
*   **Navegación Contextual (Indicadores de Estado):** La aplicación móvil cuenta con un "Listener de red". Cuando se pierde la conexión, la navegación se adapta mostrando un banner persistente de "Modo sin conexión" para darle seguridad al agente de que puede seguir operando en la caché local.
*   **Navegación de Flujo (Wizard):** Para reducir la curva de aprendizaje y los errores operativos (como omitir fotos de DNI o datos), el proceso de *Separación de Lote* guía al agente pantalla por pantalla de forma obligatoria hasta la extracción del OCR.
*   **Menú Lateral (Dashboard Web):** Para el comprador, la plataforma web ofrece una barra de navegación estructurada (Sidebar) que le permite saltar fácilmente entre el Simulador de Financiamiento, su Estado de Cuenta y sus Contratos, dándole completa autonomía.

### 3.1.3. Landing Page UI Design

#### 3.1.3.1. Landing Page Wireframe

#### 3.1.3.2. Landing Page Mock-up

### 3.1.4. Mobile Applications UX/UI Design

En esta sección se presenta el diseño de experiencia e interfaz de **InmoNode App - Ventas en Campo**, la aplicación nativa para Android dirigida al segmento de *Agentes Comerciales de Campo* (User Persona: Azbel Capillo). El diseño se elaboró en **Figma** sobre un lienzo de 360 × 800 dp y se deriva de las historias de usuario de las épicas **EP-01 (Gestión Operativa In Situ)** y **EP-02 (Captura y Digitalización Documental)**, así como de los recursos REST que el backend expone para el rol `FIELD_AGENT` (sincronización de campo, portafolio offline y registro de vouchers).

#### 3.1.4.1. Mobile Applications Wireframes

Los wireframes representan la estructura de cada pantalla en baja fidelidad (escala de grises), sin aplicar todavía la paleta corporativa, con el fin de validar la jerarquía de contenido, los flujos y los estados de error antes del diseño visual. Todos los componentes respetan las *Style Guidelines* de la sección 3.1.1: retícula base de **8 px**, títulos en **Josefin Sans** (40 px y 32 px) y textos en **Montserrat 14 px**. Se reutilizan los mismos componentes de navegación definidos en la sección 3.1.2.5: barra de navegación inferior (Mapa, Prospectos, Sincronizar y Perfil), banner persistente de **"Modo sin conexión"** y un *wizard* de cuatro pasos para **Separar Lote**. Las notas amarillas indican el escenario Gherkin de la historia de usuario que representa la pantalla.

**Enlace al archivo de Figma:** [InmoNode – Wireframes (página *Mobile App Wireframes*)](https://www.figma.com/design/6OrCU2GtWZCuuiH5qCd4HX/InmoNode-%E2%80%93-Wireframes)

La [Tabla 3.2](#tabla-3-2) permite relacionar cada pantalla con las historias de usuario que atiende y con el recurso del backend que la alimenta.

<a id="tabla-3-2"></a>

##### Tabla 3.2
*Trazabilidad de los wireframes de la aplicación móvil*

| ID | Pantalla | User Stories | Recurso del backend |
| :--- | :--- | :--- | :--- |
| M01 | Splash | US-02 | Base de datos local (SQLite) |
| M02 | Iniciar sesión | US-01 | `POST /api/v1/auth/login` |
| M03 | Iniciar sesión – Acceso bloqueado | US-01 (Escenario 2) | `POST /api/v1/auth/login` |
| M04 | Descarga de portafolio | US-02 | `GET /api/v1/field-sync/portfolio` |
| M05 | Descarga incompleta | US-02 (Escenario 2) | `GET /api/v1/field-sync/portfolio` |
| M06 | Mapa Catastral | US-05 | Lotes GeoJSON del portafolio descargado |
| M07 | Mapa Catastral – Modo sin conexión y filtro | US-03, US-05 | Caché local |
| M08 | Detalle de lote | US-05 (Escenario 2) | Propiedades del lote: `code`, `area`, `front`, `depth`, `price` |
| M09 | Lote no disponible | US-06 (Escenario 2) | Caché local |
| M10 | Filtro sin resultados | Searching Systems (3.1.2.4) | Caché local |
| M11 | Simulación rápida | US-05 | `financingRules` del proyecto en el portafolio |
| M12 | Prospectos | US-04 | Base de datos local |
| M13 | Nuevo Prospecto | US-04 | `POST /api/v1/field-sync` (`prospects`) |
| M14 | Nuevo Prospecto – Validación | US-04 (Escenario 2) | Validación local del documento (8 a 12 caracteres) |
| M15 | Prospecto guardado | US-04, US-11 | Cola de sincronización local |
| M16 | Separar Lote – Paso 1: Prospecto | US-06 | `POST /api/v1/field-sync` (`reservations`) |
| M17 | Separar Lote – Paso 2: Escanear Voucher | US-07 | Cámara del dispositivo |
| M18 | Permiso de cámara | US-07 (Escenario 2) | Diálogo nativo de permisos |
| M19 | Imagen ilegible | US-09 (Escenario 2) | Motor OCR en el dispositivo |
| M20 | Separar Lote – Paso 3: Datos OCR | US-08, US-09, US-10 | `POST /api/v1/vouchers/upload-url` y `POST /api/v1/vouchers` |
| M21 | Separar Lote – Paso 4: Contrato preliminar | US-13 | Plantilla PDF local |
| M22 | Contrato – Datos faltantes | US-13 (Escenario 2) | Validación local |
| M23 | Separación registrada | US-06 | Cola de sincronización local |
| M24 | Cola de sincronización | US-08, US-11 | `POST /api/v1/field-sync` (resultados `SYNCED` y `DUPLICATE`) |
| M25 | Sincronización pausada | US-08 (Escenario 2), US-11 (Escenario 2) | Reintento automático |
| M26 | Conflicto de disponibilidad | US-12 | `POST /api/v1/field-sync` (resultado `CONFLICT` y `conflictReason`) |
| M27 | Reasignar lote | US-12 (Escenario 2) | `POST /api/v1/field-sync` |
| M28 | Perfil del agente | US-01, US-02 | `POST /api/v1/auth/logout` |
| M29 | Separaciones | US-54 | `GET /api/v1/reservations/{transactionId}/payment-evidences` |
| M30 | Detalle de separación | US-54 | `GET /api/v1/reservations/{transactionId}/payment-evidences` |
| M31 | Voucher rechazado | US-25, US-54 (Escenario 2) | `GET .../payment-evidences` y `POST /api/v1/vouchers` |

**Acceso e inicio de jornada**

La [Figura 3.6](#figura-3-6) presenta el ingreso del agente a la aplicación. El inicio de sesión utiliza el correo electrónico y la contraseña del agente; tras cinco intentos fallidos el acceso se bloquea durante 15 minutos. Una vez autenticado, la aplicación descarga el portafolio de proyectos, lotes y reglas de financiamiento para trabajar sin conexión; si la red se interrumpe durante la descarga, se conserva la última versión estable del catálogo.

<a id="figura-3-6"></a>
![Wireframes de acceso e inicio de jornada](../assets/cap3/mobile/wireframes/wf-01-acceso-jornada.png)  
**Figura 3.6**  
*Wireframes de acceso e inicio de jornada (M01–M05)*

**Mapa catastral y disponibilidad**

La [Figura 3.7](#figura-3-7) presenta el plano maestro del proyecto, renderizado desde la caché local. Los lotes se distinguen por estado (Disponible, Separado o Vendido) y pueden filtrarse por rango de metraje; cuando ningún lote cumple el filtro, el mapa los muestra inactivos y despliega un mensaje de ausencia de stock. Al seleccionar un lote se muestran su área, frente, fondo y precio base, junto con las acciones **Simular cuota**, que calcula la cuota con las reglas de financiamiento del proyecto, y **Separar Lote**.

<a id="figura-3-7"></a>
![Wireframes del mapa catastral](../assets/cap3/mobile/wireframes/wf-02-mapa-catastral.png)  
**Figura 3.7**  
*Wireframes del mapa catastral y la disponibilidad de lotes (M06–M11)*

**Registro de prospectos**

La [Figura 3.8](#figura-3-8) presenta el registro de prospectos sin conexión. El formulario solicita el nombre completo y el documento de identidad como datos obligatorios; el teléfono es opcional y el estado civil se requiere únicamente para generar el contrato preliminar. Cada registro se guarda en el dispositivo y se añade a la cola de sincronización.

<a id="figura-3-8"></a>
![Wireframes del registro de prospectos](../assets/cap3/mobile/wireframes/wf-03-prospectos.png)  
**Figura 3.8**  
*Wireframes del registro de prospectos (M12–M15)*

**Separar Lote**

La [Figura 3.9](#figura-3-9) y la [Figura 3.10](#figura-3-10) presentan el *wizard* de separación. En el primer paso se asocia el prospecto y el monto de separación; en el segundo se captura el voucher con la cámara, contemplando la solicitud de permisos y el rechazo de imágenes ilegibles. En el tercer paso el motor OCR completa el monto, la moneda, la fecha y el número de operación, mostrando su nivel de confianza; cualquier campo corregido manualmente queda marcado para el back-office. Finalmente, el agente previsualiza el contrato preliminar y confirma la separación, que queda pendiente de sincronizar.

<a id="figura-3-9"></a>
![Wireframes de Separar Lote, parte 1](../assets/cap3/mobile/wireframes/wf-04-separar-lote-1.png)  
**Figura 3.9**  
*Wireframes de Separar Lote: prospecto y captura del voucher (M16–M19)*

<a id="figura-3-10"></a>
![Wireframes de Separar Lote, parte 2](../assets/cap3/mobile/wireframes/wf-05-separar-lote-2.png)  
**Figura 3.10**  
*Wireframes de Separar Lote: datos OCR, contrato preliminar y confirmación (M20–M23)*

**Sincronización y conflictos**

La [Figura 3.11](#figura-3-11) presenta la cola de sincronización ordenada cronológicamente. Al recuperar la conexión, cada registro se envía al servidor y muestra su resultado: sincronizado (con la hora hasta la que el lote queda bloqueado), duplicado o en conflicto. Si la red es inestable, la transmisión se pausa y se reintenta automáticamente. Cuando otro actor tomó el lote antes de sincronizar, la aplicación conserva los datos del prospecto y permite reasignarle un nuevo lote disponible.

<a id="figura-3-11"></a>
![Wireframes de sincronización y conflictos](../assets/cap3/mobile/wireframes/wf-06-sincronizacion.png)  
**Figura 3.11**  
*Wireframes de sincronización, conflictos de disponibilidad y perfil (M24–M28)*

**Seguimiento de separaciones y vouchers**

La [Figura 3.12](#figura-3-12) presenta el seguimiento posterior a la sincronización. El agente consulta sus separaciones, el tiempo restante del bloqueo de 24 horas y el estado de verificación de cada voucher. Si el área administrativa rechaza un comprobante, se muestra el motivo, se conserva el historial de evidencias y se habilita el envío de un voucher sustituto desde campo.

<a id="figura-3-12"></a>
![Wireframes de seguimiento de separaciones](../assets/cap3/mobile/wireframes/wf-07-seguimiento.png)  
**Figura 3.12**  
*Wireframes del seguimiento de separaciones y vouchers (M29–M31)*

#### 3.1.4.2. Mobile Applications Wireflow Diagrams

Los *wireflows* combinan los wireframes de la sección anterior con las transiciones que los conectan, de modo que cada diagrama describe cómo el agente cumple un objetivo concreto dentro de la aplicación. Se elaboraron en Figma (página *Mobile Wireflows*) bajo la siguiente notación:

* **Zona de interacción (recuadro azul):** elemento que el agente toca para avanzar, como un botón, un lote del mapa o una pestaña.
* **Flecha continua:** transición provocada por una acción del agente o por una respuesta del sistema, rotulada con el evento que la origina (por ejemplo, *Credenciales válidas* o *Servidor responde CONFLICT*).
* **Flecha discontinua:** retorno a una pantalla ya visitada dentro del mismo flujo.

Se elaboró un wireflow por cada objetivo del agente identificado en el *User Task Matrix* y en el *User Journey* del Capítulo II: iniciar la jornada, explorar el mapa, registrar prospectos, separar lotes, sincronizar y dar seguimiento a la verificación de vouchers.

**Inicio de jornada**

La [Figura 3.13](#figura-3-13) presenta cómo el agente accede a la aplicación y obtiene el portafolio para trabajar sin conexión. Tras autenticarse, la descarga del portafolio conduce al Mapa Catastral; si la red se pierde durante la descarga, el agente puede continuar con la última versión estable del catálogo. El quinto intento fallido de inicio de sesión deriva a la pantalla de acceso bloqueado.

<a id="figura-3-13"></a>
![Wireflow de inicio de jornada](../assets/cap3/mobile/wireflows/wfl-01-inicio-jornada.png)  
**Figura 3.13**  
*Wireflow de inicio de jornada*

**Exploración del mapa catastral**

La [Figura 3.14](#figura-3-14) presenta la exploración del plano maestro. Al tocar un lote disponible se abre su ficha, desde la cual el agente puede simular la cuota o iniciar la separación; al tocar un lote vendido, el sistema informa su indisponibilidad. La aplicación de filtros sin conexión que no coinciden con ningún lote conduce al estado de ausencia de stock.

<a id="figura-3-14"></a>
![Wireflow de exploración del mapa catastral](../assets/cap3/mobile/wireflows/wfl-02-mapa-catastral.png)  
**Figura 3.14**  
*Wireflow de exploración del mapa catastral*

**Registro de prospectos offline**

La [Figura 3.15](#figura-3-15) presenta el registro de un cliente potencial desde la pestaña Prospectos. Si al guardar falta el documento de identidad, el formulario muestra la validación y, una vez corregido, el prospecto se guarda en el dispositivo y entra a la cola de sincronización.

<a id="figura-3-15"></a>
![Wireflow de registro de prospectos](../assets/cap3/mobile/wireflows/wfl-03-prospectos.png)  
**Figura 3.15**  
*Wireflow de registro de prospectos offline*

**Separar Lote con voucher y OCR**

La [Figura 3.16](#figura-3-16) presenta el flujo crítico de la aplicación. Desde la ficha del lote, el *wizard* guía al agente por la selección del prospecto, la captura del voucher, la verificación de los datos extraídos por OCR y la previsualización del contrato preliminar. El diagrama incluye los desvíos por falta de permiso de cámara, imagen ilegible (con retorno a la captura) y datos faltantes para generar el contrato.

<a id="figura-3-16"></a>
![Wireflow de Separar Lote](../assets/cap3/mobile/wireflows/wfl-04-separar-lote.png)  
**Figura 3.16**  
*Wireflow de Separar Lote con voucher y OCR*

**Sincronización y conflictos de disponibilidad**

La [Figura 3.17](#figura-3-17) presenta el envío de los registros offline. Cuando el servidor responde con un conflicto porque otro actor tomó el lote, el agente reasigna un nuevo lote al mismo prospecto y la nueva separación vuelve a la cola. Si la red es inestable, la sincronización se pausa y se reintenta automáticamente.

<a id="figura-3-17"></a>
![Wireflow de sincronización y conflictos](../assets/cap3/mobile/wireflows/wfl-05-sincronizacion.png)  
**Figura 3.17**  
*Wireflow de sincronización y conflictos de disponibilidad*

**Seguimiento de separaciones y voucher sustituto**

La [Figura 3.18](#figura-3-18) presenta el seguimiento de las separaciones sincronizadas. Desde la pestaña Separaciones, el agente consulta el estado de verificación y el contrato preliminar de cada separación; si un voucher fue rechazado, revisa el motivo y captura un voucher sustituto reutilizando el paso de escaneo del *wizard*.

<a id="figura-3-18"></a>
![Wireflow de seguimiento de separaciones](../assets/cap3/mobile/wireflows/wfl-06-seguimiento.png)  
**Figura 3.18**  
*Wireflow de seguimiento de separaciones y voucher sustituto*

#### 3.1.4.3. Mobile Applications Mock-ups

Los mock-ups representan la versión de alta fidelidad de las 31 pantallas de la aplicación móvil. Parten de la misma estructura de los wireframes y aplican la identidad visual definida en las *Style Guidelines* (sección 3.1.1): el isotipo de InmoNode, la paleta corporativa, la tipografía Josefin Sans y Montserrat, la retícula de 8 px y la iconografía **Material Symbols Rounded**, consistente con el lenguaje visual de Android. Se elaboraron en Figma, en la página *Mobile App Mock-ups*.

La [Tabla 3.3](#tabla-3-3) permite identificar cómo se aplicó cada color de la paleta sobre los componentes de la aplicación.

<a id="tabla-3-3"></a>

##### Tabla 3.3
*Aplicación de la paleta de colores en los mock-ups de la aplicación móvil*

| Color | Código Hex | Aplicación en la aplicación móvil |
| :--- | :--- | :--- |
| **Verde Inmobiliario** | `#319A4B` | Botones de acción principal (*Iniciar sesión*, *Separar Lote*, *Confirmar separación*), botón flotante *Nuevo Prospecto*, pestaña activa de la barra inferior, pasos completados del *wizard*, barras de progreso e íconos. |
| **Verde Claro** | `#87C757` | Lotes en estado **Disponible** en el mapa catastral, degradados de las imágenes de proyecto y etiquetas de estado positivo (*Verificada*, *Disponible*). |
| **Amarillo Alerta** | `#F0F66E` | Banner persistente de **Modo sin conexión**, lotes en estado **Separado** y etiquetas de estados en espera (*En verificación*, *Pendiente de sincronizar*). |
| **Naranja Terracota** | `#E4572E` | Lotes **Vendidos**, alertas de error (acceso bloqueado, imagen ilegible, conflicto de disponibilidad, voucher rechazado), campos con validación fallida y etiquetas *Rechazado* o *Vencida*. |
| **Negro Puro** | `#020202` | Títulos, textos de alta prioridad, barra de estado e íconos de navegación de retorno. |
| **Blanco Claro** | `#F7F8F5` | Fondo base de todas las pantallas, sobre el que se ubican tarjetas y formularios en blanco. |

**Acceso e inicio de jornada**

La [Figura 3.19](#figura-3-19) presenta las pantallas de ingreso con el isotipo de InmoNode. El error de acceso bloqueado se comunica en terracota y la descarga del portafolio muestra su avance con la barra de progreso en verde.

<a id="figura-3-19"></a>
![Mock-ups de acceso e inicio de jornada](../assets/cap3/mobile/mockups/mk-01-acceso-jornada.png)  
**Figura 3.19**  
*Mock-ups de acceso e inicio de jornada (M01–M05)*

**Mapa catastral y disponibilidad**

La [Figura 3.20](#figura-3-20) presenta el mapa catastral con la codificación cromática de los lotes: verde claro para los disponibles, amarillo para los separados y terracota para los vendidos. Los lotes que no cumplen un filtro se atenúan en gris, y el banner amarillo indica que el agente trabaja con datos locales.

<a id="figura-3-20"></a>
![Mock-ups del mapa catastral](../assets/cap3/mobile/mockups/mk-02-mapa-catastral.png)  
**Figura 3.20**  
*Mock-ups del mapa catastral y la disponibilidad de lotes (M06–M11)*

**Registro de prospectos**

La [Figura 3.21](#figura-3-21) presenta la lista y el formulario de prospectos. Cada registro indica si está pendiente de sincronizar, y la validación del documento de identidad se resalta en terracota junto al campo afectado.

<a id="figura-3-21"></a>
![Mock-ups del registro de prospectos](../assets/cap3/mobile/mockups/mk-03-prospectos.png)  
**Figura 3.21**  
*Mock-ups del registro de prospectos (M12–M15)*

**Separar Lote**

La [Figura 3.22](#figura-3-22) y la [Figura 3.23](#figura-3-23) presentan el *wizard* de separación. El indicador de pasos avanza en verde y la vista de cámara usa un fondo oscuro para facilitar el encuadre del voucher. En el paso de datos OCR, la confianza de la lectura se muestra como etiqueta y el campo editado manualmente queda señalado antes de confirmar la separación.

<a id="figura-3-22"></a>
![Mock-ups de Separar Lote, parte 1](../assets/cap3/mobile/mockups/mk-04-separar-lote-1.png)  
**Figura 3.22**  
*Mock-ups de Separar Lote: prospecto y captura del voucher (M16–M19)*

<a id="figura-3-23"></a>
![Mock-ups de Separar Lote, parte 2](../assets/cap3/mobile/mockups/mk-05-separar-lote-2.png)  
**Figura 3.23**  
*Mock-ups de Separar Lote: datos OCR, contrato preliminar y confirmación (M20–M23)*

**Sincronización y conflictos**

La [Figura 3.24](#figura-3-24) presenta la cola de sincronización, donde cada tipo de registro (separación, voucher o prospecto) se identifica con su propio ícono. Los conflictos de disponibilidad y las pausas por red inestable se destacan en terracota, y la reasignación de lote reutiliza el mapa catastral con la misma leyenda de estados.

<a id="figura-3-24"></a>
![Mock-ups de sincronización y conflictos](../assets/cap3/mobile/mockups/mk-06-sincronizacion.png)  
**Figura 3.24**  
*Mock-ups de sincronización, conflictos de disponibilidad y perfil (M24–M28)*

**Seguimiento de separaciones y vouchers**

La [Figura 3.25](#figura-3-25) presenta el seguimiento de las separaciones. Las etiquetas de estado aplican la paleta de forma consistente (amarillo en espera, verde verificado y terracota rechazado o vencido), y la línea de tiempo muestra el avance de la verificación del voucher.

<a id="figura-3-25"></a>
![Mock-ups de seguimiento de separaciones](../assets/cap3/mobile/mockups/mk-07-seguimiento.png)  
**Figura 3.25**  
*Mock-ups del seguimiento de separaciones y vouchers (M29–M31)*

#### 3.1.4.4. Mobile Applications User Flow Diagrams

Los *user flow diagrams* describen, para cada objetivo del agente comercial, la secuencia completa de pantallas, acciones, decisiones y procesos del sistema necesaria para cumplirlo. A diferencia de los wireflows, se centran en la lógica del recorrido: incluyen el camino principal (*happy path*) y los caminos alternos derivados de los escenarios Gherkin de las historias de usuario, e indican en qué punto interviene el backend. Se elaboraron en Figma (página *Mobile User Flows*) con la siguiente notación:

* **Inicio / Fin (verde):** evento que inicia el flujo y resultado esperado. Los finales alternos se muestran en terracota (fallo) o amarillo (resultado en espera).
* **Pantalla (borde verde):** vista de la aplicación, identificada con el código del wireframe correspondiente (M01–M31).
* **Acción del agente (verde claro):** interacción que realiza el usuario.
* **Proceso del sistema / API (gris, borde discontinuo):** operación local (SQLite, OCR, compresión) o llamada a un recurso del backend.
* **Decisión (rombo amarillo):** condición que bifurca el flujo, con sus salidas rotuladas.

**Iniciar la jornada de campo**

La [Figura 3.26](#figura-3-26) presenta el flujo de autenticación y descarga del portafolio. El *happy path* va desde el inicio de sesión hasta el Mapa Catastral con el portafolio guardado en el dispositivo. Los caminos alternos cubren las credenciales inválidas, el bloqueo tras el quinto intento fallido y la interrupción de la descarga, ante la cual el agente puede reintentar o continuar con la última versión estable.

<a id="figura-3-26"></a>
![User flow de inicio de jornada](../assets/cap3/mobile/user-flows/uf-01-inicio-jornada.png)  
**Figura 3.26**  
*User flow: iniciar la jornada de campo*

**Registrar un prospecto sin conexión**

La [Figura 3.27](#figura-3-27) presenta el registro de un cliente potencial. Si el nombre o el documento de identidad no son válidos, el formulario impide el guardado hasta que se completen; en caso contrario, el prospecto se guarda en SQLite y queda en la cola de sincronización.

<a id="figura-3-27"></a>
![User flow de registro de prospecto](../assets/cap3/mobile/user-flows/uf-02-registrar-prospecto.png)  
**Figura 3.27**  
*User flow: registrar un prospecto sin conexión*

**Separar un lote con voucher y OCR**

La [Figura 3.28](#figura-3-28) presenta el flujo principal de la aplicación. El agente verifica la disponibilidad del lote en la caché local, registra el prospecto y el monto, captura el voucher y valida los datos extraídos por OCR antes de previsualizar el contrato preliminar. Las decisiones del flujo atienden los escenarios alternos de las historias US-06, US-07, US-09, US-10 y US-13: lote no disponible, permiso de cámara denegado, imagen ilegible, corrección manual de datos (registrada como `manuallyCorrected`) y datos faltantes para el contrato.

<a id="figura-3-28"></a>
![User flow de separación de lote](../assets/cap3/mobile/user-flows/uf-03-separar-lote.png)  
**Figura 3.28**  
*User flow: separar un lote con voucher y OCR*

**Sincronizar registros y resolver conflictos**

La [Figura 3.29](#figura-3-29) presenta lo que ocurre al recuperar la conexión. La aplicación comprime los vouchers por debajo de 2 MB y envía los registros pendientes mediante `POST /api/v1/field-sync`. Según el resultado que devuelve el servidor para cada separación, el flujo continúa de tres formas: `SYNCED` bloquea el lote durante 24 horas y sube el voucher, `DUPLICATE` marca el registro como ya sincronizado y `CONFLICT` lleva al agente a reasignar un nuevo lote conservando los datos del prospecto. Si la respuesta supera los 15 segundos, la transmisión se pausa y se reintenta automáticamente.

<a id="figura-3-29"></a>
![User flow de sincronización](../assets/cap3/mobile/user-flows/uf-04-sincronizar.png)  
**Figura 3.29**  
*User flow: sincronizar registros y resolver conflictos*

**Dar seguimiento a la verificación del voucher**

La [Figura 3.30](#figura-3-30) presenta el seguimiento de una separación sincronizada a partir de las evidencias de pago que devuelve el backend. Una evidencia aprobada habilita la emisión del contrato; una pendiente se mantiene en espera mientras el bloqueo de 24 horas siga vigente, y vence si este expira; una rechazada permite al agente capturar y registrar un voucher sustituto.

<a id="figura-3-30"></a>
![User flow de seguimiento de vouchers](../assets/cap3/mobile/user-flows/uf-05-seguimiento.png)  
**Figura 3.30**  
*User flow: dar seguimiento a la verificación del voucher*

#### 3.1.4.5. Mobile Applications Prototyping
