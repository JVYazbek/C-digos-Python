def busca_linear(lista, alvo):
    """
    Realiza a busca linear de um 'alvo' em uma 'lista'.

    Args:
        lista (list): A lista de elementos a ser pesquisada.
        alvo: O valor a ser encontrado na lista.

    Returns:
        int: O índice do 'alvo' na lista se encontrado, ou -1 se não estiver presente.
    """
    
    # Itera sobre cada elemento da lista, usando o índice 'i'
    for i in range(len(lista)):
        
        # 1. Comparação: Verifica se o elemento atual é igual ao alvo
        if lista[i] == alvo:
            # 2. Sucesso: Se encontrado, retorna o índice (posição)
            return i
            
    # 3. Falha: Se o loop terminar sem encontrar o alvo, retorna -1
    return -1

# --- Exemplo de Uso ---
minha_lista = [5, 15, 8, 42, 1, 30, 19]
numero_alvo = 42
numero_ausente = 100

# Busca bem-sucedida
indice_encontrado = busca_linear(minha_lista, numero_alvo)

if indice_encontrado != -1:
    print(f"O número {numero_alvo} foi encontrado no índice: {indice_encontrado}")
else:
    print(f"O número {numero_alvo} não foi encontrado na lista.")

print("-" * 20)

# Busca sem sucesso
indice_nao_encontrado = busca_linear(minha_lista, numero_ausente)

if indice_nao_encontrado != -1:
    print(f"O número {numero_ausente} foi encontrado no índice: {indice_nao_encontrado}")
else:
    print(f"O número {numero_ausente} não foi encontrado na lista.")