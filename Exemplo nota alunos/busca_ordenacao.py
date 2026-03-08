
#Função para realizar a busca linear em uma lista númerica.
#A função deve receber como parâmetro a lista e o valor a ser localizado.


#função para ordenar uma lista de números inteiros em ordem crescente usando o método bolha (bubblesort)

def bolha(lista: list[int]) -> list[int]:
    for j in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista
