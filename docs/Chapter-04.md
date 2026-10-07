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

La distribución L/C es una **propuesta de planificación con asignación aleatoria autorizada**, no un registro de un acuerdo histórico ni de trabajo ejecutado. Los integrantes se toman del README del informe; los GitHub Username quedan pendientes de comprobación. Las asignaciones individuales del backlog se entienden como propuestas sujetas a disponibilidad y validación de capacidad en Sprint Planning.

| Team Member | GitHub Username | Landing Page | Backend Bounded Contexts | Mobile App UI | Testing | Deployment |
| --- | --- | :---: | :---: | :---: | :---: | :---: |
| Caisahuana Osores, Becker Junior | Pendiente de comprobar | C | C | C | L | C |
| Capillo Lema, Mía Valentina | Pendiente de comprobar | C | L | C | C | C |
| Nuñez Soto, Andy Arturo | Pendiente de comprobar | C | C | C | C | L |
| Perez Encarnacion, Breithner Rodolfo | Pendiente de comprobar | L | C | C | C | C |
| Rocca Mariaca, Angel Mathias | Pendiente de comprobar | C | C | L | C | C |

Landing Page incluye la coordinación de los formularios web de US-14 y la exploración de US-15; Mobile App UI incluye los adaptadores y almacenamiento necesarios para US-01, US-02 y US-04, además del prototipo aislado de US-47. Mía coordinará los contratos del backend; Becker, las pruebas; Andy, el despliegue; Breithner, los flujos web; y Angel, los flujos móviles. La responsabilidad de cada tarea corresponde a un líder o colaborador de su aspecto, sin exigir que el líder implemente todas las tareas.

##### 4.2.1.3. Sprint Backlog 1

**Sprint # 1 — Sprint Goal propuesto:** habilitar la base del catálogo mediante alta y publicación de proyectos y lotes, conectar la presentación pública con el registro y la exploración web, y preparar al agente para autenticarse, descargar el portafolio y registrar prospectos localmente sin conexión. Se incorporarán la optimización de GeoJSON, el caché de lecturas web y un spike de OCR para reducir incertidumbre antes de los flujos de separación y comprobantes de los siguientes sprints.

El alcance conserva las doce historias asignadas a Sprint 1 en el Capítulo II, sección 2.4.3, Tabla 2.60, consultado en `feature/chapter-02:docs/Chapter-02.md` mediante `git show`, sin cambiar de rama. Los títulos completos corresponden a 2.4.1. La descomposición, las horas y los responsables son una propuesta de planificación: los Story Points del Product Backlog no se convierten en horas. Todas las filas parten de **To Do** como estado inicial propuesto, no como lectura de un tablero existente. Se prevé el seguimiento con los estados To Do, In Process, To Review y Done; su evolución deberá demostrarse con evidencia real.

**URL público del Sprint Board: PENDIENTE — lo aportará el usuario.**

**Screenshot inicial del Sprint Board: PENDIENTE — el usuario aportará la captura del tablero del producto con las tareas del Sprint 1.** No se inserta una imagen ni un enlace hasta contar con un recurso verificable. El tablero `inmonode-report` coordina la redacción del informe y no sustituye el Sprint Board del producto. La URL abreviada del Product Backlog tampoco se reutiliza como evidencia.

El orden de negocio de la Tabla 2.60 no define el orden técnico de ejecución. US-51 precederá a US-52 y US-53; US-14 habilitará el acceso autenticado de US-15 y las redirecciones de US-P01; US-01 precederá a la descarga de US-02. La seguridad, migraciones, secretos, documentación base y pipeline asignados a Sprint 0 deberán verificarse como prerrequisitos, sin presumir que ya existen. US-04 se limita al guardado local y la cola pendiente: el envío de registros de US-11 pertenece a Sprint 2. US-47 será un prototipo de investigación, no la implementación productiva de OCR de US-09, también de Sprint 2.

