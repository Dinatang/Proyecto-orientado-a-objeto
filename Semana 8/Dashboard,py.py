import os

# Función para mostrar el código de un script dado su ruta
def mostrar_codigo(ruta_script):
    # Convierte la ruta del script a una ruta absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Intenta abrir el archivo en modo lectura
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            # Lee y muestra el contenido del archivo
            print(archivo.read())
    except FileNotFoundError:
        # Maneja el caso en que el archivo no se encuentre
        print("El archivo no se encontró.")
    except Exception as e:
        # Maneja cualquier otro error que ocurra al leer el archivo
        print(f"Ocurrió un error al leer el archivo: {e}")

# Función para mostrar un menú de opciones y permitir al usuario elegir un script
def mostrar_menu():
    # Obtiene la ruta del directorio donde se encuentra el script actual
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    # Diccionario que asocia números de opción con las rutas absolutas de los scripts
    opciones = {
        '1': os.path.join(ruta_base, 'Abstracción/Ejemplo de Abstracción.py'),
        '2': os.path.join(ruta_base, 'Encapsulación/Ejemplo de Encapsulación.py'),
        '3': os.path.join(ruta_base, 'Herencia/Ejemplo de Herencia.py'),
        '4': os.path.join(ruta_base, 'Polimorfismo/Ejemplo de Polimorfismo.py'),
        '5': os.path.join(ruta_base, 'Semana 3/Programación orientado a objeto.py/Programación Tradicional.py'),
        '6': os.path.join(ruta_base, 'Semana 4/Ejemplo MundoReal_POO.py'),
        '7': os.path.join(ruta_base, 'Semana 5/Ejemplo de identificadores snake_case.py'),
        '8': os.path.join(ruta_base, 'Semana 6/Ejemplo de Clase,Objeto,herencia,encapsulación y polimorfismo.py'),
        '9': os.path.join(ruta_base, 'Semana 7/Ejemplo Implementación de Constructores y Destructores.py'),
        # Agrega aquí el resto de las rutas de los scripts según sea necesario
    }

    # Muestra el menú de opciones
    print("\n--- Menú de Opciones ---\n")
    for key, value in opciones.items():
        print(f"{key}. {value}")

    # Solicita al usuario que elija una opción
    eleccion = input("\nElige el número del script que deseas ver (o 'q' para salir): ")

    # Verifica si el usuario decide salir
    if eleccion.lower() == 'q':
        return

    # Verifica si la elección del usuario es válida
    if eleccion in opciones:
        # Muestra el código del script correspondiente
        mostrar_codigo(opciones[eleccion])
    else:
        # Indica que la opción no es válida
        print("Opción no válida. Inténtalo de nuevo.")

# Ejecuta el menú si el script se ejecuta directamente
if __name__ == "__main__":
    mostrar_menu()
