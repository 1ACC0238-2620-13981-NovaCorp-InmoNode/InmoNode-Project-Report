# Objetivos SMART

# Capítulo I: Introducción

---

## 1.1. Startup Profile

---

### 1.1.1. Descripción de la Startup
NovaCorp es una startup tecnológica emergente enfocada en la modernización del sector inmobiliario a través de soluciones de software. Nuestro propósito es optimizar la comercialización, gestión documental y control financiero de lotes mediante herramientas multiplataforma innovadoras, escalables y centradas en el usuario.

| Atributo | Declaración Estratégica |
| :--- | :--- |
| **Misión** | Empoderar a los agentes comerciales y empresas inmobiliarias en la gestión de sus ventas mediante el desarrollo de aplicaciones inteligentes que faciliten el registro in situ, la digitalización documental y el seguimiento eficiente de cotizaciones. |
| **Visión** | Ser la *startup* líder en la región en la creación de ecosistemas digitales para el sector inmobiliario, transformando la manera en que la tecnología elimina la fricción operativa y conecta a inversionistas con oportunidades de forma transparente. |

### 1.1.2. Perfiles de integrantes del equipo

| **Nombre y Apellido** | Caisahuana Osores, Becker Junior - U202419462 |                                                                                                                                                                     
|:----------------------|:-----------------------------------------|
| **Descripcion**       | Especialista en el modelado, manejo y estructuración de la información. Su labor consiste en diseñar el esquema de persistencia de datos y apoyar en el desarrollo de los servicios internos, garantizando que los registros del sistema se almacenen de forma segura y eficiente.                                   |
| **Foto**              |<img src="../assets/member_Caisahuana_Becker.png" alt="Becker Caisahuana Profile Picture" height="120" width="100"/>

| **Nombre y Apellido** | Capillo Lema, Mía Valentina - U20241C101 |                                                                                                                                                                     
|:----------------------|:---------------------------------------------|
| **Descripcion**       | Responsable de conceptualizar y construir la experiencia visual de la plataforma. Su principal objetivo es asegurar que la aplicación sea intuitiva, atractiva y, sobre todo, que cumpla con los estándares de accesibilidad e inclusión necesarios para llegar a todo tipo de usuarios.                                 |
| **Foto**              |<img src="../assets/member_Capillo_Mia.jpeg" alt="Capillo Mia Profile Picture" height="120" width="100"/>

| **Nombre y Apellido** | Nuñez Soto, Andy Arturo - U20231E795 |                                                                                                                                                                     
|:----------------------|:-----------------------------------------|
| **Descripcion**       | Lidera la construcción de la interfaz interactiva con la que operará el usuario final. Su misión es transformar los diseños visuales en componentes completamente funcionales, asegurando un rendimiento fluido y una comunicación estable entre la pantalla del cliente y los servicios del servidor.                                   |
| **Foto**              |<img src="../assets/member_Nunez_Andy.jpeg" alt="Nuñez Andy Profile Picture" height="120" width="100"/>

| **Nombre y Apellido** | Perez Encarnacion, Breithner Rodolfo - U202418577 |                                                                                                                                                                     
|:----------------------|:-----------------------------------------|
| **Descripcion**       | Responsable de velar por la calidad del producto final y la organización del control de versiones. Se encarga de supervisar que el código cumpla con las convenciones establecidas por el equipo y de coordinar la publicación y el despliegue de la aplicación en los entornos correspondientes.                                   |
| **Foto**              |<img src="../assets/member_Perez_Breithner.jpeg" alt="Perez Breithner Profile Picture" height="120" width="100"/>

| **Nombre y Apellido** | Rocca Mariaca, Angel Mathias - U20231E515 |                                                                                                                                                                     
|:----------------------|:-----------------------------------------|
| **Descripcion**       | Encargado de diseñar la arquitectura base del sistema y definir las estrategias tecnológicas del proyecto. Su enfoque está en estructurar una solución sólida y escalable, además de gestionar la integración del OCR que potenciará la lógica central de la plataforma para la validación de vouchers.                                   |
| **Foto**              |<img src="../assets/member_Rocca_Angel.png" alt="Angel Rocca Profile Picture" height="120" width="100"/>

---

## 1.2. Solution Profile

---

### 1.2.1. Antecedentes y problemática
En la actualidad, la comercialización y gestión de lotes representa uno de los desafíos más críticos para las agencias inmobiliarias y promotoras. La necesidad de capturar datos de prospectos y registrar pagos de separación directamente en el campo a menudo colisiona con la falta de conectividad a internet en zonas de nuevos desarrollos. Esto obliga a los agentes comerciales a depender de procesos manuales, generando una alta incidencia de errores humanos, pérdida de vouchers físicos y retrasos significativos en la actualización de la información.

