# Clase base: Libro
class Libro:
    def __init__(self, titulo, autor, paginas):
        # Atributos privados (encapsulación)
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    # Método para obtener el título
    def obtener_titulo(self):
        return self.__titulo

    # Método para establecer el título
    def establecer_titulo(self, titulo):
        self.__titulo = titulo

    # Método para mostrar la información del libro
    def mostrar_informacion(self):
        print(f"Título: {self.__titulo}, Autor: {self.__autor}, Páginas: {self.__paginas}")

    # Método para obtener el número de páginas
    def obtener_paginas(self):
        return self.__paginas


# Clase derivada: LibroElectronico
class LibroElectronico(Libro):
    def __init__(self, titulo, autor, paginas, tamano_archivo):
        # Llamada al constructor de la clase base
        super().__init__(titulo, autor, paginas)
        self.__tamano_archivo = tamano_archivo

    # Método para mostrar la información del libro electrónico (polimorfismo)
    def mostrar_informacion(self):
        # Llamada al método de la clase base
        super().mostrar_informacion()
        print(f"Tamaño del archivo: {self.__tamano_archivo} MB")


# Función principal para demostrar la funcionalidad del programa
def main():
    # Creación de instancias de Libro y LibroElectronico
    libro1 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", 180)
    libro_electronico1 = LibroElectronico("Fortaleza Digital", "Dan Brown", 356, 2.5)

    # Demostración de la encapsulación
    print("Título original del libro:", libro1.obtener_titulo())
    libro1.establecer_titulo("El Gran Gatsby - Edición Revisada")
    print("Título actualizado del libro:", libro1.obtener_titulo())

    # Mostrar información del libro
    print("\nInformación del Libro:")
    libro1.mostrar_informacion()

    # Mostrar información del libro electrónico (polimorfismo)
    print("\nInformación del Libro Electrónico:")
    libro_electronico1.mostrar_informacion()


if __name__ == "__main__":
    main()
