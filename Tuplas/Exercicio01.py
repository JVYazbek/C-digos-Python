"""1. Implemente uma função em Python que recebe uma lista de tuplas, onde cada
tupla representa as coordenadas (x, y) de um ponto no plano cartesiano. A
função deve gerar e imprimir no terminal as seguintes informações:
a) O ponto mais distante da origem (0, 0).
b) O ponto mais próximo da origem (0, 0).
c) A média das distâncias dos pontos à origem.
Para calcular a distância de um ponto p de coordenas (x, y) até a origem (0, 0)
utiliza-se a expressão:
d = raiz de x ao quadrado + y ao quadrado"""

from random import randint
from math import sqrt

def gerar_pontos():
    lista = [] #--> lista = list()
    for _ in range(randint(1, 5)):
        lista.append((randint(-10, 10), randint(-10, 10)))
    return lista
# função para calcular a distância de cada um dos pontos até a origem
def calcular_distancia(lista):
    distancia = []
    for i in range (len(lista)):
        x, y = lista[i]
        distancia.append(sqrt(x*x+y*y))
    return distancia

# função para retornar o ponto mais distante da origem
def mais_distante (lista, distancia):
    ponto = lista[0]
    maior = distancia[0]
    for i in range(len(lista)):
        if distancia[i] > maior:
            maior = distancia[i]
            ponto = lista[i]
    return ponto

# função para retornar o ponto mais proximo a origem 
def mais_proxmimo (lista, distancia):
    ponto = lista[0]
    menor = distancia[0]
    for i in range(len(lista)):
        if distancia[i] > menor:
            menor = distancia[i]
            ponto = lista[i]
    return ponto
# função para calcular a média das distâncias 
def calcularmedia(distancia):
    media = 0
    for d in distancia:
        media += d
    return media / len(distancia)


# função main()
def main():
    lista = gerar_pontos()
    distancia = calcular_distancia(lista)
    for i in range(len(lista)):
        print(f"{lista[i]}-->{distancia[i]:.2f}")
    
    print(f'ponto mais distante em relação a origem --> {mais_distante(lista, distancia)}')
    print(f'ponto mais próximo em relação a origem --> {mais_proxmimo(lista, distancia)}')
    print(f'média das distâncias --> {calcularmedia(distancia):.2f}')

    
#Programa principal
if __name__ == '__main__':
    main()