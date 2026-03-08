import math
class Ponto:
    #Metodo Construtor
    def __init__(self, x : int = 0, y : int = 0):
        self.x = x
        self.y = y

    #Método para calcular e retornar a distância de dois pontos
    def calcular_distancia(self, p : "Ponto") -> float:
        return math.hypot(self.x - p.x, self.y - p.y)
    
    #Método para calcular e retornar a distância de um ponto até a origem
    def calcular_distancia_ate_origem(self) -> float:
        return math.hypot(self.x, self.y)
    
    #Sobreposição de método ou override
    def __str__(self):
        return f"({self.x}, {self.y})"
    