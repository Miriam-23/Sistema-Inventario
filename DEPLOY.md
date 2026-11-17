# Procedimiento de Despliegue — Sistema de Inventario

## 1. Objetivo

Documentar el procedimiento necesario para instalar, configurar, ejecutar y verificar el funcionamiento del Sistema de Inventario desarrollado en Python, utilizando el paquete publicado en GitHub Releases.

## 2. Información del sistema

| Elemento | Descripción |
|---|---|
| Proyecto | Sistema de Inventario |
| Lenguaje | Python |
| Versión liberada | v1.0.3 |
| Tipo de aplicación | Aplicación de consola |
| Entorno de despliegue inicial | Windows |
| Repositorio | GitHub |
| Paquete | sistema-inventario-v1.0.3.zip |
| Archivo principal | main.py |

## 3. Requisitos del entorno

Para ejecutar el Sistema de Inventario se requiere:

- Una computadora con Windows.
- Python instalado y disponible desde la terminal.
- PowerShell, CMD o una terminal equivalente.
- El paquete ZIP de la versión liberada.
- Las dependencias que requiera el proyecto.

Para verificar Python:

`python --version`

Para comprobar pip:

`python -m pip --version`

## 4. Descargar la versión liberada

1. Ingresar al repositorio del Sistema de Inventario en GitHub.
2. Acceder a la sección Releases.
3. Localizar la versión v1.0.3.
4. Descargar el archivo `sistema-inventario-v1.0.3.zip`.
5. Crear una carpeta denominada `despliegue-inventario`.
6. Guardar el archivo ZIP dentro de dicha carpeta.

## 5. Extraer los archivos

1. Localizar el archivo ZIP descargado.
2. Seleccionar la opción Extraer todo.
3. Extraer el contenido en una carpeta identificada con la versión.
4. Verificar que los archivos del sistema se encuentren disponibles.

Los archivos principales del proyecto incluyen:

- `main.py`: archivo principal de ejecución.
- `src/producto.py`: módulo del sistema de inventario.
- `requirements.txt`: archivo de dependencias.
- `README.md`: información del proyecto.

## 6. Configuración del entorno

Abrir una terminal y acceder a la carpeta donde se extrajo el proyecto.

Comprobar que Python esté instalado.

Si el proyecto requiere dependencias externas y contiene `requirements.txt`, ejecutar:

`python -m pip install -r requirements.txt`

Si no se requieren bibliotecas externas, se puede continuar directamente con la ejecución.

## 7. Ejecutar el Sistema de Inventario

Desde la carpeta que contiene `main.py`, ejecutar:

`python main.py`

El sistema deberá iniciar y mostrar su interfaz de consola.

## 8. Verificar el funcionamiento

Para comprobar que el despliegue fue exitoso:

1. Ejecutar el programa.
2. Verificar que el menú principal aparezca correctamente.
3. Registrar un producto de prueba.
4. Consultar los productos registrados.
5. Comprobar que la información se muestre correctamente.
6. Verificar que no se presenten errores durante la ejecución.

## 9. Posibles problemas y soluciones

| Problema | Posible solución |
|---|---|
| Python no se reconoce | Verificar su instalación y configuración en PATH |
| No se encuentra main.py | Comprobar que la terminal esté ubicada en la carpeta correcta |
| Falta un módulo | Instalar las dependencias necesarias |
| No se encuentra requirements.txt | Comprobar su existencia en el paquete extraído |
| El programa no inicia | Revisar los mensajes de error y los archivos del sistema |
| El paquete está incompleto | Descargar nuevamente el ZIP desde GitHub Releases |

## 10. Resultado del despliegue manual

La versión v1.0.3 del Sistema de Inventario fue descargada y extraída correctamente desde GitHub Releases.

Se comprobó la disponibilidad de Python y se ejecutó el archivo principal `main.py` desde la terminal.

El programa inició correctamente en el entorno local, confirmando que la versión liberada puede ejecutarse fuera del entorno original de desarrollo.

## 11. Conclusión

El despliegue manual permitió verificar que la versión v1.0.3 del Sistema de Inventario puede instalarse y ejecutarse en una computadora de destino.

La documentación generada establece un procedimiento reproducible para futuras instalaciones y constituye la base para automatizar el despliegue mediante GitHub Actions.