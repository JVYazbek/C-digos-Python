"""a) Leia uma lista contendo vários dicionários. Cada dicionário tem duas chaves (pai e filho) e,
 o valor de cada chave é a sequência de DNA. Por exemplo: {"pai":"AACCTGGA", "filho":"AAGCTGGT"}.
 Não há a necessidade de verificar se os caracteres são válidos ou não. 
 Você deve validar apenas o tamanho das sequências que devem ser iguais e ter no mínimo 2 caracteres.

b) Um método deverá ser chamado para verificar se há compatibilidade entre as sequências.
O método deverá retornar um valor boolean true (caso haja compatibilidade) ou false (caso não haja).
Se houve compatibilidade deverá ocorrer a impressão POTENCIAL PAI-FILHO ou NÃO COMPATÍVEL de acordo com
 o retorno da função."""

lista = []
numero = int(input("digite o número de comparações que serão feitas-->"))
for i in range(numero):
    nome_pai = (input("Nome_Pai-->"))
    pai = (input("DNA_Paterno-->")).upper()
    nome_filho = (input("Nome_filho-->"))
    filho = input("DNA_filho-->").upper()
    lista.append({'Nome do Pai':nome_pai,'DNA Paterno':pai,'nome do filho':nome_filho, 'DNA filho':filho})
    letrasp = len(pai)
    letrasf = len(filho)
    if letrasp == letrasf:
        print("Sequências de tamnaho válido!")
    elif letrasp or letrasf <2:
        print("Sequências de tamnaho inválido!")
    else: 
        print("Sequências de tamanho inválido!")
    print(lista)
    