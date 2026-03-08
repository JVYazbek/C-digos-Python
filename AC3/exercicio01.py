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

q = int(input())

for x in range(q):
    i = input()
    c = input()
    v = float(input())
    t = float(input()) / 100
    n = int(input())
    emps.append(Emprestimo(v, t, n, i, c))


for i in range(len(emps)):
    for j in range(i + 1, len(emps)):
        if emps[j].juros() > emps[i].juros():
            a = emps[i]
            emps[i] = emps[j]
            emps[j] = a


print("[Ranking por Juros Totais]")
k = 1
for e in emps:
    p = e.parc()
    j = e.juros()
    print(str(k) + ") " + e.i + " - " + str(e.n) + "x | Parcela: R$ " + str(p) +
          " Juros Totais: R$ " + str(j) +
          " Custo Total: R$ " + str(e.v + j))
    k = k + 1


print("Saldo apos 12 parcelas")
for e in emps:
    print(e.i + " - " + str(e.n) + "x: R$ " + str(e.saldo(12)))