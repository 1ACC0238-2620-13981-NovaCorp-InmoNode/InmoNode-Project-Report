<div style="break-before: page; page-break-before: always;"></div>

<a id="conclusiones"></a>

# Conclusiones

<a id="conclusiones-y-recomendaciones"></a>

## Conclusiones y recomendaciones

**Conclusiones al cierre del Sprint 1 (TB1).**

1. El Problem Statement identificó como brecha principal la falta de operación offline y de digitalización de comprobantes en los CRM inmobiliarios. El Sprint 1 atacó la primera parte de esa brecha: la aplicación Android registra prospectos sin conexión, los conserva en la base local tras reiniciar la aplicación y rechaza los registros sin documento de identidad (US-04), como muestran las figuras 4.6 a 4.8.
2. La oferta inmobiliaria que consumen los demás procesos ya puede administrarse: los Web Services permiten dar de alta proyectos y lotes con su polígono catastral, publicarlos y consultarlos desde el catálogo público (US-51, US-52, US-53 y US-15). Las 63 pruebas automatizadas ejecutadas terminaron sin fallos, y el servicio está desplegado en Render con su documentación OpenAPI y protección por token.
3. La Landing Page está publicada en GitHub Pages y presenta la propuesta de valor a los dos segmentos objetivo, lo que da un canal público para la captación de agencias inmobiliarias planteada en los Business Assumptions.
4. Las Hypothesis Statements aún no pueden aceptarse ni rechazarse: el equipo no ha realizado las Validation Interviews con usuarios de los segmentos objetivo. Las métricas de éxito del Problem Statement (tiempo de registro en campo, conversión de prospectos y pérdida de comprobantes) se medirán a partir de esas sesiones.

**Recomendaciones y roadmap.**

1. En el Sprint 3, integrar con los Web Services y validar en el dispositivo el flujo de campo de la aplicación Android, cuyo código ya está en el repositorio: separación offline (US-06), captura del voucher (US-07), extracción OCR con ML Kit Text Recognition (US-09), corrección de los datos extraídos (US-10), sincronización automática (US-11) y resolución de conflictos de disponibilidad (US-12), validando la precisión del OCR con el spike US-47.
2. Realizar las Validation Interviews con al menos tres representantes por segmento sobre la Landing Page y la aplicación, y aplicar la evaluación según heurísticas para contrastar los assumptions con el comportamiento real de los usuarios.
3. Distribuir las aplicaciones Android y Flutter mediante Firebase App Distribution y planificar para el Release 2 la ampliación del autoservicio del comprador en la aplicación Flutter (US-19, US-20 y US-21).
4. Distribuir la implementación de cada producto según la LACX, de modo que todos los integrantes contribuyan a la aplicación móvil, la Landing Page y los Web Services.

<div style="break-before: page; page-break-before: always;"></div>

<a id="glosario"></a>

# Glosario

Los términos del dominio del negocio se definen en el Ubiquitous Language de la sección 2.3.6. Este glosario reúne los términos técnicos, metodológicos y las siglas utilizadas en el informe.

- **API (Application Programming Interface):** conjunto de operaciones que un sistema expone para que otros sistemas lo utilicen.
- **APK (Android Package Kit):** formato del archivo instalable de una aplicación Android.
- **ASO (App Store Optimization):** prácticas para mejorar la visibilidad de una aplicación en una tienda de aplicaciones.
- **BDD (Behavior-Driven Development):** práctica que especifica el comportamiento esperado del software mediante escenarios en lenguaje natural estructurado, como Gherkin.
- **Bounded Context:** límite explícito dentro del cual un modelo de dominio y su lenguaje tienen un significado único.
- **C4 Model:** técnica de representación de la arquitectura de software en cuatro niveles: contexto, contenedores, componentes y código.
- **CI (Continuous Integration):** práctica de compilar y probar automáticamente cada cambio integrado en el repositorio.
- **Conventional Commits:** convención para redactar mensajes de commit con un tipo, un alcance opcional y una descripción.
- **DDD (Domain-Driven Design):** enfoque de diseño de software que organiza el modelo y el código alrededor del dominio del negocio.
- **DTO (Data Transfer Object):** objeto que transporta datos entre capas o sistemas sin lógica de negocio.
- **ETag:** identificador de versión de un recurso HTTP que permite responder 304 Not Modified cuando el recurso no cambió.
- **EventStorming:** taller colaborativo que modela un dominio a partir de los eventos que ocurren en él.
- **GeoJSON:** formato estándar basado en JSON para representar geometrías geográficas, como los polígonos de los lotes.
- **Gherkin:** lenguaje estructurado con las palabras clave Given, When y Then para redactar criterios de aceptación.
- **GitFlow:** modelo de ramas de Git con ramas main, develop, feature, release y hotfix.
- **JWT (JSON Web Token):** token firmado que transporta la identidad y los roles de un usuario autenticado.
- **LACX (Leadership-and-Collaboration Matrix):** matriz que indica el líder y los colaboradores de cada aspecto de un Sprint.
- **Lean UX:** proceso que aplica supuestos, hipótesis y experimentación para orientar el diseño de productos digitales.
- **Material Design:** sistema de diseño de Google que define componentes, color, tipografía e interacción para Android y la web.
- **Mock-up:** representación visual de alta fidelidad de una pantalla, sin interacción.
- **OCR (Optical Character Recognition):** reconocimiento automático de texto en imágenes.
- **OpenAPI:** especificación estándar para describir APIs RESTful; Swagger UI la presenta de forma navegable.
- **Pull request:** solicitud para integrar los cambios de una rama en otra, que permite revisarlos antes de su integración.
- **REST (Representational State Transfer):** estilo arquitectónico para servicios web basado en recursos y verbos HTTP.
- **SaaS (Software as a Service):** modelo de distribución de software como servicio por suscripción.
- **SEO (Search Engine Optimization):** prácticas para mejorar la visibilidad de un sitio web en los motores de búsqueda.
- **Spike:** historia orientada a investigar o probar la viabilidad técnica de una solución antes de implementarla.
- **Sprint:** iteración de duración fija en la que el equipo entrega un incremento del producto.
- **Story Point:** unidad relativa para estimar el esfuerzo de una historia de usuario.
- **User Flow:** diagrama del recorrido de un usuario para cumplir un objetivo, con su camino principal y sus caminos alternos.
- **User Story:** descripción breve de una funcionalidad desde la perspectiva del usuario que la necesita.
- **Wireflow:** diagrama que combina wireframes con las transiciones entre ellos para un objetivo del usuario.
- **Wireframe:** representación de baja fidelidad de la estructura de una pantalla.

