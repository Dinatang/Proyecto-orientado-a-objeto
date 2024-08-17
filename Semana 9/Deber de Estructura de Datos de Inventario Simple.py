# producto.py

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto."""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """Método para representar el producto como una cadena."""
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

    # Getters y setters para cada atributo
    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


# inventario.py

from producto import Producto

class Inventario:
    def __init__(self):
        """Constructor de la clase Inventario. Inicializa una lista vacía de productos."""
        self.productos = []

    def agregar_producto(self, producto):
        """Añadir un nuevo producto asegurándose de que el ID sea único."""
        for prod in self.productos:
            if prod.get_id_producto() == producto.get_id_producto():
                print("Error: Producto con este ID ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        """Eliminar un producto por ID."""
        for prod in self.productos:
            if prod.get_id_producto() == id_producto:
                self.productos.remove(prod)
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualizar la cantidad o el precio de un producto por ID."""
        for prod in self.productos:
            if prod.get_id_producto() == id_producto:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Buscar productos por nombre."""
        encontrados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if encontrados:
            for prod in encontrados:
                print(prod)
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        """Mostrar todos los productos en el inventario."""
        if self.productos:
            for prod in self.productos:
                print(prod)
        else:
            print("El inventario está vacío.")


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '6':
            break
        elif opcion == '1':
            # Solicitar información del producto al usuario
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            # Agregar producto al inventario
            inventario.agregar_producto(producto)
        elif opcion == '2':
            # Solicitar ID del producto a eliminar
            id_producto = input("Ingrese ID del producto a eliminar: ")
            # Eliminar producto del inventario
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            # Solicitar ID del producto a actualizar
            id_producto = input("Ingrese ID del producto a actualizar: ")
            # Solicitar nueva cantidad y precio (dejar vacío si no se desea cambiar)
            cantidad = input("Ingrese nueva cantidad (deje vacío si no quiere cambiarla): ")
            precio = input("Ingrese nuevo precio (deje vacío si no quiere cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            # Actualizar producto en el inventario
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            # Solicitar nombre del producto a buscar
            nombre = input("Ingrese nombre del producto a buscar: ")
            # Buscar y mostrar producto(s) en el inventario
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            # Mostrar todos los productos en el inventario
            inventario.mostrar_inventario()
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
