# Capturas de Swagger — Sprint 1

Guardar las imágenes PNG en esta carpeta con los nombres de la tabla. URL indicada por Becker para las nuevas capturas: `https://inmonode-backend.onrender.com/swagger-ui/index.html`. Registrar Render como entorno y el commit desplegado si se conoce. Las evidencias locales anteriores no se trasladan automáticamente a Render. Los espacios correspondientes se encuentran en la sección 4.2.1.7 de Chapter IV, identificados por su título y nombre de archivo.

| Archivo | Espacio del informe | Qué capturar |
| --- | --- | --- |
| swagger-overview.png | Documentación general (sección 4.2.1.7) | Abrir Swagger UI en la URL de Render indicada arriba. Mostrar la URL y los grupos Projects, Real estate catalog, Field sync y Health disponibles. |
| swagger-project-create.png | Alta de proyecto (sección 4.2.1.7) | POST /api/v1/catalog/projects; rol CATALOG_ADMIN. Usar el ejemplo E y guardar el projectId devuelto. Mostrar request con nombre, ubicación, etapas y reglas; respuesta esperada 201 con id y DRAFT. |
| swagger-lot-create.png | Alta de lote (sección 4.2.1.7) | POST /api/v1/catalog/projects/{projectId}/lots; rol CATALOG_ADMIN. Usar el ejemplo F y una etapa del proyecto creado. Guardar el lotId devuelto. Mostrar projectId, código, dimensiones, área, precio y polígono; respuesta esperada 201 con DRAFT. |
| swagger-project-publish.png | Publicación de proyecto (sección 4.2.1.7) | PUT /api/v1/catalog/projects/{projectId}/publish; rol CATALOG_ADMIN. El proyecto debe tener el lote registrado. Mostrar projectId y respuesta esperada 200 con PUBLISHED. No requiere body. |
| swagger-lot-publish.png | Publicación de lote (sección 4.2.1.7) | PUT /api/v1/catalog/lots/{lotId}/publish; rol CATALOG_ADMIN. Usar un lote DRAFT cuyo proyecto ya esté publicado. Mostrar lotId y respuesta esperada 200 con AVAILABLE. No usar un lote BLOCKED para demostrar esta transición. |
| swagger-projects.png | Catálogo público (sección 4.2.1.7) | GET /api/v1/projects. Mostrar la URL y respuesta 200: id, nombre, priceRange, totalLots, availabilityPercentage y soldOut. Usar los datos realmente devueltos. |
| swagger-project-detail.png | Detalle de proyecto (sección 4.2.1.7) | GET /api/v1/projects/{projectId}; usar un proyecto publicado. Mostrar projectId y respuesta 200: nombre, ubicación, estado, etapas y reglas. |
| swagger-lots.png | Geometría y datos del lote (sección 4.2.1.7) | GET /api/v1/projects/{projectId}/lots. Mostrar projectId y respuesta 200 con FeatureCollection, Polygon, coordinates, código, área, precio y estado del lote. |
| health.png | Disponibilidad del entorno capturado (sección 4.2.1.7) | GET /health. Puede capturarse en Swagger si está listado o como JSON en el navegador. Mostrar URL, respuesta real y servicios. Resultado esperado con base disponible: 200 y UP; registrar Render o local según la URL capturada. |
| swagger-project-validation.png | Rechazo de proyecto incompleto (sección 4.2.1.7) | POST /api/v1/catalog/projects; rol CATALOG_ADMIN. Quitar un campo requerido del ejemplo E, por ejemplo stages. Mostrar el campo ausente en el request y respuesta esperada 400 con explicación de validación. |
| swagger-lot-validation.png | Rechazo de polígono inválido (sección 4.2.1.7) | POST /api/v1/catalog/projects/{projectId}/lots; rol CATALOG_ADMIN. Usar geometría inválida, por ejemplo un polígono con aristas cruzadas. Mostrar el polígono enviado y respuesta esperada 400 con su error. Diferenciar este caso de un código duplicado 409. |
| swagger-publication-rejected.png | Rechazo de publicación fuera de condiciones (sección 4.2.1.7) | PUT /api/v1/catalog/lots/{lotId}/publish; rol CATALOG_ADMIN. Usar un lote DRAFT de otro proyecto que aún esté DRAFT. Mostrar lotId y rechazo esperado 422 por proyecto no publicado. Después registrar la transición válida en la captura de publicación de lote. |
| swagger-catalog-forbidden.png | Autorización administrativa (sección 4.2.1.7) | Consultar GET /api/v1/catalog/projects/{projectId}/lots con una cuenta de prueba BUYER. Mostrar endpoint y respuesta esperada 403. Describir el rol usado sin incluir el JWT ni el header Authorization. |
| swagger-field-sync.png | Recepción de prospecto en servidor (sección 4.2.1.7) | POST /api/v1/field-sync; rol FIELD_AGENT. Usar el ejemplo C con datos de prueba y reservations=[]. Mostrar el prospecto enviado y respuesta esperada 201 con prospectsSynced. Acredita recepción servidor; el registro offline Android requiere evidencia aparte. |
| swagger-portfolio.png | Portfolio de soporte (sección 4.2.1.7) | GET /api/v1/field-sync/portfolio; rol FIELD_AGENT. Mostrar respuesta 200 y ETag. Es dependencia técnica de US-02, fuera del cierre del Sprint 1. |
| swagger-portfolio-not-modified.png | Respuesta condicional de portfolio (sección 4.2.1.7) | Repetir GET /api/v1/field-sync/portfolio con el If-None-Match devuelto antes. Mostrar If-None-Match y respuesta esperada 304 sin body; no incluir Authorization. |

