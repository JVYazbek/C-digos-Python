from ponto import Ponto
class Retangulo:
    # Método construtor
    def __init__(self, largura : float, altura : float , canto_superior_esquerdo: "Ponto"):
        self.largura = largura
        self.altura = altura
        self.canto_superior_esquerdo = canto_superior_esquerdo

    # Método para calcular e retornar a área
    def calcular_area(self) -> float:
        return self.altura * self.largura
    
    # Método para calcular e retornar o perímetro
    def calcular_perimetro(self) -> float:
        return 2 * (self.altura + self.largura)
    
    # Método para aumentar o tamnho do retângulo
    def aumentar_tamanho(self, altura: float, largura: float) -> float:
        self.largura += largura
        self.altura += altura

    # Método para retornar a coordenada do centro do retângulo
    def coordenada_centro(self) -> Ponto:
        xc = self.canto_superior_esquerdo.x + self.largura / 2
        yc = self.canto_superior_esquerdo.y - self.altura / 2
        return Ponto(xc, yc)