Los contratos de 2.6 orientarán las tareas del backend: Catálogo Inmobiliario crea y publica la ficha y los eventos; Control Financiero y Documental mantiene la disponibilidad canónica. El caché acelera lecturas web y no autoriza bloqueos ni sirve la descarga de campo. Las tareas transversales se identifican como tales, sin crear nuevas User Stories.

| User Story Id | User Story Title | Task Id | Task Title | Description | Estimation (Hours) | Assigned To | Status (To Do / In Process / To Review / Done) |
| --- | --- | --- | --- | --- | :---: | --- | --- |
| US-51 | Alta de proyecto inmobiliario | S1-51-01 | Modelo y persistencia de Project | Definir nombre, ubicación y etapas obligatorios; crear migración y repositorio para Project en DRAFT según 2.6.5. | 6 | Capillo Lema, Mía Valentina | To Do |
| US-51 | Alta de proyecto inmobiliario | S1-51-02 | Comando y endpoint de alta | Implementar CreateProjectCommandHandler y POST /api/v1/catalog/projects con validación, autorización administrativa y ProjectCreatedEvent. | 8 | Capillo Lema, Mía Valentina | To Do |
| US-51 | Alta de proyecto inmobiliario | S1-51-03 | Formulario administrativo de proyecto | Construir formulario de nombre, ubicación y etapas; conectar el alta y mostrar rechazo por ubicación ausente. | 6 | Perez Encarnacion, Breithner Rodolfo | To Do |
| US-52 | Alta de lote con ficha técnica y polígono catastral | S1-52-01 | Modelo y validación geoespacial | Implementar LotDimensions, Money y GeoPolygon; validar figura cerrada, precio y pertenencia de etapa al proyecto. | 8 | Capillo Lema, Mía Valentina | To Do |
| US-52 | Alta de lote con ficha técnica y polígono catastral | S1-52-02 | Persistencia y endpoint de lote | Crear migración, repositorio y CreateLotCommandHandler para POST /api/v1/catalog/projects/{projectId}/lots, guardando DRAFT. | 8 | Nuñez Soto, Andy Arturo | To Do |
| US-52 | Alta de lote con ficha técnica y polígono catastral | S1-52-03 | Formulario de ficha técnica | Integrar código, dimensiones, área, precio y carga de coordenadas; presentar el error de polígono inválido sin guardar el lote. | 8 | Perez Encarnacion, Breithner Rodolfo | To Do |
| US-53 | Publicación de lote al catálogo | S1-53-01 | Publicación y activación de proyecto | Implementar PublishLotCommandHandler y PUT /api/v1/catalog/lots/{lotId}/publish; impedir publicación incompleta y activar el proyecto al publicar su primer lote. | 8 | Capillo Lema, Mía Valentina | To Do |
| US-53 | Publicación de lote al catálogo | S1-53-02 | Alta de inventario canónico por eventos | Conectar los eventos de catálogo a las proyecciones de proyectos y alta idempotente de Lot en Control Financiero y Documental, conservando lotId. | 8 | Nuñez Soto, Andy Arturo | To Do |
| US-53 | Publicación de lote al catálogo | S1-53-03 | Acción administrativa de publicación | Agregar confirmación de publicación y mensajes de datos faltantes a la vista del lote; reflejar el resultado sin decidir disponibilidad en Catálogo. | 4 | Perez Encarnacion, Breithner Rodolfo | To Do |
| US-P01 | Landing Page informativa | S1-P01-01 | Estructura responsiva y contenido | Construir secciones de propuesta de valor, pitch, proyectos destacados, CTA, contacto y redes; solicitar recursos reales sin inventar cuentas o capturas del producto. | 8 | Perez Encarnacion, Breithner Rodolfo | To Do |
| US-P01 | Landing Page informativa | S1-P01-02 | Navegación al registro y catálogo | Conectar proyecto destacado y Cotizar con US-15; dirigir a US-14 cuando no haya sesión, conservando el destino elegido. | 6 | Perez Encarnacion, Breithner Rodolfo | To Do |
| US-P01 | Landing Page informativa | S1-P01-03 | Pruebas públicas y responsivas | Automatizar acceso sin sesión y redirecciones; comprobar navegación y adaptación a tamaños móvil y escritorio. | 6 | Caisahuana Osores, Becker Junior | To Do |
| US-15 | Exploración del catálogo de proyectos inmobiliarios | S1-15-01 | Consulta autenticada de proyectos | Implementar consulta de proyectos activos con miniaturas, rango de precios y porcentaje de disponibilidad desde la autoridad canónica según 2.6. | 8 | Capillo Lema, Mía Valentina | To Do |
| US-15 | Exploración del catálogo de proyectos inmobiliarios | S1-15-02 | Vista de catálogo y Sold Out | Integrar la consulta en el portal autenticado, mostrar proyectos y conservar visibles los totalmente vendidos con etiqueta Sold Out. | 8 | Perez Encarnacion, Breithner Rodolfo | To Do |
| US-15 | Exploración del catálogo de proyectos inmobiliarios | S1-15-03 | Pruebas de exploración | Automatizar escenarios de proyecto activo, porcentaje de disponibilidad y proyecto vendido usando datos de prueba, no ventas reales. | 6 | Caisahuana Osores, Becker Junior | To Do |
| US-04 | Registro de prospectos offline | S1-04-01 | Guardado local y cola pendiente | Crear esquema SQLite y repositorio para nombre, documento, teléfono y UUID; guardar prospecto y entrada de cola en una transacción, sin enviar al servidor. | 8 | Rocca Mariaca, Angel Mathias | To Do |
| US-04 | Registro de prospectos offline | S1-04-02 | Formulario móvil offline | Construir formulario Material Design y validación de documento obligatorio; mostrar confirmación local y errores sin depender de la red. | 6 | Rocca Mariaca, Angel Mathias | To Do |
| US-04 | Registro de prospectos offline | S1-04-03 | Pruebas de persistencia sin red | Verificar guardado y cola tras reiniciar la app, rechazo de documento ausente y ausencia de envío; reservar sincronización para US-11. | 6 | Caisahuana Osores, Becker Junior | To Do |
| US-02 | Descarga de portafolio para inicio de jornada | S1-02-01 | Contrato de descarga de campo | Implementar consulta autenticada del catálogo de campo desde Control Financiero y Documental según 2.6, con syncToken coherente y sin caché de exhibición. | 8 | Capillo Lema, Mía Valentina | To Do |
| US-02 | Descarga de portafolio para inicio de jornada | S1-02-02 | Descarga y reemplazo local atómico | Integrar descarga tras login y almacenamiento SQLite; cancelar datos parciales ante fallo de red y conservar la última versión estable. | 8 | Rocca Mariaca, Angel Mathias | To Do |
| US-02 | Descarga de portafolio para inicio de jornada | S1-02-03 | Indicadores y prueba de interrupción | Agregar progreso y alerta de descarga incompleta; automatizar pérdida de red para comprobar conservación de la versión estable. | 6 | Caisahuana Osores, Becker Junior | To Do |
| US-14 | Registro de cuenta de usuario web | S1-14-01 | Registro y control de duplicados | Implementar alta de cuenta Inactiva en Identidad y Acceso, unicidad de correo y almacenamiento seguro de contraseña según contratos de 2.6. | 8 | Capillo Lema, Mía Valentina | To Do |
| US-14 | Registro de cuenta de usuario web | S1-14-02 | Verificación de correo | Generar token único y enlace de verificación, conectar envío de correo y activación; comprobar configuración del proveedor sin exponer secretos. | 8 | Nuñez Soto, Andy Arturo | To Do |
| US-14 | Registro de cuenta de usuario web | S1-14-03 | Formulario web y mensajes de cuenta | Integrar registro, aviso de verificación y rechazo de correo duplicado con sugerencia de recuperación, sin implementar historias posteriores de recuperación. | 6 | Perez Encarnacion, Breithner Rodolfo | To Do |
| US-01 | Autenticación segura in situ | S1-01-01 | Autenticación y protección por intentos | Implementar validación online y emisión de token; bloquear 15 minutos al quinto intento inválido y registrar el evento de seguridad. | 8 | Capillo Lema, Mía Valentina | To Do |
| US-01 | Autenticación segura in situ | S1-01-02 | Login móvil y manejo de sesión | Construir vista Material Design, conectar autenticación y manejo seguro del token; mostrar rechazo y bloqueo sin permitir entrada al perfil. | 8 | Rocca Mariaca, Angel Mathias | To Do |
| US-01 | Autenticación segura in situ | S1-01-03 | Pruebas de login y bloqueo | Automatizar credenciales válidas, quinto intento erróneo y expiración del bloqueo usando reloj controlado; verificar registro de seguridad. | 6 | Caisahuana Osores, Becker Junior | To Do |
| US-39 | Endpoint optimizado de polígonos GeoJSON | S1-39-01 | Consulta y representación GeoJSON | Implementar recurso de polígonos según el contrato de descarga de 2.6; preservar lotId y geometría sin trasladar disponibilidad a Catálogo. | 8 | Capillo Lema, Mía Valentina | To Do |
| US-39 | Endpoint optimizado de polígonos GeoJSON | S1-39-02 | Compresión y validación condicional | Configurar GZIP para payloads mayores de 10 KB y ETag con If-None-Match; devolver 304 sin cuerpo cuando la representación no cambie. | 6 | Nuñez Soto, Andy Arturo | To Do |
| US-39 | Endpoint optimizado de polígonos GeoJSON | S1-39-03 | Pruebas de tamaño y ETag | Medir reducción de al menos 60% como criterio por comprobar; probar 304 y cambio de ETag con fixtures geográficos, documentando resultados reales. | 6 | Caisahuana Osores, Becker Junior | To Do |
| US-41 | Implementación de caché en memoria (Caffeine) para catálogo | S1-41-01 | Caché de lecturas de exhibición | Implementar CaffeineCatalogCacheAdapter en Control Financiero y Documental para consultas web con TTL de 5 minutos; excluir descarga de campo y decisiones de bloqueo. | 8 | Capillo Lema, Mía Valentina | To Do |
| US-41 | Implementación de caché en memoria (Caffeine) para catálogo | S1-41-02 | Invalidación posterior al commit | Suscribir publicación y transiciones canónicas del lote para purgar clave de lote y listado de proyecto después del commit, sin implementar ventas de sprints posteriores. | 6 | Nuñez Soto, Andy Arturo | To Do |
| US-41 | Implementación de caché en memoria (Caffeine) para catálogo | S1-41-03 | Pruebas de hit, TTL e invalidación | Verificar ausencia de SQL en hit, TTL y purga con fixtures de eventos; medir el objetivo menor a 50 ms sin declararlo alcanzado de antemano. | 6 | Caisahuana Osores, Becker Junior | To Do |
| US-47 | Spike: Precisión de librerías nativas OCR (Vision API) | S1-47-01 | Preparación del benchmark OCR | Reunir 50 vouchers de muestra autorizados y anonimizados; establecer valores esperados, protocolo de medición y dispositivos de gama media-baja. | 6 | Caisahuana Osores, Becker Junior | To Do |
| US-47 | Spike: Precisión de librerías nativas OCR (Vision API) | S1-47-02 | Prototipo aislado de OCR offline | Prototipar la extracción de montos con librerías nativas como ML Kit Vision; ejecutar sin red, fuera del flujo productivo de US-09. | 8 | Rocca Mariaca, Angel Mathias | To Do |
| US-47 | Spike: Precisión de librerías nativas OCR (Vision API) | S1-47-03 | Evaluación de precisión y memoria | Ejecutar el protocolo sobre 50 muestras y observar RAM, OOM y estabilidad en el hardware definido; registrar si se supera 85%, sin asumir éxito. | 8 | Rocca Mariaca, Angel Mathias | To Do |
| US-47 | Spike: Precisión de librerías nativas OCR (Vision API) | S1-47-04 | Informe de decisión del spike | Documentar mediciones, limitaciones y recomendación para Sprint 2; distinguir datos obtenidos del umbral de aceptación solicitado. | 4 | Caisahuana Osores, Becker Junior | To Do |
| No aplica | Testing transversal del Sprint 1 | S1-TR-01 | Suite automatizada del backend | Implementar Unit Tests de clases y comportamientos de US-51/52/53/14, Integration Tests y Acceptance Tests con Gherkin .feature y Steps; enlazar cada caso a su US. | 8 | Caisahuana Osores, Becker Junior | To Do |
| No aplica | Documentación transversal del Sprint 1 | S1-TR-02 | OpenAPI de los contratos del sprint | Actualizar especificación de altas, publicación, registro, autenticación y consultas de US-01/02/14/15/39/51/52/53 con parámetros, seguridad y respuestas de ejemplo; comprobar herramienta base de Sprint 0. | 8 | Capillo Lema, Mía Valentina | To Do |
| No aplica | Deployment transversal del Sprint 1 | S1-TR-03 | Publicación de Landing Page y portal | Preparar recursos y configuración del hosting para US-P01/14/15, ejecutar despliegue y comprobar URL pública; registrar pasos y capturas solo cuando se realicen. | 6 | Nuñez Soto, Andy Arturo | To Do |
| No aplica | Deployment transversal del Sprint 1 | S1-TR-04 | Publicación de Web Services | Preparar recursos cloud y configuración de API y base de datos; conectar automatización existente, desplegar y verificar acceso por token y documentación pública. | 8 | Nuñez Soto, Andy Arturo | To Do |
| No aplica | Deployment transversal del Sprint 1 | S1-TR-05 | Instalación y revisión en dispositivo | Generar e instalar la app en dispositivo físico; comprobar flujos US-01/02/04 y Material Design, sin confundir el prototipo OCR con funcionalidad productiva. | 6 | Rocca Mariaca, Angel Mathias | To Do |
| No aplica | Documentación transversal del Sprint 1 | S1-TR-06 | Recopilación de evidencia para Review | Recopilar commits verificables, resultados de pruebas, capturas y video de navegación; completar 4.2.1.4-8 únicamente con artefactos efectivamente producidos. | 4 | Caisahuana Osores, Becker Junior | To Do |

