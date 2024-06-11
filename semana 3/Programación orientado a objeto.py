
# Programación Orientada a Objetos (POO)

class Clima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temperatura):
        self.temperaturas.append(temperatura)

    def calcular_promedio_semanal(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

# Creación del objeto Clima
clima = Clima()

# Ingreso de temperaturas
for i in range(7):
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
    clima.ingresar_temperatura(temp)

# Cálculo del promedio semanal utilizando el método del objeto
promedio = clima.calcular_promedio_semanal()

print(f"Las temperaturas ingresadas son: {clima.temperaturas}")
print(f"El promedio semanal de las temperaturas es: {promedio}")