Si bien existen soluciones de software CRM en el mercado, la mayoría carecen de capacidades operativas offline y no resuelven la fricción del manejo de documentos físicos, resultando en lentitud administrativa. Frente a este escenario, se propone el desarrollo de **inmoNode**, una plataforma inteligente que integra captura de datos sin conexión y validación de vouchers mediante tecnología OCR (Reconocimiento Óptico de Caracteres) para ofrecer control financiero automatizado y un repositorio digital centralizado.

Para delimitar y comprender a profundidad el alcance de esta problemática, se emplea el marco de análisis **5W2H**:

* **Who (Quién):** Agentes comerciales de campo, analistas financieros de empresas inmobiliarias, e inversionistas o compradores que buscan una experiencia de cotización transparente.
* **What (Qué):** Ineficiencias operativas causadas por la gestión manual de documentos físicos, la incapacidad de registrar pagos in situ sin internet, y la falta de visibilidad en tiempo real del estado de los contratos y cotizaciones.
* **Where (Dónde):** En terrenos de desarrollo inmobiliario, zonas periféricas con baja cobertura de red, y oficinas administrativas de agencias de bienes raíces en el Perú y la región latinoamericana.
* **When (Cuándo):** Durante todo el ciclo de venta del lote, presentándose los mayores obstáculos en el momento de la prospección, el registro del pago de separación en campo, y la posterior conciliación financiera en la oficina.
* **Why (Por qué):** Debido a que el uso de papel es propenso a deterioro y pérdida, la falta de señal móvil impide el uso de sistemas en la nube en tiempo real, y los flujos manuales de digitalización de vouchers son lentos y propensos a la doble digitación.
* **How (Cómo):** El problema se manifiesta a través de cuellos de botella administrativos, demoras en la emisión de contratos y desconfianza por parte del comprador. Actualmente, los agentes lo mitigan tomando notas en papel que luego transcriben, lo que genera retrasos. Para resolver esto de forma efectiva, la integración de aplicaciones móviles con bases de datos locales y lectura automatizada (OCR) resulta fundamental, ya que la automatización de la gestión documental en campo reduce significativamente la fricción operativa y los errores de registro (Gartner, 2022, *The Future of Paperless Operations*).
* **How much (Cuánto):** La dependencia de archivos físicos y los procesos de doble digitación tienen un impacto financiero y operativo cuantificable. Se estima que las ineficiencias por el uso de documentos en papel y la doble entrada de datos pueden representar hasta una pérdida del 20% en la productividad administrativa de los equipos de ventas (McKinsey & Company, 2021, *Automation in Real Estate*). Asimismo, la lentitud en la respuesta y la falta de plataformas de autoservicio transparentes reducen las tasas de cierre de ventas, perdiendo un importante margen de prospectos digitales.

---

### 1.2.2. Lean UX Process

#### 1.2.2.1. Lean UX Problem Statements

Nuestra solución busca optimizar la gestión documental y operativa de los agentes de ventas mediante el uso de una app nativa con capacidades offline y tecnología OCR.
Hemos observado que los agentes comerciales de campo sufren ineficiencias operativas al depender de procesos manuales y archivos físicos para capturar datos en zonas con poca conectividad.
¿Cómo puede nuestro producto agilizar el registro in situ de pagos y documentos para reducir la fricción operativa y los errores humanos?

Nuestra solución busca facilitar la comercialización de lotes ofreciendo un portal accesible y transparente para los clientes. 
Hemos observado que los inversionistas y compradores enfrentan procesos lentos y opacos al momento de cotizar lotes y revisar el estado de sus contratos, lo que retrasa la toma de decisiones y afecta la confianza. 
¿Cómo puede nuestro producto centralizar la visualización de cotizaciones y contratos para acelerar el ciclo de ventas y captar más prospectos?

Nuestra solución busca garantizar un control financiero riguroso y automatizado mediante un repositorio digital centralizado. 
Hemos observado que las empresas inmobiliarias lidian con la pérdida de información y cuellos de botella administrativos generados por la dependencia de vouchers y comprobantes físicos. 
¿Cómo puede nuestro producto utilizar la digitalización automatizada para eliminar el papel y asegurar conciliaciones financieras rápidas y exactas?

#### 1.2.2.2. Lean UX Assumptions

**Business Assumptions:**

