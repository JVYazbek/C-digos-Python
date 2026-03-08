#1)
import random

n = int(input("Digite a ordem da matriz: "))

def gerar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(random.randint(0, 9))
        matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()
    print()

def vizinhos(matriz, i, j):
    n = len(matriz)
    v = []

    if i > 0 and j > 0:
        v.append(matriz[i-1][j-1])
    if i > 0:
        v.append(matriz[i-1][j])
    if i > 0 and j < n-1:
        v.append(matriz[i-1][j+1])

    if j > 0:
        v.append(matriz[i][j-1])
    if j < n-1:
        v.append(matriz[i][j+1])

    if i < n-1 and j > 0:
        v.append(matriz[i+1][j-1])
    if i < n-1:
        v.append(matriz[i+1][j])
    if i < n-1 and j < n-1:
        v.append(matriz[i+1][j+1])

    return v

def maior_valor(lista):
    maior = lista[0]
    for k in range(1, len(lista)):
        if lista[k] > maior:
            maior = lista[k]
    return maior

def menor_valor(lista):
    menor = lista[0]
    for k in range(1, len(lista)):
        if lista[k] < menor:
            menor = lista[k]
    return menor

def classificar_pontos(matriz):
    n = len(matriz)
    nova = []

    for i in range(n):
        linha = []
        for j in range(n):
            v = vizinhos(matriz, i, j)
            maior = maior_valor(v)
            menor = menor_valor(v)

            if matriz[i][j] > maior:
                linha.append('P')  
            elif matriz[i][j] < menor:
                linha.append('V') 
            else:
                linha.append('N')  
        nova.append(linha)
    return nova

matriz = gerar_matriz(n)
print("Matriz original (altitudes):")
imprimir_matriz(matriz)

classificada = classificar_pontos(matriz)
print("Matriz classificada (P/V/N):")
imprimir_matriz(classificada)

#2)
import random

def gerar_labirinto(n):
    lab = []

    for i in range(n):
        linha = []
        for j in range(n):
            if random.random() < 0.5:
                linha.append('#')
            else:
                linha.append('.')
        lab.append(linha)

    ei, ej = random.randint(0, n-1), random.randint(0, n-1)
    si, sj = random.randint(0, n-1), random.randint(0, n-1)

    while (ei, ej) == (si, sj):
        si, sj = random.randint(0, n-1), random.randint(0, n-1)

    lab[ei][ej] = 'E'
    lab[si][sj] = 'S'

    return lab, (ei, ej), (si, sj)

def imprimir_labirinto(lab):
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            print(lab[i][j], end=" ")
        print()
    print()

def existe_caminho(lab, i, j, si, sj):
    n = len(lab)

    if (i, j) == (si, sj):
        return True

    if lab[i][j] != 'E': 
        lab[i][j] = 'x'

    if i > 0 and lab[i-1][j] not in ['#', 'x']:
        if existe_caminho(lab, i-1, j, si, sj):
            return True

    if i < n-1 and lab[i+1][j] not in ['#', 'x']:
        if existe_caminho(lab, i+1, j, si, sj):
            return True
    
    if j > 0 and lab[i][j-1] not in ['#', 'x']:
        if existe_caminho(lab, i, j-1, si, sj):
            return True
  
    if j < n-1 and lab[i][j+1] not in ['#', 'x']:
        if existe_caminho(lab, i, j+1, si, sj):
            return True

    return False

n = int(input("Digite a ordem do labirinto: "))
labirinto, entrada, saida = gerar_labirinto(n)

print("Labirinto gerado:")
imprimir_labirinto(labirinto)

ei, ej = entrada
si, sj = saida

if existe_caminho(labirinto, ei, ej, si, sj):
    print("Existe um caminho entre 'E' e 'S'")
else:
    print("Não existe caminho entre 'E' e 'S'")

#3)
pedidos = {
    "P001": {"cliente": "Selmini", "produtos": {"Metanol": 100.0, "Vinho": 450.0}},
    "P002": {"cliente": "Surjan", "produtos": {"Bolas": 40.0}},
    "P003": {"cliente": "Selmini", "produtos": {"Conjunto de Taças": 90.0, "Etanol": 150.0}},
    "P004": {"cliente": "Humberto", "produtos": {"Fuzil de Assalto": 950.0}}
}

total_pedido = {}
for pedido_id, info in pedidos.items():
    soma = 0
    for preco in info["produtos"].values():
        soma += preco
    total_pedido[pedido_id] = soma

print(f"Total por pedido:{total_pedido}")

total_cliente = {}
for pedido_id, info in pedidos.items():
    cliente = info["cliente"]
    gasto = total_pedido[pedido_id]
    if cliente not in total_cliente:
        total_cliente[cliente] = gasto
    else:
        total_cliente[cliente] += gasto

