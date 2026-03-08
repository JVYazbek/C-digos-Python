'''Implemente uma função em Python que recebe uma lista de tuplas, onde cada
tupla representa um intervalo numérico [𝑎𝑎, 𝑏𝑏], com 𝑎𝑎 ≤ 𝑏𝑏. A função deve
realizar as seguintes operações:
a) unir intervalos que se sobrepõem: se dois intervalos [𝑎𝑎, 𝑏𝑏] e [𝑐𝑐, 𝑑𝑑] se
sobrepõem (ou seja, 𝑏𝑏 ≥ 𝑐𝑐), eles devem ser unidos em um único intervalo.
b) contar o número total de intervalos resultantes.
c) Retornar a soma total do comprimento de todos os intervalos resultantes.
'''
numero_intervalos = input("digite os intervalo")
lista = [numero_intervalos]
lista.append(input(f"digite o valor do número{lista}º"))


print(f"{lista}")
