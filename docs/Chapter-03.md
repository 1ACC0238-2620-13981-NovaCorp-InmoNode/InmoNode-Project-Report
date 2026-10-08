# Capítulo III: Solution UI/UX Design

## 3.1. Product design

### 3.1.1. Style Guidelines

#### 3.1.1.1. General Style Guidelines

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

### 3.1.3. Landing Page UI Design

#### 3.1.3.1. Landing Page Wireframe

#### 3.1.3.2. Landing Page Mock-up

### 3.1.4. Mobile Applications UX/UI Design

#### 3.1.4.1. Mobile Applications Wireframes

#### 3.1.4.2. Mobile Applications Wireflow Diagrams

#### 3.1.4.3. Mobile Applications Mock-ups

#### 3.1.4.4. Mobile Applications User Flow Diagrams

#### 3.1.4.5. Mobile Applications Prototyping
