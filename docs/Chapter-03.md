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

#### 3.1.4.1. Mobile Applications Wireframes

#### 3.1.4.2. Mobile Applications Wireflow Diagrams

#### 3.1.4.3. Mobile Applications Mock-ups

#### 3.1.4.4. Mobile Applications User Flow Diagrams

#### 3.1.4.5. Mobile Applications Prototyping
