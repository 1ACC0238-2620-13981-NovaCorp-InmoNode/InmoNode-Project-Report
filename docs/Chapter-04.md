# Capítulo IV: Product Implementation & Validation

## 4. Product Implementation & Validation

### 4.1. Software Configuration Management

#### 4.1.1. Software Development Environment Configuration

#### 4.1.2. Source Code Management

#### 4.1.3. Source Code Style Guide & Conventions

#### 4.1.4. Software Deployment Configuration

### 4.2. Landing Page & Mobile Application Implementation

#### 4.2.1. Sprint n

##### 4.2.1.1. Sprint Planning n

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

##### 4.2.1.4. Development Evidence for Sprint Review

En la Sprint Review se resumirán los avances efectivamente implementados de Landing Page, flujos web, Web Services y aplicación móvil que correspondan al Sprint 1. Se relacionará cada avance con su repositorio, rama y commits verificables, diferenciando el prototipo de US-47 del código productivo.


| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commited on(Date) |
| --- | --- | --- | --- | --- | --- |

##### 4.2.1.5. Testing Suite Evidence for Sprint Review

Se documentará la suite automatizada de Web Services correspondiente al alcance del Sprint 1, distinguiendo Unit Tests, Integration Tests y Acceptance Tests. Los Unit Tests identificarán clases y comportamientos; las pruebas BDD incluirán el código Gherkin de los archivos `.feature`, sus archivos Steps y la explicación de su relación con las User Stories. Los resultados se consignarán solo después de la ejecución comprobada.


| Test Id | Test Type (Unit / Integration / Acceptance) | User Story Id | Class | Behavior | Test File | .feature File / Gherkin Code | Steps File | Explanation | Execution Result / Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commited on(Date) |
| --- | --- | --- | --- | --- | --- |

##### 4.2.1.6. Execution Evidence for Sprint Review

Esta sección resumirá lo alcanzado una vez que los flujos del Sprint 1 estén implementados y puedan ejecutarse. Se presentarán screenshots de las principales vistas, con explicación del flujo y su User Story, junto con un video que muestre la visualización y navegación logradas. Los escenarios de registro local se distinguirán de la sincronización futura y el spike OCR se identificará como prototipo.


| Product | User Story Id | Implemented View / Flow | Execution Summary | Screenshot | Explanation | Video URL |
| --- | --- | --- | --- | --- | --- | --- |

##### 4.2.1.7. Services Documentation Evidence for Sprint Review

Se resumirán los avances reales en documentación de Web Services del Sprint 1 mediante OpenAPI. Para cada endpoint se registrarán las acciones implementadas, verbo HTTP, sintaxis de llamada, parámetros, ejemplo y explicación del response, y enlace a la documentación desplegada o URL local si aún no hay despliegue. Las capturas deberán explicar la interacción con datos de muestra. Se identificarán el repositorio de Web Services y los commits asociados a la documentación.

| Endpoint | Implemented Action | HTTP Verb | Call Syntax | Parameters | Response Example | Response Explanation | Documentation URL |
| --- | --- | --- | --- | --- | --- | --- | --- |

| Endpoint / Action | Sample Data | Interaction Screenshot | Interaction Explanation |
| --- | --- | --- | --- |

| Web Services Repository URL | Commit Id | Documentation Change |
| --- | --- | --- |

##### 4.2.1.8. Software Deployment Evidence for Sprint Review

Se describirán los procesos de Deployment efectivamente realizados durante el Sprint 1 para Landing Page, Web Services y aplicaciones. La evidencia distinguirá creación de cuentas, configuración de recursos cloud, configuración de proyectos para integración o automatización, publicación e instalación en dispositivos. Cada paso se acompañará de capturas y explicación; se registrará el entorno y el resultado verificable sin publicar credenciales ni secretos.

| Product (Landing Page / Web Services / Applications) | Deployment Process / Step | Provider / Environment | Account | Cloud Resource | Project Configuration / Integration / Automation | Public URL / Device | Screenshot | Step Explanation / Verified Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### 4.2.1.9. Team Collaboration Insights during Sprint
