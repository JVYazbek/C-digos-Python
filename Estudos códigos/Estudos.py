# Busca sequencial
def busca_sequencial(lista: list[int], valor: int)-> int:
    for i in range (len(lista)):
        if lista[i] == valor:
            return i
        return -i
    
# Busca binaria *valor foi definido antes desse código em um exercicio*
def busca_binaria(lista: list[int, valor]):
    ini, fim = 0, len(lista) -1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            ini = meio + 1
        else:
            fim = meio -1
    return -1

# Bubble sort
def bolha(lista):
    for _ in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i]> lista[i+1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista

#Método de seleção
def selecao(x):
    n = len(x)
    for i in range(n - 1):
        menor = i 
        for j in range( i + 1, n):
            if x[j] < x[menor]:
                menor = j

            # Troca os elementos (essa linha precisa estar dentro do laço)
            x[i], x[menor] = x[menor], x[i]
        return x
# Inercao
def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
        x[i + 1] = valor

# Quick sort
def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len (lista) - 1

    if inicio < fim:
        pivote = particionar(lista, inicio, fim)
        quicksort(lista, iniciio, pivote -1)
        quicksort(lista, pivote + 1, fim)

def particiionar(lista, inicio, fim)-> int: # Devolve o índicie do pivote
    pivote = lista[fim]
    i = inicio -1

    for j in range(inicio, fim):
        if lista[j]<= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    # Coloca o  pivote na localização correta
    lista[i+1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

