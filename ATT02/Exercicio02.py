'''Um robô explorador está em um labirinto representado por uma matriz de caracteres, onde:
'S' representa o ponto de saída, '.' representa um caminho livre, '#' representa uma parede e 'E'
representa o ponto de entrada (posição inicial do robô). O robô pode se mover para cima, para
baixo, para a esquerda ou para a direita, mas não nas diagonais. Você deve criar um programa
em Python que realize as seguintes funcionalidades:
a) Gerar um labirinto de caracteres. A ordem da matriz que representará o labirinto deverá ser
informada pelo terminal. A geração do labirinto deverá ser realizada em uma função. Veja a
seguir um exemplo de labirinto (a entrada e saída não precisam estar necessariamente nas
bordas da matriz). Veja a seguir um exemplo de labirinto.
# # # # # #
# E . . # #
# # . # . #
# . . # S #
# # # # # #
b) Uma função deverá verificar se existe ou não um caminho de 'E' até 'S'. A função deverá
retornar um valor booleano. No caso do labirinto mostrado no exemplo acima não há um
caminho entre 'E' e 'S'.'''
import random

def gerar_labirinto(n):
    lab = []

    for i in range(n):
        linha = []
        for j in range(n):
            if random.random() < 0.5:
                linha.append('#')
            else:
                linha.append('.')
        lab.append(linha)

    ei, ej = random.randint(0, n-1), random.randint(0, n-1)
    si, sj = random.randint(0, n-1), random.randint(0, n-1)

    while (ei, ej) == (si, sj):
        si, sj = random.randint(0, n-1), random.randint(0, n-1)

    lab[ei][ej] = 'E'
    lab[si][sj] = 'S'

    return lab, (ei, ej), (si, sj)

def imprimir_labirinto(lab):
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            print(lab[i][j], end=" ")
        print()
    print()

def existe_caminho(lab, i, j, si, sj):
    n = len(lab)

    if (i, j) == (si, sj):
        return True

    if lab[i][j] != 'E': 
        lab[i][j] = 'x'

    if i > 0 and lab[i-1][j] not in ['#', 'x']:
        if existe_caminho(lab, i-1, j, si, sj):
            return True

    if i < n-1 and lab[i+1][j] not in ['#', 'x']:
        if existe_caminho(lab, i+1, j, si, sj):
            return True
    
    if j > 0 and lab[i][j-1] not in ['#', 'x']:
        if existe_caminho(lab, i, j-1, si, sj):
            return True
  
    if j < n-1 and lab[i][j+1] not in ['#', 'x']:
        if existe_caminho(lab, i, j+1, si, sj):
            return True

    return False

n = int(input("Digite a ordem do labirinto: "))
labirinto, entrada, saida = gerar_labirinto(n)

print("Labirinto gerado:")
imprimir_labirinto(labirinto)

ei, ej = entrada
si, sj = saida

if existe_caminho(labirinto, ei, ej, si, sj):
    print("Existe um caminho entre 'E' e 'S'")
else:
    print("Não existe caminho entre 'E' e 'S'")