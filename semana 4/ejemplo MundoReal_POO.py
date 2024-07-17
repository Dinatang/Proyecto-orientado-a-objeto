# Definición de la clase CarroDeportivo que hereda de Carro
class CarroDeportivo(carro):
    def __init__(self, color, marca, modelo, caballos_de_fuerza):
        super().__init__(color, marca, modelo)  # Llama al constructor de la clase base
        self.caballos_de_fuerza = caballos_de_fuerza  # Añade un nuevo atributo específico para el carro deportivo

    def turbo(self):
        """Activa el modo turbo del carro deportivo."""
        if self.motor_encendido:  # Solo se puede activar el turbo si el motor está encendido
            self.velocidad += 50
            print(f"El {self.marca} {self.modelo} activó el turbo a {self.velocidad} km/h")
        else:
            print(f"El motor del {self.marca} {self.modelo} está apagado. No se puede activar el turbo.")

# Ejemplo de uso de la clase CarroDeportivo
mi_deportivo = CarroDeportivo('rojo', 'Ferrari', 'F8', 710)
mi_deportivo.encender_motor()  # Encender el motor del carro deportivo
mi_deportivo.acelerar(30)  # Acelerar el carro deportivo en 30 km/h
mi_deportivo.turbo()  # Activar el modo turbo
mi_deportivo.frenar(60)  # Frenar el carro deportivo en 60 km/h
mi_deportivo.apagar_motor()  # Apagar el motor del carro deportivo
mi_deportivo.mostrar_info()  # Mostrar la información del carro deportivo
