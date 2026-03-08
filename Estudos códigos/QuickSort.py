def quick_sort(lista, baixo, alto):
    """
    Função principal do Quick Sort.
    Ordena a sublista entre os índices 'baixo' e 'alto'.
    """
    if baixo < alto:
        # 'pi' é o índice de particionamento, lista[pi] está agora no lugar certo
        pi = particionar(lista, baixo, alto)

        # Chama a função recursivamente para ordenar os elementos
        # antes e depois da partição
        quick_sort(lista, baixo, pi - 1)  # Ordena a sublista esquerda
        quick_sort(lista, pi + 1, alto)  # Ordena a sublista direita

def particionar(lista, baixo, alto):
    """
    Esta função toma o último elemento como pivo, coloca o pivo em 
    sua posição correta na lista ordenada, e coloca todos os elementos 
    menores à esquerda do pivo e os maiores à direita.
    Retorna o índice final do pivo.
    """
    pivo = lista[alto]  # Escolhe o último elemento como pivo
    i = (baixo - 1)  # Índice do menor elemento

    for j in range(baixo, alto):
        # Se o elemento atual for menor ou igual ao pivo
        if lista[j] <= pivo:
            # Incrementa o índice do menor elemento
            i = i + 1
            # Troca lista[i] e lista[j]
            lista[i], lista[j] = lista[j], lista[i]

    # Troca o pivo (lista[alto]) com o elemento em lista[i + 1]
    lista[i + 1], lista[alto] = lista[alto], lista[i + 1]
    
    return (i + 1)

# --- Exemplo de Uso ---
dados_desordenados = [10, 80, 30, 90, 40, 50, 70]
n = len(dados_desordenados)

quick_sort(dados_desordenados, 0, n - 1)

print(f"Dados desordenados originais: [10, 80, 30, 90, 40, 50, 70]")
print(f"Lista ordenada (Quick Sort): {dados_desordenados}")