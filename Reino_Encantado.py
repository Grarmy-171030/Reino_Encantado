class Personaje:
    def __init__(self, nombre, vida, ataque, nivel):
        #Atributos del personaje 
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
    #Metodo atacar
    def atacar(self, objetivo):
        #Se le quita vida al jugador por el ataque 
        objetivo.vida -= self.ataque
        print(f"{self.nombre} ataca a {objetivo.nombre} y le quita {self.ataque} de vida.")
    #Metodo  donde indica el estado Inicial de vida de los jugadores
    def estado(self):
        print(f"{self.nombre} tiene {self.vida} puntos de vida.")
#Clase hijas 
class Combatiente(Personaje):
    pass
class Enemigo(Personaje):
    pass
#Clase de los Item Magicos
class MagicItem:
    def __init__(self, nombre, tipo, efecto):
        #Atributos de los Item
        self.nombre = nombre
        self.tipo = tipo
        self.efecto = efecto
    #Metodo de Usar personajes 
    def usar(self, personaje):
        #Condicional para el uso de pocion o armadura
        if self.tipo == "pocion":
            personaje.vida += self.efecto
            print(f"{personaje.nombre} usa {self.nombre} y recupera {self.efecto} de vida.")
#Clase juego
class Juego:
    def __init__(self):
        self.personajes = []
        self.objetos = []
        self.escenario = "Bosque Mágico tenebroso"
    #Metodo de Iniciar-juego  con una narrativa como introducción
    def iniciar(self):
        print("Bienvenido al Reino Mágico de Gracelandia")
        print(f"Te encuentras en el {self.escenario}. La aventura comienza\n")
        #Objetos creados para el juego  
        combatiente1 = Combatiente("Sonic", 20, 5, 1)
        combatiente2 = Enemigo("Mario", 15, 3, 1)
        self.personajes = [combatiente1, combatiente2]
        #Objeto de Item
        pocion = MagicItem("Poción de Vida", "pocion", 10)
        self.objetos = [pocion]
        #Estado Inicial de los dos jugadores
        print("Estado inicial:")
        combatiente1.estado()
        combatiente2.estado()
        #Un pequeño menu para dar interaccion entre los personajes 
        print("\n¿Qué deseas hacer?")
        print("1. Atacar al enemigo")
        print("2. Usar objeto mágico")
        #Una condicional la cual nos permite atacar o usar una pocion
        opcion = input("Elige (1 o 2): ")
        if opcion == "1":
            combatiente1.atacar(combatiente2)
        elif opcion == "2":
            self.objetos[0].usar(combatiente1)
        else:
            print("Opción no válida. No haces nada.")
        if combatiente2.vida > 0:
            print("\nTurno del enemigo:")
            combatiente2.atacar(combatiente1)
        #Estado final de los jugadores 
        print("\nEstado final:")
        combatiente1.estado()
        combatiente2.estado()

# Iniciar el juego
juego = Juego()
juego.iniciar()


