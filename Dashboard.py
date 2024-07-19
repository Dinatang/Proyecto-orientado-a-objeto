import os

# Función para mostrar el código de un script dado su ruta
def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
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


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Abstracción/Ejemplo de Abstracción.py',
        '2': 'Encapsulación/Ejemplo de Encapsulación.py',
        '3': 'Herencia/Ejemplo de Herencia.py',
        '4': 'Polimorfismo/Ejemplo de Polimorfismo.py',
        '5': 'semana 3/Programación orientado a objeto.py',
        '6': 'semana 3/Programación Tradicional.py',
        '7': 'Semana 4/Ejemplo MundoReal_POO.py',
        '8': 'Semana 5 Tipo de Datos ,identificadores/Ejemplo de identificadores snake_case.py',
        '9': 'Semana 6 Definición Clase_Objeto_Herencia_encapsulación y polimorfismo/Ejemplo de Clase, objeto, herencia,encapsulación y polimorfismo.py',
        '10': 'semana 7 Implementación de Constructores y Destructores/ejemplo Implementación de Constructores y Destructores.py' ,

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
