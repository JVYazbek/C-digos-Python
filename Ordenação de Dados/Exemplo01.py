def bolha(v):
    for j in range(len(v)):
        for i in range(len(v) - 1):
            if v[i] > v[i + 1]:
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux


#Função para ordenar lista pelo método da seleção
def selecao(x):
    n = len(x)
    for i in range(n-1):
        menor = i
        for j in range(i +1, n):
            if x[j] < x[menor]:
                menor = j


    #Troca dos elementos (essa linha precisa estar dentro do laço externo)
    x[i], x[menor] = x[menor], x[i]

def insercao(x):
    n = len(x)
    for j in range(1, n):
        valor = x[j]
        i = j - 1
        while i >= 0 and valor < x[i]:
            x[i + 1] = x[i]
            i -= 1
            x[i + 1] = valor

#--------------------------------------------------------------------------------
# Função para ordenar uma lista pelo método quicksort (pivô como ultimo elemento)
def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1

    if inicio < fim:
        pivo = particionar(lista, inicio, fim)
        quicksort(lista, inicio, pivo - 1)
        quicksort(lista, pivo + 1, fim)
    
def particionar(lista, inicio, fim) -> int: #Retorna o Indice do Pivô
    pivo = lista[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
        
    # colocar Pivô no local correto
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1