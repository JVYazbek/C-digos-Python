from random import randint

lista_original = []
lista_nova = []

# Lendo os valores para a lista original
for i in range(randint(2, 8)):
    lista_original.append(randint(-2, 10))
    if lista_original [i] not in lista_nova:
        lista_nova.append(lista_original[i]) 
print(f'lista original -->{lista_original}')
print(f'lista nova -->{lista_nova}')