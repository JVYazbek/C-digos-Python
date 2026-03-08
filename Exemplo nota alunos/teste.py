import busca_ordenacao
from random import randint

lista = [randint(1, 500) for _ in range(10)]
print(busca_ordenacao.bolha(lista))
