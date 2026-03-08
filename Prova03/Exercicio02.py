class chamado:
     id : int
     tiutlo : str
     prioridade : int
     status: str

def __init__(self, id = "", titulo = "", prioridade = "", status = ""):
        self.id = id
        self.titulo = titulo
        self.prioridade = prioridade
        self.status = status

x = list()
lista1 = []
for i in range():
    id = int(input("digite o nome do hospede--> "))
    titulo = input("digite o titulo do chamado")
    prioridade = input("digite a prioridade do seu chamado")
    status = input("digite se estão trabalhando no seu chamado ou não")
    lista1.append(chamado(id, titulo, prioridade, status))
    


def urgencia():
       if chamado.id > 3:
              print("baixa urgencia")
       elif chamado.id == 3:
              print ("urgencia média")
       else:
              print("alta urgencia")
    