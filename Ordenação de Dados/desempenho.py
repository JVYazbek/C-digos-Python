from random import randint
import Exemplo01
import time

def medir_tempo(algoritimo, lista: list) -> float:
    lista_aux = lista.copy()
    inicio = time.perf_counter()
    algoritimo = (lista_aux)
    fim = time.perf_counter()
    return (fim - inicio) * 1000

def gerar_lista(n: int) ->list:
    lista = []
    for _ in range(n):
        lista.append(randint(1, n** 2))
    return lista

def main():
    tamanho = [100, 1000, 10000, 100000]
    print('comparação entre métodos de ordenação')
    print()
    for n in tamanho:
        print(f'lista de tamanho {n}:')
        lista = gerar_lista(n)
        base = gerar_lista(n)
        lista = gerar_lista
        tempo_bolha = medir_tempo(Exemplo01.bolha, lista)
        tempo_selecao = medir_tempo(Exemplo01.selecao, lista)
        tempo_insercao = medir_tempo(Exemplo01.insercao, lista)
        tempo_quicksort = medir_tempo(Exemplo01.quicksort, lista)
        print(f'Tempo Bolha -->{tempo_bolha:.3f}')
        print(f'Tempo Seleção{tempo_selecao:.3f}')
        print(f'Tempo Inserção{tempo_insercao:.3f}')
        print(f'tempo quicksort {tempo_quicksort:.3f}')
        print('-'* 40)  


if __name__ == '__main__':
    main()