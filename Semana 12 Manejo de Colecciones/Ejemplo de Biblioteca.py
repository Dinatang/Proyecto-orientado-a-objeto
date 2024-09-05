# Clase Libro: Representa un libro con atributos como título, autor, categoría y ISBN.
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Atributos del libro, como título, autor, categoría y ISBN.
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        # Representación en cadena del libro para facilitar la lectura del objeto.
        return f"'{self.titulo}' by {self.autor} (Category: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario: Representa un usuario con atributos como nombre, ID y libros prestados.
class Usuario:
    def __init__(self, nombre, id_usuario):
        # Atributos del usuario, como nombre, ID único y lista de libros prestados.
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        # Método para añadir un libro a la lista de libros prestados por el usuario.
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        # Método para eliminar un libro de la lista de libros prestados por el usuario.
        self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        # Método para obtener la lista de libros actualmente prestados por el usuario.
        return self.libros_prestados

    def __str__(self):
        # Representación en cadena del usuario y los libros que ha prestado.
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {[libro.titulo for libro in self.libros_prestados]}"


# Clase Biblioteca: Gestiona los libros, usuarios y los préstamos de la biblioteca.
class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar libros, con ISBN como clave y el objeto Libro como valor.
        self.libros = {}
        # Diccionario para almacenar usuarios, con ID único como clave y el objeto Usuario como valor.
        self.usuarios = {}
        # Conjunto para asegurar que los IDs de los usuarios sean únicos.
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        # Método para añadir un libro a la biblioteca.
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        # Método para eliminar un libro de la biblioteca.
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn} en la biblioteca.")

    def registrar_usuario(self, usuario):
        # Método para registrar un nuevo usuario en la biblioteca.
        if usuario.id_usuario in self.ids_usuarios:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado con éxito.")

    def dar_baja_usuario(self, id_usuario):
        # Método para dar de baja a un usuario existente en la biblioteca.
        if id_usuario in self.ids_usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        # Método para prestar un libro a un usuario.
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros.pop(isbn)  # Elimina el libro del diccionario de libros disponibles.
            usuario.prestar_libro(libro)  # Añade el libro a la lista de libros prestados del usuario.
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print(f"No se pudo completar el préstamo. Verifica el ID de usuario y el ISBN.")

    def devolver_libro(self, id_usuario, isbn):
        # Método para devolver un libro prestado a la biblioteca.
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            # Encuentra el libro en la lista de libros prestados del usuario.
            libro = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
            if libro:
                usuario.devolver_libro(libro)  # Elimina el libro de la lista de libros prestados del usuario.
                self.libros[isbn] = libro  # Añade el libro de vuelta al diccionario de libros disponibles.
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} no tiene el libro con ISBN {isbn}.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        # Método para buscar libros en la biblioteca por título, autor o categoría.
        resultados = [libro for libro in self.libros.values()
                      if (titulo and titulo.lower() in libro.titulo.lower()) or
                         (autor and autor.lower() in libro.autor.lower()) or
                         (categoria and categoria.lower() == libro.categoria.lower())]
        return resultados

    def listar_libros_prestados(self, id_usuario):
        # Método para listar los libros prestados por un usuario.
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.listar_libros_prestados()
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")


# Ejemplo de uso del sistema de gestión de biblioteca digital

# Creación de una instancia de la biblioteca
mi_biblioteca = Biblioteca()

# Añadir libros a la biblioteca
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Ficción", "1234567890")
libro2 = Libro("1984", "George Orwell", "Ficción", "0987654321")
mi_biblioteca.añadir_libro(libro1)
mi_biblioteca.añadir_libro(libro2)

# Registrar un usuario
usuario1 = Usuario("Dina", "001")
mi_biblioteca.registrar_usuario(usuario1)

# Prestar un libro a un usuario
mi_biblioteca.prestar_libro("001", "1234567890")

# Devolver un libro
mi_biblioteca.devolver_libro("001", "1234567890")

# Buscar un libro por título
resultados_busqueda = mi_biblioteca.buscar_libro(titulo="1984")
print("Resultados de búsqueda:")
for libro in resultados_busqueda:
    print(libro)

# Listar libros prestados por un usuario
print(f"\nLibros prestados por {usuario1.nombre}:")
libros_prestados = mi_biblioteca.listar_libros_prestados("001")
for libro in libros_prestados:
    print(libro)
