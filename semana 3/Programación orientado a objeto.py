# Programación Tradicional

def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Ingreso de temperaturas
temperaturas = ingresar_temperaturas()

# Cálculo del promedio semanal
promedio = calcular_promedio_semanal(temperaturas)

print(f"Las temperaturas ingresadas son: {temperaturas}")
print(f"El promedio semanal de las temperaturas es: {promedio}")
