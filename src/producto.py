
productos = []


def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")

    codigo = input("Ingresa el código: ")
    nombre = input("Ingresa el nombre: ")
    precio = float(input("Ingresa el precio: "))
    existencia = int(input("Ingresa la existencia: "))

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "existencia": existencia
    }

    productos.append(producto)

    print(f"Producto '{nombre}' agregado correctamente.")


def buscar_producto(codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for producto in productos:
            mostrar_informacion(producto)


def mostrar_informacion(producto):
    print("\n--- INFORMACIÓN DEL PRODUCTO ---")
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: {producto['precio']}")
    print(f"Existencia: {producto['existencia']}")


def main():
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
            codigo = input("Ingresa el código que deseas buscar: ")
            producto = buscar_producto(codigo)

            if producto:
                mostrar_informacion(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            mostrar_productos()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
