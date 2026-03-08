#função criptografada
def criptografar(texto:str, deslocamento: int)->str:
    aux = ""
    for letra in texto:
        if letra.isalpha():
            codigo = ord(letra)
            aux += chr(((codigo - 97 + deslocamento) % 26 ) + 97)
        else:
            aux += letra
    return aux
#função descriptografar
def descriptografar(texto_cripto: str, deslocamento: int) -> str:
    return criptografar(texto_cripto, - deslocamento)

#função principal
def main():
    texto = input("informe uma frase-->").lower()
    deslocamento = int(input("deslocamento:"))
    texto_cripto = criptografar(texto, deslocamento)
    print(texto_cripto)
    original = descriptografar(texto_cripto, deslocamento)
    print(original)
#Função main
if __name__ == "__main__":
    main()