
# função criptografada
def criptografar(texto: str) -> str:
    aux = ""
    for letra in texto:
        if letra.isalpha():
            aux += chr(ord(letra) + 3)
        else:
            aux += letra
    
    aux = aux[::-1]

    meio = len(aux) // 2
    resultado = ""
    for i in range(len(aux)):
        if i >= meio:
            resultado += chr(ord(aux[i]) - 1)
        else:
            resultado += aux[i]

    return resultado
    

def main():
    N = int(input())
    for _ in range(N):
        texto = input()
        texto_cripto = criptografar(texto)
        print(texto_cripto)
   
if __name__ == "__main__":
    main()