**Pendiente de validación en Sprint Planning:** fechas, duración, capacidad del equipo, disponibilidad de cada responsable y aprobación de estimaciones. Esta tabla no acredita implementación ni seguimiento ejecutado. El Capítulo II consultado aún no está integrado en la rama activa; se conserva su referencia textual sin añadir enlaces locales inexistentes.

##### 4.2.1.4. Development Evidence for Sprint Review

En la Sprint Review se resumirán los avances efectivamente implementados de Landing Page, flujos web, Web Services y aplicación móvil que correspondan al Sprint 1. Se relacionará cada avance con su repositorio, rama y commits verificables, diferenciando el prototipo de US-47 del código productivo.

**PENDIENTE:** repositorios de implementación, commits y fechas de los avances reales. La tabla se mantiene sin filas de datos; no se usan commits del informe como evidencia de implementación del producto.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commited on(Date) |
| --- | --- | --- | --- | --- | --- |

##### 4.2.1.5. Testing Suite Evidence for Sprint Review

Se documentará la suite automatizada de Web Services correspondiente al alcance del Sprint 1, distinguiendo Unit Tests, Integration Tests y Acceptance Tests. Los Unit Tests identificarán clases y comportamientos; las pruebas BDD incluirán el código Gherkin de los archivos `.feature`, sus archivos Steps y la explicación de su relación con las User Stories. Los resultados se consignarán solo después de la ejecución comprobada.

