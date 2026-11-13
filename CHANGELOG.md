# Historial de cambios – Sistema de Inventario

Este documento registra los cambios, correcciones y resultados de las versiones del Sistema de Inventario desarrollado en Python.

## [v1.0.3] – Liberación corregida

### Corregido
- Se eliminó la prueba fallida agregada intencionalmente para validar el proceso de liberación.
- Se restauró la ejecución satisfactoria de las pruebas automatizadas.

### Validación
- Las pruebas automatizadas finalizaron correctamente.
- GitHub Actions completó el proceso de liberación.
- Se generó y publicó el paquete `sistema-inventario-v1.0.3.zip`.

## [v1.0.2] – Liberación fallida (prueba de control)

### Pruebas
- Se agregó temporalmente una prueba con una condición incorrecta para provocar un fallo controlado.
- GitHub Actions detectó el error durante la ejecución de las pruebas.

### Resultado
- El workflow de liberación terminó con estado FAILED.
- Los pasos de empaquetado y publicación fueron omitidos.
- No se publicó una nueva Release de esta versión.

## [v1.0.1] – Liberación exitosa

### Corregido
- Se corrigió la ejecución automática del menú interactivo para evitar que se iniciara durante la importación del módulo en las pruebas.

### Validación
- Las pruebas automatizadas finalizaron correctamente.
- GitHub Actions ejecutó satisfactoriamente el workflow de liberación.
- Se generó y publicó el paquete `sistema-inventario-v1.0.1.zip`.

## [v1.0.0] – Etiqueta inicial

### Registro
- Se creó la etiqueta inicial `v1.0.0` para identificar una versión del Sistema de Inventario.
- Se inició la configuración del proceso de liberación automatizada mediante GitHub Actions.

### Observaciones
- La creación de esta etiqueta no produjo una publicación de GitHub Release con un paquete ZIP personalizado.