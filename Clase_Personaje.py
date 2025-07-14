# Clase base para todos los personajes
class Personaje:
    def __init__(self, nombre, vida, ataque, nivel):
        # Atributos del personaje
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
    # Método para atacar a otro personaje
    def atacar(self, objetivo):
        objetivo.vida -= self.ataque
        print(f"{self.nombre} ataca a {objetivo.nombre} y le quita {self.ataque} puntos de vida.")

    # Método para mostrar el estado actual del personaje
    def estado(self):
        print(f"{self.nombre} tiene {self.vida} puntos de vida.")

# Clases hijas que heredan de Personaje
class Combatiente(Personaje):
    pass
class Enemigo(Personaje):
    pass