**PENDIENTE:** relación real de tests diseñados, código de `.feature` y Steps, resultados de ejecución, ruta del repositorio de Testing y commits. Las siguientes tablas son esquemas sin filas de datos, no pruebas implementadas.

| Test Id | Test Type (Unit / Integration / Acceptance) | User Story Id | Class | Behavior | Test File | .feature File / Gherkin Code | Steps File | Explanation | Execution Result / Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commited on(Date) |
| --- | --- | --- | --- | --- | --- |

##### 4.2.1.6. Execution Evidence for Sprint Review

Esta sección resumirá lo alcanzado una vez que los flujos del Sprint 1 estén implementados y puedan ejecutarse. Se presentarán screenshots de las principales vistas, con explicación del flujo y su User Story, junto con un video que muestre la visualización y navegación logradas. Los escenarios de registro local se distinguirán de la sincronización futura y el spike OCR se identificará como prototipo.

**PENDIENTE:** resumen de ejecución comprobada, capturas de las vistas implementadas y URL del video de navegación. No se insertan imágenes ni enlaces sin disponer de archivos o recursos verificables.

| Product | User Story Id | Implemented View / Flow | Execution Summary | Screenshot | Explanation | Video URL |
| --- | --- | --- | --- | --- | --- | --- |

##### 4.2.1.7. Services Documentation Evidence for Sprint Review