<div style="break-before: page; page-break-before: always;"></div>

<a id="bibliografia"></a>

# Bibliografía

**Métodos y técnicas de ingeniería de software**

Adzic, G. (2012). *Impact mapping: Making a big impact with software products and projects*. Provoking Thoughts.

Brandolini, A. (s.f.). *Introducing EventStorming*. Leanpub. https://leanpub.com/introducing_eventstorming

Brown, S. (s.f.). *The C4 model for visualising software architecture*. https://c4model.com/

Cohn, M. (2004). *User stories applied: For agile software development*. Addison-Wesley.

Conventional Commits. (s.f.). *Conventional Commits 1.0.0*. https://www.conventionalcommits.org/en/v1.0.0/

DDD Crew. (s.f.). *The Bounded Context Canvas*. GitHub. https://github.com/ddd-crew/bounded-context-canvas

Driessen, V. (2010, 5 de enero). *A successful Git branching model*. nvie.com. https://nvie.com/posts/a-successful-git-branching-model/

Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley.

Gothelf, J., & Seiden, J. (2021). *Lean UX: Applying lean principles to improve user experience* (3.ª ed.). O'Reilly Media.

Hofer, S., & Schwentner, H. (2021). *Domain storytelling: A collaborative, visual, and agile way to build domain-driven software*. Addison-Wesley.

Preston-Werner, T. (s.f.). *Semantic Versioning 2.0.0*. https://semver.org/

Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*. https://scrumguides.org/

**Lenguajes, frameworks y herramientas**

Android Developers. (s.f.-a). *Jetpack Compose*. https://developer.android.com/compose

Android Developers. (s.f.-b). *Save data in a local database using Room*. https://developer.android.com/training/data-storage/room

Cucumber. (s.f.). *Gherkin reference*. https://cucumber.io/docs/gherkin/reference/

Firebase. (s.f.). *Firebase App Distribution*. https://firebase.google.com/docs/app-distribution

GitHub. (s.f.). *GitHub Pages documentation*. https://docs.github.com/en/pages

Google. (s.f.-a). *Material Design 3*. https://m3.material.io/

Google. (s.f.-b). *Text recognition v2*. ML Kit. https://developers.google.com/ml-kit/vision/text-recognition/v2

OpenAPI Initiative. (2021). *OpenAPI Specification v3.1.0*. https://spec.openapis.org/oas/v3.1.0

Render. (s.f.). *Docker on Render*. https://render.com/docs/docker

Spring. (s.f.). *Spring Boot reference documentation*. https://docs.spring.io/spring-boot/

**Formato del documento**

American Psychological Association. (2020). *Publication manual of the American Psychological Association* (7.ª ed.).

<div style="break-before: page; page-break-before: always;"></div>

<a id="anexos"></a>

# Anexos

<a id="anexo-a-videos-de-exposiciones"></a>

## Anexo A. Videos de Exposiciones

La [Tabla A.1](#tabla-A-1) registra el enlace privado del video de exposición de cada entrega.

<a id="tabla-A-1"></a>

**Tabla A.1**

*Videos de exposición por entrega*

| Entrega | Contenido | Enlace |
|:---|:---|:---|
| TB1 | Exposición del Stage Review: capítulos III y IV y Sprint 1. | [Carpeta del video de exposición TB1](https://drive.google.com/drive/folders/1R6WQafmtbeu7hPq1Y36eYpJY4tSB80CM?usp=drive_link) |
