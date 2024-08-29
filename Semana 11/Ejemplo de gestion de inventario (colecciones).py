import csv

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario."""
        self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto."""
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca y muestra productos por nombre."""
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        """Guarda el inventario en un archivo CSV."""
        with open(archivo, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Nombre', 'Cantidad', 'Precio'])  # Escribe encabezados
            for producto in self.productos.values():
                writer.writerow([producto.id_producto, producto.nombre, producto.cantidad, producto.precio])

    def cargar_inventario(self, archivo):
        """Carga el inventario desde un archivo CSV."""
        try:
            with open(archivo, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Salta el encabezado
                self.productos = {}
                for row in reader:
                    id_producto, nombre, cantidad, precio = int(row[0]), row[1], int(row[2]), float(row[3])
                    self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    # Carga el inventario desde el archivo al inicio
    inventario.cargar_inventario('inventario.csv')

    # Agregar productos al inventario
    inventario.agregar_producto(Producto(1, "Teclado", 10, 19.99))
    inventario.agregar_producto(Producto(2, "Mouse", 25, 9.99))

    # Mostrar el inventario
    print("Inventario después de agregar productos:")
    inventario.mostrar_inventario()

    # Actualizar un producto
    inventario.actualizar_producto(1, cantidad=15, precio=17.99)

    # Mostrar el inventario después de la actualización
    print("\nInventario después de actualizar un producto:")
    inventario.mostrar_inventario()

    # Buscar un producto
    print("\nBuscar producto con nombre 'teclado':")
    inventario.buscar_producto("teclado")

    # Eliminar un producto
    inventario.eliminar_producto(2)

    # Mostrar el inventario después de eliminar un producto
    print("\nInventario después de eliminar un producto:")
    inventario.mostrar_inventario()

    # Guarda el inventario en el archivo al salir
    inventario.guardar_inventario('inventario.csv')
