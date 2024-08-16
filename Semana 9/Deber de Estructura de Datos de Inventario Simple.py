class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa un producto con su ID, nombre, cantidad y precio
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Devuelve una representación en cadena del producto
        return f"{self.id_producto}: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"


class Inventario:
    def __init__(self):
        # Inicializa un inventario vacío usando una lista
        self.productos = []

    def agregar_producto(self, producto):
        # Agrega un producto al inventario si no está ya presente
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: Producto ya existe.")
                return
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado al inventario.")

    def eliminar_producto(self, id_producto):
        # Elimina un producto del inventario usando su ID
        for p in self.productos:
            if p.id_producto == id_producto:
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado del inventario.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualiza la cantidad y/o precio de un producto en el inventario usando su ID
        for p in self.productos:
            if p.id_producto == id_producto:
                if cantidad is not None:
                    p.cantidad = cantidad
                if precio is not None:
                    p.precio = precio
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Busca productos en el inventario cuyo nombre contiene la cadena proporcionada
        encontrado = False
        for p in self.productos:
            if nombre.lower() in p.nombre.lower():
                print(p)
                encontrado = True
        if not encontrado:
            print("Producto no encontrado.")

    def listar_productos_bajo_stock(self, nivel):
        # Lista los productos cuya cantidad está por debajo del nivel proporcionado
        bajo_stock = [p for p in self.productos if p.cantidad < nivel]
        if bajo_stock:
            print("Productos con bajo stock:")
            for p in bajo_stock:
                print(p)
        else:
            print("No hay productos con bajo stock.")

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)


# Interfaz de usuario en la consola
def menu():
    # Inicializa un inventario vacío
    inventario = Inventario()

    while True:
        # Muestra el menú de opciones al usuario
        print(
            "\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Listar Productos con Bajo Stock\n6. Mostrar Inventario\n7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '7':
            # Salir del menú
            break
        elif opcion == '1':
            # Agregar producto
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Eliminar producto
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Actualizar producto
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            # Buscar producto
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            # Listar productos con bajo stock
            nivel = int(input("Nivel de stock: "))
            inventario.listar_productos_bajo_stock(nivel)
        elif opcion == '6':
            # Mostrar inventario
            inventario.mostrar_inventario()


# Ejecuta el menú si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()
