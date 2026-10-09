# Capítulo IV: Product Implementation & Validation

## 4. Product Implementation & Validation

La implementación de inmoNode, desarrollado por NovaCorp, comprende la Landing Page, los servicios RESTful, la aplicación Android para agentes comerciales y el frontend web para compradores y back-office. El trabajo se organiza por Sprints, relacionando las historias seleccionadas con evidencias de desarrollo, pruebas, documentación, despliegue y validación.

Los productos distribuyen las capacidades comerciales, documentales y financieras de los cuatro bounded contexts definidos en el diseño. Android concentra la operación en campo; el frontend web, el autoservicio y back-office; y los servicios RESTful, la consolidación e integración de información. La autenticación está especificada en las historias, sin que ello acredite su implementación.

Se selecciona ML Kit Text Recognition para el feature de aprendizaje autónomo asociado con US-47 y US-09. Se evaluará el reconocimiento local de vouchers y la interpretación de monto, fecha y código de operación, manteniendo revisión humana.

### 4.1. Software Configuration Management

En esta sección se establece decisiones comunes sobre entorno, organización del código, convenciones y despliegue.

#### 4.1.1. Software Development Environment Configuration

El equipo utiliza Jira, Spring Boot, Angular y Android Studio con Kotlin y Jetpack Compose.

