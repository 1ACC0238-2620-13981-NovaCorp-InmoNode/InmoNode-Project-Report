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

## 2.2. Entrevistas

### 2.2.1. Diseño de entrevistas

### 2.2.2. Registro de entrevistas

### 2.2.3. Análisis de entrevistas

## 2.3. Needfinding

### 2.3.1. User Personas

### 2.3.2. User Task Matrix

### 2.3.3. User Journey Mapping

### 2.3.4. Empathy Mapping

### 2.3.5. Big Picture EventStorming

### 2.3.6. Ubiquitous Language

## 2.4. Requirements specification

### 2.4.1. User Stories

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
