from random import randint

def ler_dados():
    total_ano = int(input('informe o total de anos para análise -->'))
    total_mes = int(input('informe o total de mes para análise -->'))
    tempreratura = [[randint(5, 40) for j in range(total_mes)]for i in range(total_ano)]
    return tempreratura

def imprimir(temperatura):
    for i in range(len(temperatura)):
        for j in range(len(temperatura[i])):
            print(temperatura[i][j], end='\t')
        print()

def calcular_media_anual(temperatura):
    media = []
    for i in range(len(temperatura[i])):
        aux = 0
        for j in range(len(temperatura[i])):
            aux += temperatura[i][j]
            media.append(aux/ len(temperatura[i]))
        return media
    
def imprimir_media(media):
    for i in range(len(media)):
        print(f'Ano {i + 1}--> {media[i]:.2f}')
    
def calcular_maior_media(media):
    aux = 0
    ano = 0
    for i in range(len(media)):
        if media [i] > aux:
            aux = media[i]
    return aux
def calcular_menor_media(media):
     aux = 0
     ano = 0
     for i in range(len(media)):
        if media [i] < aux:
            aux = media[i]
     return aux

#função main
def main():
    temperatura = ler_dados()
    imprimir(temperatura)
    media = calcular_media_anual(temperatura)
    print('media anual')
    imprimir_media(media)
    ano_maior_media = calcular_maior_media(media)
    print(f"Ano com maior média é{(ano_maior_media):.2f}")
    ano_menor_media = calcular_maior_media(media)
    print(f"Ano com maior média é{(ano_menor_media):.2f}")
    

#programa principal
if __name__ == '___main__':
    main()