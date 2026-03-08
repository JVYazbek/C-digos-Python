# função randon
import random

# função jogar 
def jogar(palavras):
    segredo = random.choice(palavras).lower()

    #listas auxiliares
    linhas =['_'] * len(segredo) 
    
    erro = 0

    while erro <= 6 and '_' in linhas:
        print(linhas)
        letra = input("informe uma letra-->")
        
        if letra in segredo:
            for i in range(len(segredo)):
                if segredo[i] == letra:
                    linhas[i] = letra
        else:
            erro += 1
            print(f'Você errou pela {erro}ª vez. Tente novamnete!')

    if '_' not in linhas:
        print("Você acertou!")
    else:
        print("Você foi enforcado!")

# função ler_palavras
def ler_palavras():
    palavras = []
    for i in range (5):
        palavras.append(input("informe uma palavra --->"))
    return palavras

# função principal
def main():
    palavras = ler_palavras()
    jogar(palavras)

# programa principal
if __name__ == '__main__':
    main()
