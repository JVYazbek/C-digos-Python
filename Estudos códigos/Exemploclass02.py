# Arquivo: main.py

# A instrução 'from src.carro import Carro' diz:
# 1. Procure pelo PACOTE 'src'
# 2. Dentro do pacote 'src', procure pelo MÓDULO (arquivo) 'carro'
# 3. Importe a CLASSE 'Carro' desse módulo
from Exemploclass01 import Carro

print("--- Inicializando o Sistema de Veículos ---")

# Criando instâncias da classe Carro importada
meu_carro = Carro("Tesla", "Model S")
carro_esportivo = Carro("Ferrari", "SF90")

# Usando os métodos dos objetos
print(f"\n1. Criado: {meu_carro}")
print(f"2. Criado: {carro_esportivo}")

# Chamando o método 'ligar'
mensagem_ligar = meu_carro.ligar()
print(f"\nOperação: {mensagem_ligar}")

# Verificando o status
print(f"Status Atual: {meu_carro}")