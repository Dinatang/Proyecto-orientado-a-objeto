import csv


# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Inicializa un producto con su ID, nombre, cantidad y precio."""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """Devuelve una representación en forma de cadena del producto."""
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# Clase que maneja el inventario de productos
class Inventario:
    def __init__(self):
        """Inicializa el inventario como un diccionario vacío."""
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
        """Actualiza la cantidad o el precio de un producto en el inventario."""
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            # Si se proporciona una nueva cantidad, actualiza el producto
            if cantidad is not None:
                producto.cantidad = cantidad
            # Si se proporciona un nuevo precio, actualiza el producto
            if precio is not None:
                producto.precio = precio
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca y muestra productos por nombre en el inventario."""
        # Busca productos cuyo nombre coincida parcial o completamente con la búsqueda
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
            writer.writerow(['ID', 'Nombre', 'Cantidad', 'Precio'])  # Escribe los encabezados
            # Escribe los detalles de cada producto en el archivo CSV
            for producto in self.productos.values():
                writer.writerow([producto.id_producto, producto.nombre, producto.cantidad, producto.precio])

    def cargar_inventario(self, archivo):
        """Carga el inventario desde un archivo CSV."""
        try:
            with open(archivo, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Salta el encabezado
                self.productos = {}
                # Lee cada línea del archivo CSV y crea productos en el inventario
                for row in reader:
                    id_producto, nombre, cantidad, precio = int(row[0]), row[1], int(row[2]), float(row[3])
                    self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")


# Función que muestra el menú de opciones para el usuario
def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")


# Ejemplo de uso interactivo del programa
if __name__ == "__main__":
    inventario = Inventario()  # Se crea una instancia de la clase Inventario

    while True:  # Ciclo infinito para mostrar el menú hasta que el usuario decida salir
        mostrar_menu()  # Muestra el menú de opciones
        opcion = input("Selecciona una opción: ")  # Solicita la opción al usuario

        if opcion == '1':  # Opción para agregar un producto
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            print("Producto agregado con éxito.")

        elif opcion == '2':  # Opción para eliminar un producto
            id_producto = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':  # Opción para actualizar un producto
            id_producto = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar en blanco si no se actualiza): ")
            precio = input("Nuevo precio (dejar en blanco si no se actualiza): ")
            # Si se ingresa un valor, se convierte al tipo correspondiente (int o float)
            inventario.actualizar_producto(id_producto, cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)

        elif opcion == '4':  # Opción para buscar un producto por nombre
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':  # Opción para mostrar todo el inventario
            inventario.mostrar_inventario()

        elif opcion == '6':  # Opción para guardar el inventario en un archivo CSV
            archivo = input("Nombre del archivo para guardar (ej. inventario.csv): ")
            inventario.guardar_inventario(archivo)
            print("Inventario guardado con éxito.")

        elif opcion == '7':  # Opción para cargar el inventario desde un archivo CSV
            archivo = input("Nombre del archivo para cargar (ej. inventario.csv): ")
            inventario.cargar_inventario(archivo)
            print("Inventario cargado con éxito.")

        elif opcion == '8':  # Opción para salir del programa
            print("Saliendo del programa...")
            break

        else:  # Mensaje de error si se ingresa una opción no válida
            print("Opción no válida. Intenta de nuevo.")
