'''Uma equipe de engenheiros ambientais está analisando o relevo de uma região
representada por uma matriz de altitudes. Cada posição da matriz indica a altura do terreno em
uma determinada coordenada.
Seu objetivo é desenvolver um programa em Python para ajudar a equipe a identificar os pontos
mais altos (picos) e os pontos mais baixos (vales) do mapa, considerando a altitude dos vizinhos
ao redor.
Regras: Considere a vizinhança de 8 direções (norte, sul, leste, oeste e diagonais). Para cada célula
(i, j) da matriz:
 Se celula[i][j] for maior que todos os seus vizinhos, ela é um pico.
 Se celula[i][j] for menor que todos os seus vizinhos, ela é um vale.
 Caso contrário, é um ponto neutro.
O programa deverá executar as seguintes funcionalidade:
a) Ler a ordem da matriz a partir do terminal.
b) Preencher a matriz com valores inteiros aleatórios (utilizar o módulo random). O
preenchimento da matriz deverá ocorrer em uma função.
c) Imprimir a matriz em formato tabular (a impressão deverá ser ocorrer em uma função,
diferente da função que fez o preenchimento).
d) Criar uma nova matriz do mesmo tamanho onde 'P' representa pico, 'V' representa vale e 'N'
representa ponto neutro. A geração da matriz deverá ocorrer em uma função.
e) Imprima no terminal a nova matriz em formato tabular (a impressão deve ocorrer em uma
função). Veja um exemplo a seguir'''
import random

n = int(input("Digite a ordem da matriz: "))

def gerar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(random.randint(0, 9))
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()
    print()

def vizinhos(matriz, i, j):
    n = len(matriz)
    v = []

    if i > 0 and j > 0:
        v.append(matriz[i-1][j-1])
    if i > 0:
        v.append(matriz[i-1][j])
    if i > 0 and j < n-1:
        v.append(matriz[i-1][j+1])

    if j > 0:
        v.append(matriz[i][j-1])
    if j < n-1:
        v.append(matriz[i][j+1])

    if i < n-1 and j > 0:
        v.append(matriz[i+1][j-1])
    if i < n-1:
        v.append(matriz[i+1][j])
    if i < n-1 and j < n-1:
        v.append(matriz[i+1][j+1])

    return v

def maior_valor(lista):
    maior = lista[0]
    for k in range(1, len(lista)):
        if lista[k] > maior:
            maior = lista[k]
    return maior

def menor_valor(lista):
    menor = lista[0]
    for k in range(1, len(lista)):
        if lista[k] < menor:
            menor = lista[k]
    return menor

def classificar_pontos(matriz):
    n = len(matriz)
    nova = []

    for i in range(n):
        linha = []
        for j in range(n):
            v = vizinhos(matriz, i, j)
            maior = maior_valor(v)
            menor = menor_valor(v)

            if matriz[i][j] > maior:
                linha.append('P')  
            elif matriz[i][j] < menor:
                linha.append('V') 
            else:
                linha.append('N')  
        nova.append(linha)
    return nova

matriz = gerar_matriz(n)
print("Matriz original (altitudes):")
imprimir_matriz(matriz)

classificada = classificar_pontos(matriz)
print("Matriz classificada (P/V/N):")
imprimir_matriz(classificada)
