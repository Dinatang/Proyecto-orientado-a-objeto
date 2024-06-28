# programa para calcular el área superficial de un cubo

def calcular_area_cubo(lado):
    """
    Función para calcular el área superficial de un cubo dado el lado de una de sus caras.
    :param lado: El lado de una de las caras del cubo (float)
    :return: El área superficial del cubo (float)
    """
    area_cara = lado ** 2
    area_total = 6 * area_cara
    return area_total

if __name__ == "__main__":
    # Asignación de valores
    lado_cubo = float(input("Introduce el lado del cubo: "))  # Ingresamos el valor del lado

    # Llamada a la función para calcular el área superficial
    area_cubo = calcular_area_cubo(lado_cubo)

    # Mostrar el resultado
    print(f"El área superficial del cubo con lado {lado_cubo} es: {area_cubo}")

    # Ejemplo de uso de diferentes tipos de datos
    numero_entero = 42          # Tipo de dato entero (int)
    numero_decimal = 3.14       # Tipo de dato flotante (float)
    texto = "Hola, mundo!"      # Tipo de dato cadena de texto (string)
    es_mayor = True             # Tipo de dato booleano (bool)

    # Imprimir ejemplos de diferentes tipos de datos
    print(f"Ejemplo de entero: {numero_entero}")
    print(f"Ejemplo de flotante: {numero_decimal}")
    print(f"Ejemplo de cadena de texto: {texto}")
    print(f"Ejemplo de booleano: {es_mayor}")
