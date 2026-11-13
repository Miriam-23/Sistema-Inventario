import sys
import os
# Agregar la carpeta src a las rutas de búsqueda
ruta_src = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'src')
)

sys.path.insert(0, ruta_src)

import pytest
from unittest.mock import patch
import producto


# Limpiar la lista antes de cada prueba
@pytest.fixture(autouse=True)
def limpiar_productos():
    producto.productos.clear()


# PRUEBA 1: Agregar un producto
def test_agregar_producto():

    with patch("builtins.input", return_value="Laptop"):
        with patch("builtins.print") as mock_print:
            producto.agregar_producto()

    assert "Laptop" in producto.productos

    mock_print.assert_called_with(
        "Producto 'Laptop' agregado correctamente."
    )


# PRUEBA 2: Buscar un producto existente
def test_buscar_producto_existente():

    producto.productos.append("Mouse")

    with patch("builtins.input", return_value="Mouse"):
        with patch("builtins.print") as mock_print:
            producto.buscar_producto()

    mock_print.assert_called_with(
        "El producto 'Mouse' sí existe en la lista."
    )


# PRUEBA 3: Buscar un producto inexistente
def test_buscar_producto_inexistente():

    with patch("builtins.input", return_value="Teclado"):
        with patch("builtins.print") as mock_print:
            producto.buscar_producto()

    mock_print.assert_called_with(
        "El producto 'Teclado' no se encuentra en la lista."
    )


# PRUEBA 4: Mostrar lista vacía
def test_mostrar_productos_vacia():

    with patch("builtins.print") as mock_print:
        producto.mostrar_productos()

    mock_print.assert_any_call("No hay productos registrados.")


# PRUEBA 5: Mostrar productos registrados
def test_mostrar_productos():

    producto.productos.extend(["Laptop", "Mouse", "Teclado"])

    with patch("builtins.print") as mock_print:
        producto.mostrar_productos()

    mock_print.assert_any_call("1. Laptop")
    mock_print.assert_any_call("2. Mouse")
    mock_print.assert_any_call("3. Teclado")


def test_error_intencional_release():
    assert 1 == 2, "Error intencional para comprobar RELEASE"
