# Sprint 1: evidencias pendientes

El Sprint 1 está alineado con feature/chapter-02: US-51, US-52, US-53, US-P01, US-15 y US-04; seis historias y 21 Story Points. Chapter IV contiene 23 tareas con 122 horas estimadas. US-05 y US-06 permanecen en Sprint 2.

## Evidencia del tablero

**Screenshot del Board:** captura incorporada por Becker — `../assets/sprint1.png`, verificada contra el tablero el 2026-10-09.

**Tablero:** NovaCorp — InmoNode Sprint 1 — `https://trello.com/b/zF1oDRW8/novacorp-inmonode-sprint-1`.

El tablero se cargó y verificó el 2026-10-09: objetivo/Definition of Done, seis historias con checklists y 23 tareas; 12 en To Do y 11 en To Review. Las 30 tarjetas incluyen descripciones. Becker figura como miembro de sus seis tareas principales; los demás responsables están consignados como propuestos. Las tarjetas anteriores se conservan en una lista de referencia fuera del Sprint. El registro del tablero — `evidence/sprint-1/backlog-2026-10-09.json` contiene los enlaces verificados. La captura ya está incorporada y coincide con los conteos. El acceso del evaluador al enlace del tablero aún debe comprobarse: la visibilidad observada es del Espacio de trabajo. La imagen acredita el estado actual, no un historial de avances ni la aceptación de tareas.

## Qué falta para cerrar la parte de Becker

El backend y sus registros técnicos ya permiten sustentar parte de 4.2.1.4–4.2.1.7. La matriz LACX y la captura del backlog están incorporadas. Los siguientes pendientes se contrastaron con las secciones Sprint Backlog, Testing Suite, Execution, Services Documentation, Deployment y Team Collaboration del enunciado.

| Pendiente propio o de coordinación de Becker | Evidencia para cerrar |
| --- | --- |
| Ejecución y documentación backend, 4.2.1.6–4.2.1.7 | Capturas reales de Swagger: alta DRAFT de proyecto/lote, publicación AVAILABLE, rechazos y autorización; catálogo/detalle, GeoJSON, recepción de prospectos y health. Conservar request, código y body. Identificar la versión ejecutada. |
| Pruebas backend, 4.2.1.5, con Mía | Captura de resultados de las ejecuciones registradas; ejecutar la suite completa con Docker operativo y resolver fallos. Completar los .feature, Steps y runner de BDD aplicables a servicios del Sprint. Los escenarios del informe son especificaciones propuestas, no ejecución automatizada. |
| Colaboración, 4.2.1.9 | Capturas de Contributors/actividad y Network/PR con período visible, enlazadas a los aportes y revisiones reales. Los conteos Git disponibles no sustituyen estos analíticos. |
| Aceptación del trabajo | Registrar revisión del equipo y evidencia de cumplimiento antes de cerrar tareas/historias; las tareas siguen To Do/To Review. Comprobar acceso del evaluador al tablero. |

## Información de otros productos que necesita el informe

| Producto / responsable según LACX | Información necesaria |
| --- | --- |
| Landing Page / Breithner | El repositorio ya figura en 4.1.2 como InmoNode-Landing-Page. Confirmar que es el vigente y aportar acceso al código (preferentemente carpeta local o URL GitHub accesible), rama/revisión usada y URL publicada. Permite revisar commits, propósito/pitch, CTA, contacto/redes, adaptación móvil, navegación y despliegue. |
| Frontend web / Breithner y equipo | Repositorio o carpeta, rama/revisión y URL o instrucciones de ejecución. Necesario para formularios de US-51/52/53 y catálogo US-15; la landing por sí sola no prueba estos flujos. |
| Android / Angel | Repositorio o carpeta, rama/revisión y APK/build. Añadir modelo/versión del dispositivo y evidencia física de US-04 en modo avión: guardado, reapertura, operación pendiente y rechazo sin documento. |
| Deployment / Andy | URL pública de la landing y datos del despliegue realmente realizado: proveedor, build/commit, configuración y logs. Para backend puede documentarse la URL local en Sprints previos a su despliegue, según el enunciado; un archivo Docker/CI no certifica ejecución remota. |
| Sprint Review / equipo | Enlace del video de ejecución/navegación y una captura del video. Mostrar los flujos alcanzados y señalar lo pendiente. Registrar qué revisión/build se demuestra. |

Los pendientes de frontend, Android y despliegue son dependencias del equipo para completar las tablas del informe; no se atribuyen a Becker como implementación individual.
## Capturas de Swagger listas para incorporar

Guardar los PNG en docs/evidence/sprint-1/swagger/. La guía de nombres y contenido — `evidence/sprint-1/swagger/README.md` identifica cada espacio preparado de 4.2.1.7. Las líneas de imagen están comentadas hasta que exista el archivo, para evitar imágenes rotas y no presentar evidencia inexistente.

