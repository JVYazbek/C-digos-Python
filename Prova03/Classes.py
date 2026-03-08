class hospede:
    nome : str

    def __init__(self, nome = ""):
        self.nome = nome
    
class quarto:
    numero : int
    valor : float

    def __init__(self, numero = "", valor = ""):
        self.numero = numero
        self.valor = valor

class reserva:
    def __init__(self, nome = "", numero = "", valor =""):
        self.nome = hospede.nome
        self.numero = quarto.numero
        self.valor = quarto.valor
