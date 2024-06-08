class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"{self.nombre}:")
        print(f"·Fuerza: {self.fuerza}")
        print(f"·Inteligencia: {self.inteligencia}")
        print(f"·Defensa: {self.defensa}")
        print(f"·Vida: {self.vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto")

    def calcular_daño(self, enemigo):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def atacar(self, enemigo):
        daño = self.calcular_daño(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"Vida de {enemigo.nombre} es {enemigo.vida}")
        else:
            enemigo.morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10: "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print(f"·Espada: {self.espada}")

    def calcular_daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f"·Libro: {self.libro}")

    def calcular_daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\nTurno {turno}")
        print(f">>> Acción de {jugador_1.nombre}:")
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_vivo():
            print(f">>> Acción de {jugador_2.nombre}:")
            jugador_2.atacar(jugador_1)
        turno += 1

    if jugador_1.esta_vivo():
        print(f"\nHa ganado {jugador_1.nombre}")
    elif jugador_2.esta_vivo():
        print(f"\nHa ganado {jugador_2.nombre}")
    else:
        print("\nEmpate")


# Creación de personajes y ejecución del combate
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
