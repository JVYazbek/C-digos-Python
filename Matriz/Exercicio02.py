from random import randint
dp = 0
ds = 0

linha = 4
coluna = 4
m = [[(randint(1,20)) for j in range(coluna)]for i in range (linha)]
for i in range(len(m)):
    for j in range (len(m)):
        print(m[i][j], end="\t")
    print()
for i in range(len(m)):
    for j in range(len(m)):
        # Verifica se o elemnto está na diagonal principal
        if i == j:
            dp += m[i][j]
        # verifica se o elemento está na diagonal secundária
        if i + j == len(m) - 1:
            ds += m [i][j]
print(f'somda dos elementos da diagonal principal = {dp}')
print(f'soma dos elementos da diagonal secundária {ds}')
