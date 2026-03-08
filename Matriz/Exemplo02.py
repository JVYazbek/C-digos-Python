
linha = int(input("total de linhas -->"))
coluna = int(input("total de colunas -->"))

m = [[int(input("digite o valor-->")) for j in range(coluna)] for i in range(linha)]

print(m)