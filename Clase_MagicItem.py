# Clase para los objetos mágicos
class MagicItem:
    def __init__(self, nombre, tipo, efecto):
        # Atributos del objeto mágico
        self.nombre = nombre
        self.tipo = tipo  
        self.efecto = efecto
    # Método que aplica el efecto del objeto al personaje
    def usar(self, personaje):
        if self.tipo == "pocion":
            personaje.vida += self.efecto
            print(f"{personaje.nombre} usa {self.nombre} y recupera {self.efecto} puntos de vida.")
