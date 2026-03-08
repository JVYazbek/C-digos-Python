# Arquivo: src/carro.py

class Carro:
    """
    Classe Carro definida dentro do pacote 'src'.
    """
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        """Liga o carro."""
        if not self.ligado:
            self.ligado = True
            return f"O {self.marca} {self.modelo} ligou."
        return f"O {self.marca} {self.modelo} já está ligado."

    def __str__(self):
        """Representação amigável do objeto para impressão."""
        estado = "Ligado" if self.ligado else "Desligado"
        return f"Carro: {self.marca} {self.modelo} | Estado: {estado}"

# print(f"O módulo carro.py foi carregado.")