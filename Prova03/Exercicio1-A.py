from Classes import hospede
from Classes import quarto

#hospedes
quantidade = int(input("Digite o numero de hospedes--> "))
x = list()
lista1 = []
for i in range(quantidade):
    nome = input("digite o nome do hospede--> ")
    lista1.append(hospede(nome))


#Quartos

y = list()
lista2 = []
for _ in range(quantidade):
    numero = int(input("Digite qual é o número do quarto--> "))
    valor = float(input("Digite qual é o valor da diária desse quarto--> R$"))
    lista2.append(quarto(numero, valor))


for hospedes in lista1:
    print(f" O hospede -> {hospedes.nome}")
for quartos in lista2:
    print(f"Ficará com o Quarto-->{quartos.numero} cujo valor da diária é R${quartos.valor} por dia")

dias = int(input("digite o número de dias que os hospedes vão ficar hospedados"))

totalpago = valor * dias
for hospedes in lista1:
    print(f" O hospede -> {hospedes.nome} terá que pagar {totalpago} no final de sua estadia")

totalrecebido = valor * quantidade
print(f"O total recebido pela pousada é de {totalrecebido}")








    
