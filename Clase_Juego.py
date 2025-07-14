from Clase_Personaje import Combatiente, Enemigo
from Clase_MagicItem import MagicItem
# Clase principal del juego
class Juego:
    def __init__(self):
        self.personajes = []
        self.objetos = []
        self.escenario = "Bosque Mágico tenebroso"
    def iniciar(self):
        print("Bienvenido al Reino Mágico de Gracelandia")
        print(f"Te encuentras en el {self.escenario}. La aventura comienza\n")
        # Crear personajes
        combatiente1 = Combatiente("Sonic", 20, 5, 1)
        combatiente2 = Enemigo("Mario", 20, 5, 1)
        self.personajes = [combatiente1, combatiente2]
        # Crear ítem
        pocion = MagicItem("Poción de Vida", "pocion", 10)
        self.objetos = [pocion]
        # Bucle del juego
        while combatiente1.vida > 0 and combatiente2.vida > 0:
            print("Estado actual:")
            combatiente1.estado()
            combatiente2.estado()
             #Un pequeño menu para dar interaccion entre los personajes 
            print("¿Qué deseas hacer?")
            print("1. Atacar al enemigo")
            print("2. Usar objeto mágico")
             #Una condicional la cual nos permite atacar o usar una pocion
            opcion = input("Elige (1 o 2): ")
            if opcion == "1":
                combatiente1.atacar(combatiente2)
            elif opcion == "2":
                self.objetos[0].usar(combatiente1)
            else:
                print("Opción no válida")
            if combatiente2.vida > 0:
                print("Turno del enemigo:")
                combatiente2.atacar(combatiente1)
        # Estado final
        print("nEstado final:")
        combatiente1.estado()
        combatiente2.estado()
        # Resultado
        print("Resultado del combate:")
        if combatiente1.vida > 0 and combatiente2.vida <= 0:
            print("Ganaste.")
        elif combatiente2.vida > 0 and combatiente1.vida <= 0:
            print("Perdiste.")
        elif combatiente1.vida <= 0 and combatiente2.vida <= 0:
            print("Ambos han muerto")
        else:
            print("La batalla ha finalizado")

# Ejecutar juego
juego = Juego()
juego.iniciar()
