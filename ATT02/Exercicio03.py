'''Uma loja online registra os pedidos de seus clientes em um dicionário, onde a chave é o ID
do pedido e o valor contém informações do cliente e dos produtos. Seu objetivo é gerar relatórios
de vendas e clientes usando apenas dicionários.
O dicionário contendo os pedidos deverá ter o nome pedidos e deverá ter a estrutura conforme
exemplo a seguir. Durante a avaliação serão utilizados outros exemplos, mas seguindo a mesma
estrutura.
pedidos = {
"P001": {"cliente": "Ana", "produtos": {"Mouse": 80.0, "Teclado": 120.0}},
"P002": {"cliente": "Bruno", "produtos": {"Monitor": 700.0}},
"P003": {"cliente": "Ana", "produtos": {"Cabo HDMI": 40.0, "Mouse": 80.0}},
"P004": {"cliente": "Carla", "produtos": {"Cadeira Gamer": 950.0}}
}
Escreva um programa em Python que realize as seguintes funcionalidades:
a) Calcular o total gasto em cada pedido. Exemplo: {"P001": 200.0, "P002": 700.0, ...}.
b) Calcular o total gasto por cliente. Exemplo: {"Ana": 320.0, "Bruno": 700.0, "Carla": 950.0}.
c) Identificar o cliente que mais gastou.
d) Calcular e imprimir o faturamento total da loja.
4. (2,0) Uma pequena mercearia utiliza um sistema simples para registrar suas vendas diárias.
Os preços de cada produto estão armazenados em um dicionário, e cada venda é representada
por uma lista de itens vendidos. O gerente deseja obter algumas informações consolidadas para
'''

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
