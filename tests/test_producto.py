import sys
import os
# Agregar la carpeta src a las rutas de búsqueda
ruta_src = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)

sys.path.insert(0, ruta_src)

import pytest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO
import producto


# Limpiar la lista antes de cada prueba
@pytest.fixture(autouse=True)
def limpiar_productos():
    producto.productos.clear()


# Función auxiliar para crear un producto
def crear_teclado():
    datos = ["P001", "Teclado", "350", "10"]

    with patch("builtins.input", side_effect=datos):
        producto.agregar_producto()


# CP01: Crear un producto
def test_CP01_crear_producto():
    crear_teclado()

    assert len(producto.productos) == 1
    assert producto.productos[0]["codigo"] == "P001"
    assert producto.productos[0]["nombre"] == "Teclado"
    assert producto.productos[0]["precio"] == 350
    assert producto.productos[0]["existencia"] == 10


# CP02: Mostrar el código
def test_CP02_mostrar_codigo():
    crear_teclado()

    resultado = producto.buscar_producto("P001")

    assert resultado["codigo"] == "P001"


# CP03: Mostrar el nombre
def test_CP03_mostrar_nombre():
    crear_teclado()

    resultado = producto.buscar_producto("P001")

    assert resultado["nombre"] == "Teclado"


# CP04: Mostrar el precio
def test_CP04_mostrar_precio():
    crear_teclado()

    resultado = producto.buscar_producto("P001")

    assert resultado["precio"] == 350


# CP05: Mostrar la existencia
def test_CP05_mostrar_existencia():
    crear_teclado()

    resultado = producto.buscar_producto("P001")

    assert resultado["existencia"] == 10


# CP06: Mostrar información completa
def test_CP06_mostrar_informacion_completa():
    crear_teclado()

    resultado = producto.buscar_producto("P001")

    salida = StringIO()

    with redirect_stdout(salida):
        producto.mostrar_informacion(resultado)

    informacion = salida.getvalue()

    assert "Código: P001" in informacion
    assert "Nombre: Teclado" in informacion
    assert "Precio: 350.0" in informacion
    assert "Existencia: 10" in informacion


# CP07: Crear un segundo producto
def test_CP07_crear_segundo_producto():
    crear_teclado()

    datos = ["P002", "Mouse", "180", "5"]

    with patch("builtins.input", side_effect=datos):
        producto.agregar_producto()

    assert len(producto.productos) == 2

    primero = producto.buscar_producto("P001")
    segundo = producto.buscar_producto("P002")

    assert primero["nombre"] == "Teclado"
    assert primero["precio"] == 350
    assert primero["existencia"] == 10

    assert segundo["nombre"] == "Mouse"
    assert segundo["precio"] == 180
    assert segundo["existencia"] == 5
