# Função para o calculo dos grãos
def calcular() -> int:
    total = 0
    for i in range (64):
        total += 2 ** i
    return total

# Programa principal
total = calcular()
print(f"total de grãos:{total}")
