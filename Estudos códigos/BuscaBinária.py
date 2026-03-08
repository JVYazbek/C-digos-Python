def busca_binaria(lista_ordenada, alvo):
    """
    Realiza a busca binária de um 'alvo' em uma 'lista_ordenada'.

    Args:
        lista_ordenada (list): A lista de elementos ORDENADA.
        alvo: O valor a ser encontrado.

    Returns:
        int: O índice do 'alvo' se encontrado, ou -1 se não estiver presente.
    """
    
    baixo = 0                    # Início da faixa de busca
    alto = len(lista_ordenada) - 1 # Fim da faixa de busca

    # Continua buscando enquanto a faixa for válida (baixo <= alto)
    while baixo <= alto:
        
        # 1. Encontra o ponto médio
        # (Usamos // para divisão inteira)
        meio = (baixo + alto) // 2 
        
        elemento_central = lista_ordenada[meio]

        # 2. Comparação
        if elemento_central == alvo:
            # Sucesso: O alvo foi encontrado no meio
            return meio
        
        elif elemento_central < alvo:
            # O alvo é maior, então descartamos a metade inferior.
            # Movemos 'baixo' para a direita do meio.
            baixo = meio + 1
            
        else: # elemento_central > alvo
            # O alvo é menor, então descartamos a metade superior.
            # Movemos 'alto' para a esquerda do meio.
            alto = meio - 1

    # Falha: O alvo não foi encontrado na lista
    return -1

# --- Exemplo de Uso ---
# OBSERVAÇÃO: A lista DEVE estar ordenada!
lista_de_numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
numero_procurado = 23
numero_inexistente = 40

# Busca bem-sucedida
indice_encontrado = busca_binaria(lista_de_numeros, numero_procurado)
print(f"Lista: {lista_de_numeros}")

if indice_encontrado != -1:
    print(f"O número {numero_procurado} foi encontrado no índice: {indice_encontrado}")
else:
    print(f"O número {numero_procurado} não foi encontrado.")

# Busca sem sucesso
indice_nao_encontrado = busca_binaria(lista_de_numeros, numero_inexistente)
if indice_nao_encontrado != -1:
    print(f"O número {numero_inexistente} foi encontrado no índice: {indice_nao_encontrado}")
else:
    print(f"O número {numero_inexistente} não foi encontrado.")