- Creemos que nuestros usuarios necesitan tener una herramienta integrada para gestionar todo el ciclo de comercialización y pago de lotes sin depender del papel.

- Estas necesidades se pueden satisfacer con un ecosistema multiplataforma (Web y App nativa) que automatice la lectura de comprobantes vía OCR y centralice los contratos.

- Nuestros clientes iniciales serán agencias de bienes raíces, promotoras de proyectos inmobiliarios, inversionistas y los agentes comerciales.

- El valor más importante que un cliente quiere de nuestros servicios es la agilidad para cotizar y la eliminación total del papeleo físico en sus transacciones.

- El cliente también va a obtener un control financiero exacto, inmediatez en el registro de datos in situ y mayor seguridad documental.

- Vamos a obtener la mayoría de los clientes mediante demostraciones directas del software a empresas inmobiliarias (B2B) y alianzas estratégicas con promotoras de lotes.

- Vamos a obtener ingresos mediante licencias de software SaaS, suscripciones escalonadas según el número de agentes o cobro por volumen de documentos procesados con OCR.

- Nuestra competencia en el mercado serán los CRMs inmobiliarios tradicionales que carecen de flujos offline robustos o que no integran digitalización automatizada nativa.

- Vamos a tener ventaja frente a nuestra competencia debido a la captura in situ sin conexión y la eliminación inmediata de la fricción física mediante inteligencia artificial (OCR).

- El mayor riesgo del servicio es la resistencia al cambio por parte de los agentes acostumbrados al papel, así como posibles fallos del OCR ante vouchers dañados, ilegibles o mal iluminados.

- Lo resolveremos diseñando interfaces móviles altamente intuitivas, integrando flujos de confirmación manual rápida para los escaneos y realizando capacitaciones prácticas.

**User Assumptions:**

- **¿Quien es el usuario?**

Los usuarios son agentes comerciales de campo que necesitan capturar datos en terrenos sin internet. También son los inversionistas y compradores que buscan cotizar y revisar contratos fácilmente. Finalmente, los administradores financieros que validan los pagos y gestionan el repositorio.

- **¿Que problemas tiene nuestro producto que resolver?**

Nuestro producto tiene que resolver la lentitud en la emisión de cotizaciones, el deterioro o pérdida de vouchers físicos, y la imposibilidad de registrar información comercial en zonas sin cobertura de red.

- **¿Que caracteristicas son importantes?**

Se incluye el acceso web para cotizaciones y vista de contratos, un repositorio digital centralizado, un modo offline estricto en la app móvil, el escaneo y extracción automática de datos de vouchers (OCR), y la sincronización automática al recuperar la conexión a internet.

- **¿Donde encaja nuestro producto en su trabajo o vida?**

El producto encaja como la herramienta de campo diaria e indispensable para los agentes de ventas, y como un portal de autoservicio confiable para que compradores e inversionistas gestionen y visualicen su patrimonio.

- **¿Cuando y como es nuestro producto usado?**

Se utiliza en el momento exacto de la prospección, separación y cierre de venta directamente en el terreno (App), y en cualquier momento desde una computadora o móvil para revisar estados de cuenta, pagos y contratos (Web).

- **¿Como debe verse nuestro producto y como debe comportarse?**

Debe ser extremadamente ágil y estable. La app nativa debe enfocarse en la rapidez de captura con la cámara (OCR) y dar retroalimentación clara sobre el estado de sincronización (offline/online), mientras que la web debe ofrecer dashboards limpios y estructurados para la gestión documental.

#### 1.2.2.3. Lean UX Hypothesis Statements

**Creemos** que una app nativa con modo offline y lectura OCR para los vouchers agilizará el trabajo in situ de los agentes comerciales.
**Sabremos que** hemos tenido éxito
**Cuando** el tiempo promedio de registro de una separación o venta en campo se reduzca significativamente y la tasa de errores de digitación disminuya.

**Creemos** que una plataforma web que permita a los compradores cotizar y visualizar sus contratos de manera transparente y autónoma aumentará el interés en los proyectos.
**Sabremos que** hemos tenido éxito
**Cuando** la tasa de conversión de prospectos a compradores activos se incremente y el tiempo de cierre de venta sea menor.

**Creemos** que la implementación de un repositorio digital centralizado eliminará la dependencia de archivos físicos en la administración de lotes.
**Sabremos que** hemos tenido éxito
**Cuando** el tiempo invertido en las auditorías de control financiero se reduzca y el número de reportes por pérdida de documentos físicos llegue a cero.
#### 1.2.2.4. Lean UX Canvas

## 1.3. Segmentos objetivo
