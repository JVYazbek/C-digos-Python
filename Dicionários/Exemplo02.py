'''
    A partir de uma lista de palavras(que pode haver repetição), imprimir 
    a quantidade de vezes que cada palvra aparece.Por último imprimir a ocorrência de cada letra.

'''
lista = []
total = int(input("Qual o total de palavras?"))
for i in range(total):
    lista.append(input("Palavra: "))

#Contar o número de ocorrencias de cada uma das palavras
ocorrencia_palavra = {}
for palavra in lista:
    if palavra in ocorrencia_palavra:
        ocorrencia_palavra[palavra] += 1
    else:
        ocorrencia_palavra[palavra] = 1
# impressão da ocorrência das palavras
for chave , valor in ocorrencia_palavra.itens():
    print(f'{chave}--> {valor}')

ocorencia_letra = {}
for palavra in lista:
    for letra in palavra:
        if letra in ocorencia_letra:
            ocorencia_letra[letra] += 1
        else:
            ocorencia_letra[letra] = 1

print("\nOcorrência das letras")
for chave,valor in ocorencia_letra.items():
    print(f"{chave} --> {valor}")
    