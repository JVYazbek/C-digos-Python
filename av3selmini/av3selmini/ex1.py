class Emprestimo:
    def __init__(self, v, t, n, i, c):
        self.v = v  
        self.t = t  
        self.n = n  
        self.i = i  
        self.c = c  

    def parc(self):
        if self.t == 0:
            return self.v / self.n
        return self.v * (self.t / (1 - (1 + self.t) ** (-self.n)))

    def saldo(self, k):
        if self.t == 0:
            return self.v * (1 - k / self.n)
        p = self.parc()
        return self.v * (1 + self.t) ** k - p * ((1 + self.t) ** k - 1) / self.t

    def juros(self):
        return self.n * self.parc() - self.v

emps = []

q = int(input("Coloque a quantidade de emprestimentos que serão cadastrados -> "))

for x in range(q):
    print(f"\n--- Cadastro do {x+1}º empréstimo ---")
    i = input("Identificador do empréstimo (Ex: Plano A): ")
    c = input("Nome do cliente: ")
    v = float(input("Valor financiado (P): "))
    t = float(input("Taxa de juros mensal em % (Ex: 1.5): ")) / 100
    n = int(input("Número total de parcelas (n): "))
    emps.append(Emprestimo(v, t, n, i, c))


for i in range(len(emps)):
    for j in range(i + 1, len(emps)):
        if emps[j].juros() > emps[i].juros():
            emps[i], emps[j] = emps[j], emps[i]

print("\n[Ranking por Juros Totais]")
k = 1
for e in emps:
    p = e.parc()
    j = e.juros()
    custo_total = e.v + j
    print(f"{k}) {e.i} - {e.n}x | Parcela: R$ {p:.2f} | Juros Totais: R$ {j:.2f} | Custo Total: R$ {custo_total:.2f}")
    k += 1

print("\n[Saldos após 12 parcelas]")
for e in emps:
    
    s = e.saldo(12) if e.n >= 12 else 0.0
    print(f"{e.i} - {e.n}x: R$ {max(0, s):.2f}")