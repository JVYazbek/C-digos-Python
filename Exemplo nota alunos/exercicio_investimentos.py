import random
nome_arquivo = "investimentos.txt"
n = 12
i = random.randint(1, 4) / 100

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha == "":
            continue
        nome, valor_aux = linha.split(";")
        valor = float(valor_aux)
        
        parcela = valor * (i * (i+1)**n)/((i+1)**n-1)
        print(f"{nome}--> valor da parcela: R$ {parcela:.2f}")