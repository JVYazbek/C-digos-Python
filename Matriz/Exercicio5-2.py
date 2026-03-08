from random import randint

def gerar_matriz():
    ordem = randint(2,5)
    matriz = [[randint(0, 10)for j in range(ordem)]for i in range(ordem)]
    return matriz

#Função para imprimir a matiz no principal
def imprimir(matriz):
    ordem = len(matriz)
    for i in range(ordem):
        for j in range(ordem):
            print(matriz[i][j], end='\t')
        print()

def trocar(matriz):
    j = len(matriz) - 1
    for i in range(len(matriz)):
        aux = matriz[i][i] 
        matriz[i][i] = matriz [i] [j]
        matriz[i][j] = aux
        j -= 1

# programa principal
matriz = gerar_matriz()
print('Impressão antes da troca')
imprimir(matriz)
print("\nImpressão após a troca")
trocar(matriz)
imprimir(matriz)
