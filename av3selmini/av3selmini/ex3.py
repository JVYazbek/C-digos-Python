class Docente:
    def __init__(self, nome_docente, quantidade_aulas, custo_hora_aula, titulacao):
        self.nome_docente = nome_docente
        self.quantidade_aulas = quantidade_aulas
        self.custo_hora_aula = custo_hora_aula
        self.titulacao = titulacao

    def salario_base(self):
        salario_parcial = self.quantidade_aulas * 4.5 * self.custo_hora_aula

        percentual_titulacao = 0.0

        if self.titulacao == 'Mestre':
            percentual_titulacao = 0.085
        elif self.titulacao == 'Doutor':
            percentual_titulacao = 0.12

        salario_final = salario_parcial * (1 + percentual_titulacao)
        return salario_final

    def hora_atividade(self, base_salarial):
        return base_salarial * 0.05

    def DescansoSemanal(self, base_salarial, valor_hora_atividade):
        remuneracao_s_descanso = base_salarial + valor_hora_atividade
        valor_descanso = remuneracao_s_descanso / 6
        return valor_descanso

    def remuneracao_total(self):
        base_salarial = self.salario_base()
        valor_hora_atividade = self.hora_atividade(base_salarial)
        valor_descanso = self.DescansoSemanal(base_salarial, valor_hora_atividade)

        salario_bruto = base_salarial + valor_hora_atividade + valor_descanso

        return salario_bruto

def coleta_dados_docente(indice):
    print("\n--- Informações do Docente", indice, "---")
    nome_docente = input("Nome: ")

    aulas = int(input("Quantidade de aulas semanais: "))
    while aulas < 0:
        print("A quantidade de aulas semanais não pode ser negativa.")
        aulas = int(input("Quantidade de aulas semanais: "))

    valor = float(input("Custo da hora-aula (ex: 50.00): "))
    while valor < 0:
        print("O custo da hora-aula não pode ser negativo.")
        valor = float(input("Custo da hora-aula (ex: 50.00): "))

    titulos_aceitos = ['Nenhum', 'Mestre', 'Doutor']
    titulacao = input("Titulação (Nenhum, Mestre, Doutor): ")
    
    entrada_valida = False
    while not entrada_valida:

        if titulacao in titulos_aceitos:
            entrada_valida = True
        else:
            print("Titulação inválida, digite 'Nenhum', 'Mestre' ou 'Doutor'.")
            titulacao = input("Titulação (Nenhum, Mestre, Doutor): ")

    return Docente(nome_docente, aulas, valor, titulacao)

def execucao_principal():
    lista_docentes = []
    
    contador = 1
    numero_de_docentes = 2
    while contador <= numero_de_docentes:
        novo_docente = coleta_dados_docente(contador)
        lista_docentes.append(novo_docente)
        contador += 1

    indice = 0
    while indice < len(lista_docentes):
        docente = lista_docentes[indice]
        remuneracao_total = docente.remuneracao_total()
        
        print("\nDocente:", docente.nome_docente)
        print("Titulação:", docente.titulacao)
        print(f"Remuneração Total (Salário Bruto): R$ {remuneracao_total:.2f}")
        indice += 1
        
if __name__ == "__main__":
    execucao_principal()