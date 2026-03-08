import random
from ponto import Ponto
from Exercicio03 import Retangulo

lista = []
for _ in range(random.randint(1, 10)):
    p = Ponto(random.randint(3, 15), random.randint(4, 16))
    altura = random.randint(5, 10)
    largura = random.randint(3, 12)
    lista.append(Retangulo(largura, altura, p))

# Impressão dos Dados
for r in lista:
    print(f"Área = {r.calcular_area()} | perímetro = {r.calcular_perimetro()} | coordenada do centro = { r.coordenada_centro()}")
    