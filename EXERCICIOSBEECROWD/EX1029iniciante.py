#variável global
chamada = 0 
# função recursiva para fib
def fib(x):
    global chamada
    if x == 0: 
        return 0
    elif x == 1:
        return 1
    chamada += 2
    return fib(x - 2) + fib(x - 1)
#programa principal
n = int(input())
for i in range(n):
    x = int(input())
    chamada = 0
    f = fib(x)
    print(f'fib({x}) = {chamada} calls = {f}')