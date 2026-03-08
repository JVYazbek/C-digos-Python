from ponto import Ponto
lista =[]
quantidade = int(input("Qual a quantidade de pontos -->"))
for _ in range(quantidade):
    x = int(input("Coordenada x -->"))
    y = int(input("Coordenada y -->"))
    lista.append(Ponto(x, y))

#Impressão de cada ponto e sua respectiva distância até o centro
print("Distância de cada ponto até a origem (0,0):")
for p in lista:
    print(f"{p} --> {p.calcular_distancia_ate_origem()}")

print()
print(f"Distancia entre os pontos 1 e 2")
print(lista[0].calcular_distancia(lista[1]))
    