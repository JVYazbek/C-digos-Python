def ordenar_por_juncao(lista_principal):
    # Condição de parada (lista já ordenada se tiver 0 ou 1 elemento)
    if len(lista_principal) <= 1:
        return lista_principal

    # 1. DIVISÃO
    ponto_medio = len(lista_principal) // 2
    
    # Sublistas
    metade_a = lista_principal[:ponto_medio]
    metade_b = lista_principal[ponto_medio:]

    # Chamadas recursivas para ordenar as sublistas
    metade_a = ordenar_por_juncao(metade_a)
    metade_b = ordenar_por_juncao(metade_b)

    # 2. JUNÇÃO (MERGE)
    # Combina as duas sublistas ordenadas
    return juntar_listas_ordenadas(metade_a, metade_b)

def juntar_listas_ordenadas(lista_um, lista_dois):
    """
    Função auxiliar para combinar duas listas já ordenadas.
    """
    resultado_final = []
    i = j = 0 # 'i' é o índice para 'lista_um', 'j' para 'lista_dois'

    # Enquanto houver elementos em ambas as listas
    while i < len(lista_um) and j < len(lista_dois):
        if lista_um[i] < lista_dois[j]:
            # Adiciona o menor elemento de 'lista_um' ao resultado
            resultado_final.append(lista_um[i])
            i += 1
        else:
            # Adiciona o menor elemento de 'lista_dois' ao resultado
            resultado_final.append(lista_dois[j])
            j += 1

    # Adiciona os elementos restantes, se houver, de 'lista_um'
    resultado_final.extend(lista_um[i:])
    # Adiciona os elementos restantes, se houver, de 'lista_dois'
    resultado_final.extend(lista_dois[j:])

    return resultado_final

# --- Exemplo de Uso ---
dados_nao_ordenados = [64, 25, 12, 22, 11]
dados_ordenados = ordenar_por_juncao(dados_nao_ordenados)
print(f"Dados originais: {dados_nao_ordenados}")
print(f"Dados ordenados: {dados_ordenados}")