| Actividad | Herramienta | Propósito en el proyecto | URL oficial de referencia o descarga |
| :---: | :---: | :---: | :---: |
| Gestión y requisitos | Jira | Gestionar el Product Backlog y su selección por Sprint. | [https\://www\.atlassian.com/software/jira](https://www.atlassian.com/software/jira) |
| Investigación UX | UXPressia | User Personas, mapas de empatía, recorridos e Impact Mapping | [https\://uxpressia.com/](https://uxpressia.com/) |
| Exploración del dominio | Miro | Big Picture EventStorming | [https\://miro.com/](https://miro.com/) |
| Diseño UX/UI | Figma | Wireframes, mock-ups y prototipos | [https\://www\.figma.com/](https://www.figma.com/) |
| Flujos de interacción | Lucidchart u Overflow | Wireflows y User Flows | [https\://www\.lucidchart.com/](https://www.lucidchart.com/) · [https\://overflow.io/](https://overflow.io/) |
| Arquitectura | Structurizr | Diagramas C4. Espacio | [https\://structurizr.com/](https://structurizr.com/) |
| UML y diseño de datos | Lucidchart; Lucidchart o Vertabelo | Diagramas UML y base de datos | [https\://www\.lucidchart.com/](https://www.lucidchart.com/) · [https\://vertabelo.com/](https://vertabelo.com/) |
| Desarrollo de Landing Page | HTML5, CSS3 y JavaScript | Sitio estático del modelo de negocio | [https\://developer.mozilla.org/](https://developer.mozilla.org/) |
| Desarrollo backend | Spring Boot | Servicios RESTful internos | [https\://spring.io/projects/spring-boot](https://spring.io/projects/spring-boot) |
| Desarrollo frontend | Angular | Portal del comprador y back-office. | [https\://angular.dev/](https://angular.dev/) |
| Diseño y componentes web | Material Design / Angular Material | Referencia visual y biblioteca exigidas | [https\://m3.material.io/](https://m3.material.io/) · [https\://material.angular.dev/](https://material.angular.dev/) |
| Desarrollo Android | Android Studio, Kotlin y Jetpack Compose | Aplicación nativa e interfaces | [https\://developer.android.com/studio](https://developer.android.com/studio) · [https\://kotlinlang.org/](https://kotlinlang.org/) · [https\://developer.android.com/compose](https://developer.android.com/compose) |
| Aprendizaje autónomo | ML Kit Text Recognition | Reconocimiento local de texto de vouchers | [https\://developers.google.com/ml-kit/vision/text-recognition/v2/android](https://developers.google.com/ml-kit/vision/text-recognition/v2/android) |
| Pruebas | Gherkin | Especificaciones de aceptación y comprobación de comportamientos | [https\://cucumber.io/docs/gherkin/reference/](https://cucumber.io/docs/gherkin/reference/) |
| Pruebas backend | Herramienta pendiente | Pruebas unitarias e integración; Spring Boot dispone de soporte oficial | [https\://docs.spring.io/spring-boot/reference/testing/index.html](https://docs.spring.io/spring-boot/reference/testing/index.html) |
| Documentación de servicios | OpenAPI / Swagger | Contratos RESTful | [https\://www\.openapis.org/](https://www.openapis.org/) · [https\://swagger.io/](https://swagger.io/) |
| Control de versiones | Git / GitHub | Historial y alojamiento del código | [https\://git-scm.com/](https://git-scm.com/) · [https\://github.com/](https://github.com/) |
| Despliegue | AWS y Docker | Infraestructura del diseño | [https\://aws.amazon.com/](https://aws.amazon.com/) · [https\://www\.docker.com/](https://www.docker.com/) |
| Documentación del informe | GitHub | Mantener el documento y sus versiones. | [https\://git-scm.com/](https://git-scm.com/) · [https\://github.com/](https://github.com/) |

 

#### 4.1.2. Source Code Management

Git registra modificaciones; GitHub aloja repositorios y facilita colaboración. Los Web Services deben conservar código y pruebas unitarias e integración/aceptación.

| Producto | URL | Contenido relevante |
| :---: | ----- | :---: |
| Landing Page | https\://github.com/1ACC0238-2620-13981-NovaCorp-InmoNode/InmoNode-Landing-Page.git | HTML, CSS, JavaScript y recursos. |
| Web Services | https\://github.com/1ACC0238-2620-13981-NovaCorp-InmoNode/InmoNode-Backend.git | Spring Boot, configuración y pruebas requeridas |
| Android |  | Kotlin/Compose, recursos y compilación. |
| Frontend web |  | Angular, vistas y consumo de servicios. |

 

| Rama | Propósito | Origen | Integración | Convención de nombre |
| :---: | :---: | :---: | :---: | :---: |
| main | Versiones preparadas para publicación | Inicialización | Recibe release y hotfix | main |
| develop | Integración del desarrollo | main | Recibe feature y correcciones | develop |
| feature | Una funcionalidad por rama | develop | develop | feature/\<story-id\>-\<short-description\> |
| release | Preparación de versión | develop | main y develop | release/\<MAJOR.MINOR.PATCH\> |
| hotfix | Corrección de versión publicada | main | main y develop | hotfix/\<MAJOR.MINOR.PATCH\> |

Si existe una release activa, el hotfix se incorpora también a ella y se conserva en develop al cerrarla.

Conventional Commits utiliza <type>[optional scope][!]: <description>. Ejemplos: feat(prospects): add offline prospect registration y fix(reservations): reject unavailable lots. Semantic Versioning utiliza MAJOR.MINOR.PATCH para cambios incompatibles, funcionalidades compatibles y correcciones compatibles, respectivamente.

#### 4.1.3. Source Code Style Guide & Conventions

La nomenclatura del código se mantendrá en inglés; los textos de interfaz podrán permanecer en español.

| Lenguaje | Guía de referencia | Convenciones principales propuestas |
| :---: | :---: | :---: |
| Kotlin | Kotlin Coding Conventions / Android Kotlin Style Guide | Clases e interfaces en UpperCamelCase; funciones y variables en lowerCamelCase; constantes en UPPER\_SNAKE\_CASE; paquetes en minúsculas y archivos descriptivos. Las funciones Compose de UI conservarán su convención específica. |
| Java, previsto | Google Java Style Guide | Clases e interfaces en UpperCamelCase; métodos y variables en lowerCamelCase; constantes en UPPER\_SNAKE\_CASE; paquetes en minúsculas y archivo con nombre de clase. |
| TypeScript, previsto | Google TypeScript Style Guide / Angular Style Guide | Clases e interfaces en UpperCamelCase; funciones y variables en lowerCamelCase; constantes globales en CONSTANT\_CASE; coherencia entre nombres de componentes, templates y estilos. |
| HTML y CSS | Google HTML/CSS Style Guide | HTML semántico, elementos en minúsculas, clases CSS descriptivas separadas por guiones y archivos en inglés. No aplican clases e interfaces como tipos de programación. |
| JavaScript | Google JavaScript Style Guide | Clases en UpperCamelCase; funciones y variables en lowerCamelCase; constantes globales en UPPER\_SNAKE\_CASE y archivos descriptivos. |
| Gherkin, planificado para .feature | Cucumber Gherkin Reference | Archivos, títulos y pasos descriptivos en inglés; precondición, acción y resultado separados mediante Given/When/Then; resultados observables y detalles irrelevantes excluidos. |

En Android, los bounded contexts presentes en la aplicación se organizarán en features/, con presentation, application, domain e infrastructure. Domain y Application contendrán Kotlin puro, sin SDK Android ni bibliotecas de persistencia/red. Las reglas residirán en Domain; ViewModels y estados, en Presentation; repositorios concretos y mappers, en Infrastructure. DTO y entidades de persistencia permanecerán aislados del dominio.

#### 4.1.4. Software Deployment Configuration

### 4.2. Landing Page & Mobile Application Implementation

La implementación se organiza desde el Product Backlog. Cada Sprint relaciona historias con desarrollo, pruebas, documentación y despliegue de Landing Page, aplicaciones y Web Services.

#### 4.2.1. Sprint 1

El Sprint 1 reúne presentación de inmoNode, exploración de proyectos, consulta del plano y registro local de prospectos y separaciones. Su valor es facilitar la evaluación del comprador y conservar información comercial sin conexión.

##### 4.2.1.1. Sprint Planning 1

La Sprint Planning 1 conserva las cinco historias seleccionadas y sus 24 Story Points. El Goal se propone desde el valor para compradores y agentes.

| Campo | Contenido |
| :---: | :---: |
| Sprint \# | Sprint 1 |
| Sprint Planning Background | Landing Page, exploración de proyectos y registro comercial local. |
| Date | 2026-10-05 |
| Time | 08:00 PM |
| Location | Reunión virtual |
| Prepared By | Perez Encarnacion, Breithner Rodolfo |
| Attendees (to planning meeting) | Caisahuana Osores, Becker Junior – Capillo Lema, Mía Valentina – Nuñez Soto, Andy Arturo – Rocca Mariaca, Angel Mathias |
| Sprint n – 1 Review Summary | Sprint 1 |
| Sprint n – 1 Retrospective Summary | Sprint 1 |
| Sprint Goal & User Stories | US-P01, US-15, US-04, US-05 y US-06. |
| Sprint 1 Goal | “Nuestro enfoque es permitir que compradores e inversionistas conozcan inmoNode y exploren proyectos, mientras los agentes conservan una atención comercial sin conexión. Consideramos que aporta una evaluación inicial informada y continuidad del registro en campo. En el Landing Page pueden consultarse proyectos y el agente pueda consultar el plano, registrar un prospecto y guardar una separación sin conexión”. |
| Sprint 1 Velocity | 24 |
| Sum of Story Points | 24 Story Points: 3 \+ 3 \+ 5 \+ 5 \+ 8\. |

##### 4.2.1.2. Aspect Leaders and Collaborators

Para el Sprint 1 se propone la siguiente Leadership-and-Collaboration Matrix (LACX). Los aspectos abarcan la Landing Page y sus flujos web asociados, los Backend Bounded Contexts, la Mobile App UI y su persistencia local, el Testing y el Deployment. Cada aspecto tiene un líder (L), encargado de coordinar su trabajo, y cuatro colaboradores (C), que podrán asumir tareas concretas del backlog.

| Team Member | GitHub Username        | Landing Page | Backend Bounded Contexts | Mobile App UI | Testing | Deployment |
| --- |------------------------| :---: | :---: | :---: | :---: | :---: |
| Caisahuana Osores, Becker Junior | becker693              | C | C | C | L | C |
| Capillo Lema, Mía Valentina | MiaCL-5 | C | L | C | C | C |
| Nuñez Soto, Andy Arturo | arturo-ns              | C | C | C | C | L |
| Perez Encarnacion, Breithner Rodolfo | Breithner1 | L | C | C | C | C |
| Rocca Mariaca, Angel Mathias | MRMpro13               | C | C | L | C | C |

Landing Page incluye la coordinación de los formularios web de US-14 y la exploración de US-15; Mobile App UI incluye los adaptadores y almacenamiento necesarios para US-01, US-02 y US-04, además del prototipo aislado de US-47. Mía coordinará los contratos del backend; Becker, las pruebas; Andy, el despliegue; Breithner, los flujos web; y Angel, los flujos móviles. La responsabilidad de cada tarea corresponde a un líder o colaborador de su aspecto, sin exigir que el líder implemente todas las tareas.

---
##### 4.2.1.3. Sprint Backlog 1

*Introducción resumiendo el objetivo principal del Sprint.*

**Enlace al Tablero de Trello:** [Insertar enlace aquí]

**Screenshot del Board:**
![Screenshot Trello](ruta_a_la_imagen.png)

| Sprint # | Sprint 1 | | | | | | |
| :---: | :--- | :---: | :--- | :--- | :---: | :---: | :--- |
| **User Story** | | **Work-Item / Task** | | | | | |
| **Id** | **Title** | **Id** | **Title** | **Description** | **Estimation (Hours)** | **Assigned To** | **Status** |
| US01 | [Título] | T01 | [Título Tarea] | [Desc] | [Horas] | [Nombre] | To-do/In-Process/Done |

---
##### 4.2.1.4. Development Evidence for Sprint Review

En la Sprint Review se resumirán los avances efectivamente implementados de Landing Page, flujos web, Web Services y aplicación móvil que correspondan al Sprint 1. Se relacionará cada avance con su repositorio, rama y commits verificables, diferenciando el prototipo de US-47 del código productivo.


| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commited on(Date) |
| --- | --- | --- | --- | --- | --- |

---
##### 4.2.1.5. Testing Suite Evidence for Sprint Review

Se documentará la suite automatizada de Web Services correspondiente al alcance del Sprint 1, distinguiendo Unit Tests, Integration Tests y Acceptance Tests. Los Unit Tests identificarán clases y comportamientos; las pruebas BDD incluirán el código Gherkin de los archivos `.feature`, sus archivos Steps y la explicación de su relación con las User Stories. Los resultados se consignarán solo después de la ejecución comprobada.


| Test Id | Test Type (Unit / Integration / Acceptance) | User Story Id | Class | Behavior | Test File | .feature File / Gherkin Code | Steps File | Explanation | Execution Result / Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commited on(Date) |
| --- | --- | --- | --- | --- | --- |

---
##### 4.2.1.6. Execution Evidence for Sprint Review

Esta sección resumirá lo alcanzado una vez que los flujos del Sprint 1 estén implementados y puedan ejecutarse. Se presentarán screenshots de las principales vistas, con explicación del flujo y su User Story, junto con un video que muestre la visualización y navegación logradas. Los escenarios de registro local se distinguirán de la sincronización futura y el spike OCR se identificará como prototipo.


| Product | User Story Id | Implemented View / Flow | Execution Summary | Screenshot | Explanation | Video URL |
| --- | --- | --- | --- | --- | --- | --- |

---
##### 4.2.1.7. Services Documentation Evidence for Sprint Review

Se resumirán los avances reales en documentación de Web Services del Sprint 1 mediante OpenAPI. Para cada endpoint se registrarán las acciones implementadas, verbo HTTP, sintaxis de llamada, parámetros, ejemplo y explicación del response, y enlace a la documentación desplegada o URL local si aún no hay despliegue. Las capturas deberán explicar la interacción con datos de muestra. Se identificarán el repositorio de Web Services y los commits asociados a la documentación.

| Endpoint | Implemented Action | HTTP Verb | Call Syntax | Parameters | Response Example | Response Explanation | Documentation URL |
| --- | --- | --- | --- | --- | --- | --- | --- |

| Endpoint / Action | Sample Data | Interaction Screenshot | Interaction Explanation |
| --- | --- | --- | --- |

| Web Services Repository URL | Commit Id | Documentation Change |
| --- | --- | --- |

---
##### 4.2.1.8. Software Deployment Evidence for Sprint Review

Se describirán los procesos de Deployment efectivamente realizados durante el Sprint 1 para Landing Page, Web Services y aplicaciones. La evidencia distinguirá creación de cuentas, configuración de recursos cloud, configuración de proyectos para integración o automatización, publicación e instalación en dispositivos. Cada paso se acompañará de capturas y explicación; se registrará el entorno y el resultado verificable sin publicar credenciales ni secretos.

| Product (Landing Page / Web Services / Applications) | Deployment Process / Step | Provider / Environment | Account | Cloud Resource | Project Configuration / Integration / Automation | Public URL / Device | Screenshot | Step Explanation / Verified Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

---
##### 4.2.1.9. Team Collaboration Insights during Sprint
