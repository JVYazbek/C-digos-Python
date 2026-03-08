'''Implemente uma função em Python para comparar as notas de alguns alunos
na primeira prova e na segunda prova aplicada por um professor. A função deve
receber como parâmetro duas listas de tuplas, onde cada tupla contém o nome
de um aluno e sua nota em uma prova. A função deve exibir os seguintes
resultados:
a) Alunos que melhoraram suas notas da primeira prova para a segunda.
b) Alunos que pioraram suas notas.
c) Alunos que mantiveram a mesma nota.
'''

p1 =[("Selmini", 8), ("Flávio", 7), ("Rafa", 9), ("Surian", 10)]
p2 =[("Selmini", 2), ("Flávio", 7), ("Rafa", 10), ("Surian", 10)]

melhor = []
pior = []
manteve = []

for i in range(len(p1)):
    aluno, nota1 = p1[i]
    aluno, nota2 = p2[i]
    delta = nota2 - nota1
    aux = (aluno, nota1, nota2, delta)
    if nota2 > nota1:
        melhor.append(aux)
    elif nota2 < nota1:
        pior.append(aux)
    else:
        manteve.append(aux)

print(f"alunos que melhoraram a nota --> {melhor}")
print(f"alunos que mantiveram a nota --> {manteve}")
print(f"alunos que pioraram a nota --> {pior}")