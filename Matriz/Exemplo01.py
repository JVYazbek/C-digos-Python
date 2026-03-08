
linha = int(input("total de linhas -->"))
coluna = int(input("total de colunas -->"))

m = []
# Controle de linha
for i in range(linha):
    aux = []
    #Controle de coluna
    for j in range(coluna):
        aux.append(int(input("digite o valor-->")))
    m.append(aux)

print(m)