total = 0
#bloco de leitura de arquivo
with open("alunos.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        nome, nota1, nota2 = linha.split(";")
        print(nome)
        print(nota1)
        print(nota2)
        calculo_media = (float(nota1) + float(nota2)) / 2
        print(f"{nome}--> {calculo_media:.2f}")
        if calculo_media >=6.0:
            total += 1
    print(f"total de alunos aprovados{total:.2f}")