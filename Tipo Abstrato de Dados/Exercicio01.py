from aluno import Aluno

# Lista de alunos 
x = list()
lista = []
for _ in range(3):
    nome = input("Nome --> ")
    ra = int(input("RA -->"))
    nota1 = float(input("Nota 1 -->"))
    nota2 = float(input("Nota 2 -->"))
    lista.append(Aluno(nome, ra, nota1, nota2))
    print("-" * 30)

# Impressão do nome, da méida e da situação
print(f"{"Nome":<20}{"Média":<10}{"Situação"}")
print('-' * 40)
for alunos in lista:
    media = alunos.calcular_media()
    print(f"{alunos.nome:<20}{media:<10.2f}{alunos.situacao()}")
