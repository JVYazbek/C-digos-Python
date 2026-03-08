#função multiplicação
def multi(m: int, n: int) -> int:
    if n == 0: return 0
    if n > 0: return m + multi(m, n - 1)

# função principal
def main():
    m = int(input("informe o primeiro valor -->"))
    n = int(input("informe o segundo valor -->"))
    print(f" ({m} * {n}) = {multi(m, n)} ")
#Programa principal
if __name__ == '__main__':
    main()