Se resumirán los avances reales en documentación de Web Services del Sprint 1 mediante OpenAPI. Para cada endpoint se registrarán las acciones implementadas, verbo HTTP, sintaxis de llamada, parámetros, ejemplo y explicación del response, y enlace a la documentación desplegada o URL local si aún no hay despliegue. Las capturas deberán explicar la interacción con datos de muestra. Se identificarán el repositorio de Web Services y los commits asociados a la documentación.

**PENDIENTE:** endpoints efectivamente documentados, URLs verificables, capturas de interacción y commits de documentación. Los contratos del Capítulo II orientan la planificación, pero no prueban que exista una API implementada o una documentación publicada. Las tablas no contienen filas de datos.

| Endpoint | Implemented Action | HTTP Verb | Call Syntax | Parameters | Response Example | Response Explanation | Documentation URL |
| --- | --- | --- | --- | --- | --- | --- | --- |

| Endpoint / Action | Sample Data | Interaction Screenshot | Interaction Explanation |
| --- | --- | --- | --- |

| Web Services Repository URL | Commit Id | Documentation Change |
| --- | --- | --- |

##### 4.2.1.8. Software Deployment Evidence for Sprint Review

Se describirán los procesos de Deployment efectivamente realizados durante el Sprint 1 para Landing Page, Web Services y aplicaciones. La evidencia distinguirá creación de cuentas, configuración de recursos cloud, configuración de proyectos para integración o automatización, publicación e instalación en dispositivos. Cada paso se acompañará de capturas y explicación; se registrará el entorno y el resultado verificable sin publicar credenciales ni secretos.

**PENDIENTE:** proveedores y cuentas utilizadas, recursos configurados, automatización comprobada, URLs públicas, instalación en dispositivo físico y capturas de los pasos realizados. Las tareas de despliegue del backlog son planes, no evidencia de publicación. La tabla queda sin filas de datos.

| Product (Landing Page / Web Services / Applications) | Deployment Process / Step | Provider / Environment | Account | Cloud Resource | Project Configuration / Integration / Automation | Public URL / Device | Screenshot | Step Explanation / Verified Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### 4.2.1.9. Team Collaboration Insights during Sprint
