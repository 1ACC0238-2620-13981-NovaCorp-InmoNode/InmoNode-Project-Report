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
* **Nombre y Apellidos:** 
* **Edad:** 
* **Distrito:** 
* **URL del Video Evidencia:** 
* **Timestamp de Inicio:** `hh:mm:ss`
* **Duración:** `mm:ss`

![Screenshot Entrevista 1](/assets/screenshot_entrevista1.png)

* **Resumen Descriptivo de la Entrevista:**

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

### 2.3.6. Ubiquitous Language

## 2.4. Requirements specification

### 2.4.1. User Stories

### 3.1. User Stories y Épicas

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

## 2.5. Strategic-Level Domain-Driven Design

### 2.5.1. EventStorming

#### 2.5.1.1. Candidate Context Discovery

#### 2.5.1.2. Domain Message Flows Modeling

#### 2.5.1.3. Bounded Context Canvases

### 2.5.2. Context Mapping

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
