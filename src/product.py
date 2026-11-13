productos = []

def agregar_producto():
    producto = input("Ingresa el nombre del producto: ")

    productos.append(producto)

    print(f"Producto '{producto}' agregado correctamente.")


def buscar_producto():
    producto = input("Ingresa el producto que deseas buscar: ")

    if producto in productos:
        print(f"El producto '{producto}' sí existe en la lista.")
    else:
        print(f"El producto '{producto}' no se encuentra en la lista.")


def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto}")


# Menú principal
while True:
    print("\n===== MENÚ DE PRODUCTOS =====")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Mostrar productos")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        buscar_producto()

    elif opcion == "3":
        mostrar_productos()

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")
