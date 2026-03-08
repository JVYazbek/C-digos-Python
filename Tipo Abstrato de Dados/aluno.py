class Aluno:
    # Atributos (variavel de instância) do Objeto
    nome : str
    ra : int
    nota1: float
    nota2: float

    # Construtor
    def __init__(self, nome = '', ra = 0, nota1 = 0, nota2 = 0):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self) -> float:
        return (self.nota1 + self.nota2) / 2
    
    def situacao(self) -> str:
        media = self.calcular_media()
        if media >= 7:
            return "APROVADO"
        return "REPROVADO"
    