print(f"Total por cliente:{total_cliente}")

cliente_top = None
maior_gasto = 0
for cliente, total in total_cliente.items():
    if total > maior_gasto:
        maior_gasto = total
        cliente_top = cliente

print(f" Cliente que mais gastou:{cliente_top}: {maior_gasto}")

faturamento_total = 0
for total in total_pedido.values():
    faturamento_total += total

print(f" Faturamento total da loja: {faturamento_total}")

# 4)
precos = {
    "arroz": 22.5,
    "feijao": 9.8,
    "leite": 4.7,
    "pao": 1.5
}
vendas = [
     ["arroz", "feijao", "feijao", "leite"],
    ["pao", "pao", "pao", "leite"],
    ["arroz", "leite"],
    ["feijao", "feijao", "feijao"]
]

# a)
totais_venda = []
for venda in vendas:
    total = 0.0
    for item in venda:
         total += precos[item]
    totais_venda.append(total)

# b)
faturamento_total = 0.0
for t in totais_venda:
    faturamento_total += t

# c)
qtd_por_item = {}
for venda in vendas:
     for item in venda:
        qtd_por_item[item] = qtd_por_item.get(item, 0) + 1

# d)
mais_vendido = None
mais_vendido_qtd = -1
for item, qtd in qtd_por_item.items():
    if qtd > mais_vendido_qtd:
        mais_vendido_qtd = qtd
        mais_vendido = item

faturamento_por_item = {}
for item, qtd in qtd_por_item.items():
    faturamento_por_item[item] = qtd * precos[item]

mais_faturado = None
mais_faturado_valor = -1.0
for item, val in faturamento_por_item.items():
    if val > mais_faturado_valor:
        mais_faturado_valor = val
        mais_faturado = item

# e)
numero_de_vendas = len(vendas)
ticket_medio = faturamento_total / numero_de_vendas if numero_de_vendas > 0 else 0.0

relatorio_mercearia = {
    "totais_venda": totais_venda,
    "faturamento_total": faturamento_total,
    "qtd_por_item": qtd_por_item,
    "mais_vendido": mais_vendido,
    "mais_faturado": mais_faturado,
    "ticket_medio": ticket_medio
}

# 5)
aulas = ["A1", "A2", "A3", "A4", "A5"]
presencas = {
    "Toffano": ["P", "P", "F", "P", "P"],
    "Antonio": ["P", "F", "F", "P", "F"],
    "Marcos": ["P", "P", "P", "P", "P"],
    "Selmini": ["F", "F", "P", "F", "P"]
}

# a)
por_aluno = {}
total_aulas = len(aulas)
for aluno, marcas in presencas.items():
    pres = marcas.count("P")
    falt = marcas.count("F")
    perc = (pres / total_aulas) * 100 if total_aulas > 0 else 0.0
    situacao = "APROVADO" if perc >= 75.0 else "REPROVADO"
    por_aluno[aluno] = {"P": pres, "F": falt, "perc": perc, "situacao": situacao}

# c) 
faltas_por_aula = [0] * total_aulas
for marcas in presencas.values():
    for i, m in enumerate(marcas):
        if m == "F":
            faltas_por_aula[i] += 1

indice_mais_faltas = 0
maior_faltas_aula = faltas_por_aula[0]
for i, val in enumerate(faltas_por_aula):
    if val > maior_faltas_aula:
        maior_faltas_aula = val
        indice_mais_faltas = i

aula_mais_faltas = aulas[indice_mais_faltas]


melhor_presenca = None
melhor_presenca_val = -1
mais_faltas = None
mais_faltas_val = -1
for aluno, info in por_aluno.items():
    if info["P"] > melhor_presenca_val:
     melhor_presenca_val = info["P"]
     melhor_presenca = aluno
    if info["F"] > mais_faltas_val:
        mais_faltas_val = info["F"]
    mais_faltas = aluno

soma_percentuais = 0.0
num_alunos = len(por_aluno)
for info in por_aluno.values():
    soma_percentuais += info["perc"]
presenca_media_turma = soma_percentuais / num_alunos if num_alunos > 0 else 0.0

relatorio_presencas = {
    "por_aluno": por_aluno,
    "aula_mais_faltas": aula_mais_faltas,
    "melhor_presenca": melhor_presenca,
    "mais_faltas": mais_faltas,
    "presenca_media_turma": presenca_media_turma
}

print("=== Relatório Mercearia ===")
for k, v in relatorio_mercearia.items():
    print(f"{k}: {v}")
print("\n=== Relatório Presenças ===")
for k, v in relatorio_presencas.items():
    print(f"{k}: {v}")