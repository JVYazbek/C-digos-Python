class filmes:
    titulo: str
    ano : int

    def __init__(self, titulo = "", ano = ""):
        self.titulo = titulo
        self.ano = ano

x = list()
lista1 = []
quantidade = int(input("quantos filmes você vai analisar?"))
for _ in range(quantidade):
    titulo = input('digite o nome do filme -->')
    ano = input('digite o ano do filme')
    lista1.append(filmes(titulo, ano))