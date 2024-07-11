class Libro:
    def __init__(self, titulo, autor):
        """
        Constructor de la clase Libro.

        Args:
        - titulo (str): Título del libro.
        - autor (str): Autor del libro.
        """
        self.titulo = titulo  # Inicializa el atributo título con el valor recibido
        self.autor = autor  # Inicializa el atributo autor con el valor recibido
        self.prestado = False  # Inicializa el atributo prestado como False, indicando que el libro no está prestado
        print(f'Se ha creado el libro "{self.titulo}" de {self.autor}')  # Imprime un mensaje al crear el libro

    def __del__(self):
        """
        Destructor de la clase Libro.
        Se ejecuta cuando el objeto libro es destruido y liberado de la memoria.
        """
        if self.prestado:
            print(f'¡ADVERTENCIA! El libro "{self.titulo}" de {self.autor} no ha sido devuelto.')  # Advierte si el libro no ha sido devuelto

    def prestar(self):
        """
        Método para simular el préstamo del libro.
        """
        if not self.prestado:
            self.prestado = True  # Marca el libro como prestado
            print(f'El libro "{self.titulo}" de {self.autor} ha sido prestado.')
        else:
            print(f'El libro "{self.titulo}" de {self.autor} ya está prestado.')

    def devolver(self):
        """
        Método para simular la devolución del libro.
        """
        if self.prestado:
            self.prestado = False  # Marca el libro como no prestado
            print(f'El libro "{self.titulo}" de {self.autor} ha sido devuelto.')
        else:
            print(f'El libro "{self.titulo}" de {self.autor} no estaba prestado.')


class Usuario:
    def __init__(self, nombre):
        """
        Constructor de la clase Usuario.

        Args:
        - nombre (str): Nombre del usuario.
        """
        self.nombre = nombre  # Inicializa el atributo nombre con el valor recibido
        self.libros_prestados = []  # Inicializa la lista de libros prestados del usuario como vacía
        print(f'Se ha creado el usuario {self.nombre}')  # Imprime un mensaje al crear el usuario

    def __del__(self):
        """
        Destructor de la clase Usuario.
        Se ejecuta cuando el objeto usuario es destruido y liberado de la memoria.
        """
        if self.libros_prestados:
            print(f'¡ADVERTENCIA! El usuario {self.nombre} aún tiene libros prestados.')  # Advierte si el usuario tiene libros prestados sin devolver

    def prestar_libro(self, libro):
        """
        Método para que el usuario preste un libro.

        Args:
        - libro (Libro): Objeto de la clase Libro a prestar.
        """
        if libro.prestado:
            print(f'El libro "{libro.titulo}" de {libro.autor} ya está prestado.')
        else:
            libro.prestar()  # Llama al método prestar del libro para prestarlo
            self.libros_prestados.append(libro)  # Agrega el libro a la lista de libros prestados del usuario

    def devolver_libro(self, libro):
        """
        Método para que el usuario devuelva un libro.

        Args:
        - libro (Libro): Objeto de la clase Libro a devolver.
        """
        if libro in self.libros_prestados:
            libro.devolver()  # Llama al método devolver del libro para devolverlo
            self.libros_prestados.remove(libro)  # Remueve el libro de la lista de libros prestados del usuario
        else:
            print(f'El libro "{libro.titulo}" de {libro.autor} no está en la lista de libros prestados.')

    def mostrar_libros_prestados(self):
        """
        Método para mostrar los libros actualmente prestados al usuario.
        """
        if self.libros_prestados:
            print(f'Libros prestados a {self.nombre}:')
            for libro in self.libros_prestados:
                print(f'- "{libro.titulo}" de {libro.autor}')
        else:
            print(f'{self.nombre} no tiene libros prestados.')


# Ejemplo de uso del programa
def ejemplo_uso():
    # Creación de libros y usuarios
    libro1 = Libro('Harry Potter y la piedra filosofal', 'J.K. Rowling')
    libro2 = Libro('Cien años de soledad', 'Gabriel García Márquez')
    usuario1 = Usuario('Juan')
    usuario2 = Usuario('María')

    # Prestamos de libros
    usuario1.prestar_libro(libro1)
    usuario2.prestar_libro(libro2)
    usuario1.prestar_libro(libro2)  # Intento de prestar un libro ya prestado

    # Mostrar libros prestados
    usuario1.mostrar_libros_prestados()
    usuario2.mostrar_libros_prestados()

    # Devolución de libros
    usuario1.devolver_libro(libro1)
    usuario2.devolver_libro(libro2)

    # Eliminación de objetos (uso del destructor)
    del usuario1
    del libro2

    # Al finalizar la función, se destruirán automáticamente los objetos restantes


# Llamada al ejemplo de uso del programa
ejemplo_uso()
