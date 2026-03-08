
#funçao para atualizar o estoque 
def atualizar(estoque, movimentacao):
    for mov in movimentacao:
        produto = mov[0]
        quantidade = mov[1]
        

        if produto not in estoque:
            estoque[produto] = {"saldo": quantidade, "min": 0, "preco": 0}

        estoque[produto]["saldo"] += quantidade
#função main
def main():
    estoque = {
    "café": {"saldo": 10, "min": 12, "preco": 12.50},
    "pão": {"saldo": 30, "min": 25, "preco": 2.00},
    "queijo": {"saldo": 5, "min": 12, "preco": 34.00},
    }
    movimentacao = [
        ["café", -3],
        ["pão", -10],
        ["café", 5],
        ["leite", 8] # produto novo não cadastrado
    ]

    #atualizar o estoque a partir das movimentações do dia 
    atualizar( estoque, movimentacao)

#Programa principal
if __name__ == '__main__':
    main()