## Capturas, video y enlaces de los productos

| Apartado | Evidencia pendiente | Contenido |
| --- | --- | --- |
| 4.2.1.4 | Repositorios y commits de clientes | Landing Page, frontend web/back-office y Android; relacionar cada cambio con su historia. |
| 4.2.1.5 | Captura de resultados | Comando, fecha y conteos; 56 pruebas originales más siete de catálogo, sin fallos, errores u omisiones. |
| 4.2.1.6 | Alta de proyecto | Formulario de nombre, ubicación y etapas; resultado Borrador y rechazo de campo obligatorio ausente. |
| 4.2.1.6 | Alta y publicación de lote | Ficha técnica, polígono, estado No publicado; rechazo de geometría; publicación y disponibilidad. |
| 4.2.1.6 | Landing Page y catálogo | Propuesta de valor, CTA, tarjetas, precios/disponibilidad y Sold Out. Un lote BLOCKED no equivale a vendido. |
| 4.2.1.6 | Android US-04 | Modo avión, guardado/reapertura del prospecto, operación pendiente y rechazo sin documento. |
| 4.2.1.6 | Video de Sprint Review | Mostrar los seis flujos seleccionados, versión y dispositivo; enlace accesible al evaluador y captura del video. |
| 4.2.1.7 | Swagger administrativo | Requests y responses de creación de proyecto/lote, publicación, errores y autorización. |
| 4.2.1.7 | Swagger público y soporte | Catálogo, detalle, geometría, health y recepción de prospectos. |
| 4.2.1.8 | Despliegue real | Proveedor, configuración, build, logs, URL, commit y fecha; instalación Android en dispositivo físico. |
| 4.2.1.9 | GitHub Insights y PR | Contributors, Network y revisiones de los productos; período visible e interpretación de los aportes. |

Las imágenes pueden guardarse en docs/evidence/sprint-1/ e insertarse en Chapter-04.md después de existir. El servidor de validación comprobado es `http://localhost:8081/api-docs,` si continúa activo. Para operaciones administrativas, usar CATALOG_ADMIN de prueba y ocultar el token; para recepción de prospectos, FIELD_AGENT. Los ejemplos del capítulo son datos de prueba y los requests administrativos se identifican como ilustrativos.

## Implementación e infraestructura pendientes

- BDD: incorporar .feature, Steps y runner para las seis historias y conservar resultados de ejecución. Los escenarios escritos no son pruebas automatizadas ejecutadas.
- Suite completa: habilitar Docker Engine y ejecutar Maven verify con Testcontainers PostgreSQL/S3. Los 63 casos comprobados no sustituyen esa suite.
- Clientes: verificar los formularios administrativos, Landing Page/catálogo y persistencia offline de US-04 en sus repositorios; implementar los entregables que falten.
- Despliegue: publicación e instalación reales; configuración versionada no certifica un despliegue público.
- Colaboración: acreditar implementación y revisión por integrante según tareas y productos.

## Evidencia disponible

- 56 pruebas originales — `evidence/sprint-1/tests-2026-10-09.json`: 53 de dominio/controladores y tres de integración local; ObjectStorage simulado explícitamente en integración.
- Siete pruebas adicionales de catálogo — `evidence/sprint-1/tests-catalog-2026-10-09.json`: etapas, registro/publicación del lote, validación HTTP y autorización; dependencias simuladas.
- Registro HTTP/OpenAPI — `evidence/sprint-1/http-openapi-2026-10-09.json`: catálogo, detalle, GeoJSON y health con 200; datos de prueba y marca temporal.
- Colaboración Git — `evidence/sprint-1/collaboration-2026-10-09.json`: autores y revisiones auditadas, excluyendo merges.

Los cambios del informe son locales. No se publicó software ni se hizo commit/push.

La URL de Swagger indicada por Becker para las nuevas capturas es `https://inmonode-backend.onrender.com/swagger-ui/index.html`. Usar una imagen general y evidencias por operación con Server response real. Registrar Render, fecha y commit/build si se conoce; acceso y versión desplegada pendientes de comprobar. Las instrucciones detalladas están en docs/evidence/sprint-1/swagger/README.md.

## Revisión de capturas incorporadas (2026-10-09)

Se incorporaron las 16 imágenes de assets en 4.2.1.7. Quince muestran contratos o ejemplos; swagger-portfolio-not-modified.png muestra una respuesta ejecutada 401 UNAUTHORIZED en Render, no 304. swagger-project-detail.png muestra el listado GET /api/v1/projects, no el detalle. Las capturas de validación, publicación rechazada y autorización muestran documentación, sin rechazos reales. Las imágenes ya son visibles en el informe; siguen pendientes las ejecuciones con Try it out, Execute y Server response. Reemplazar o complementar las capturas para demostrar 201/200 y los errores 400/422/403; capturar el endpoint de detalle correcto y health UP real.