## Cómo incorporarlas

1. Guardar la captura con su nombre exacto en esta carpeta. No basta pegarla en el chat para que forme parte del repositorio.
2. En el espacio correspondiente de la sección 4.2.1.7 de Chapter IV, retirar únicamente las líneas `<!--` y `-->` que rodean la línea `![...](evidence/sprint-1/swagger/archivo.png)`. El comentario de instrucciones puede conservarse.
3. Completar fecha/hora, entorno, revisión/build si se conoce y resultado realmente observado. Cambiar el estado de la fila correspondiente solo después de incorporar y revisar la imagen.
4. Si se necesitan dos imágenes, usar `-request.png` y `-response.png`, actualizar la línea preparada y añadir una segunda línea debajo.

Para el flujo válido: crear proyecto, guardar su ID, crear lote, guardar su ID, publicar proyecto y publicar lote. Los ejemplos E/F y C están en 4.2.1.7. Usar otra alta de prueba para el rechazo de publicación sobre proyecto Borrador.

Mostrar endpoint, parámetros/body, código HTTP y respuesta; ocultar JWT y Authorization. Los ejemplos y resultados esperados no sustituyen la ejecución real. Las dos capturas de portfolio son complementarias, fuera del cierre de las historias del Sprint 1.
## Cómo tomar las capturas para el PDF

1. Maximizar el navegador y mantener un tamaño de texto legible (preferentemente zoom 100 %).
2. Captura general: mostrar la URL, título de Swagger y grupos de endpoints. Guardar como swagger-overview.png.
3. Captura por operación: abrir el endpoint, pulsar Try it out, completar parámetros/body y pulsar Execute. Para rutas protegidas, autorizar con la cuenta de prueba del rol correspondiente.
4. Mostrar método/ruta, petición y Server response con el código HTTP y Response body reales. No confundir Server response con Responses, Example Value o Schema.
5. Usar Win + Shift + S para recortar el área pertinente. Si petición y respuesta no caben, guardar dos imágenes con sufijos -request.png y -response.png. Evitar una captura de página completa cuyo texto se vuelva ilegible en una hoja PDF.
6. Ocultar JWT, Authorization y credenciales; los datos de los ejemplos deben ser de prueba. Mantener visibles la URL y los datos necesarios para interpretar el resultado.

Orden recomendado: captura general; catálogo público, detalle y lotes; flujo de alta/publicación; errores y autorización; recepción de prospectos y health. Los nombres exactos están en la tabla anterior. Los resultados esperados se contrastan con la ejecución real del entorno Render.