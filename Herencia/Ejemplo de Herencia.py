class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    # Métodos getter
    def get_nombre(self):
        return self.__nombre

    def get_fuerza(self):
        return self.__fuerza

    def get_inteligencia(self):
        return self.__inteligencia

    def get_defensa(self):
        return self.__defensa

    def get_vida(self):
        return self.__vida

    # Métodos setter
    def set_vida(self, vida):
        self.__vida = vida

    # Otros métodos
    def atributos(self):
        print(f"{self.__nombre}:")
        print(f"·Fuerza: {self.__fuerza}")
        print(f"·Inteligencia: {self.__inteligencia}")
        print(f"·Defensa: {self.__defensa}")
        print(f"·Vida: {self.__vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa

    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(f"{self.__nombre} ha muerto")

    def calcular_daño(self, enemigo):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def atacar(self, enemigo):
        daño = self.calcular_daño(enemigo)
        enemigo.set_vida(enemigo.get_vida() - daño)
        print(f"{self.get_nombre()} ha realizado {daño} puntos de daño a {enemigo.get_nombre()}")
        if enemigo.esta_vivo():
            print(f"Vida de {enemigo.get_nombre()} es {enemigo.get_vida()}")
        else:
            enemigo.morir()


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.__espada = espada

    # Métodos getter
    def get_espada(self):
        return self.__espada

    # Métodos setter
    def set_espada(self, espada):
        self.__espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10: "))
        if opcion == 1:
            self.set_espada(8)
        elif opcion == 2:
            self.set_espada(10)
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print(f"·Espada: {self.__espada}")

    def calcular_daño(self, enemigo):
        return self.get_fuerza() * self.__espada - enemigo.get_defensa()


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.__libro = libro

    # Métodos getter
    def get_libro(self):
        return self.__libro

    def atributos(self):
        super().atributos()
        print(f"·Libro: {self.__libro}")

    def calcular_daño(self, enemigo):
        return self.get_inteligencia() * self.__libro - enemigo.get_defensa()


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\nTurno {turno}")
        print(f">>> Acción de {jugador_1.get_nombre()}:")
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_vivo():
            print(f">>> Acción de {jugador_2.get_nombre()}:")
            jugador_2.atacar(jugador_1)
        turno += 1

    if jugador_1.esta_vivo():
        print(f"\nHa ganado {jugador_1.get_nombre()}")
    elif jugador_2.esta_vivo():
        print(f"\nHa ganado {jugador_2.get_nombre()}")
    else:
        print("\nEmpate")


# Creación de personajes y ejecución del combate
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
