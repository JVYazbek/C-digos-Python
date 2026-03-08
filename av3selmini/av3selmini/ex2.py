class Trecho:
    dist_km: float
    vel_kmh: float
    semaforos: int
    
    def __init__(self, dist_km=0.0, vel_kmh=0.0, semaforos=0):
        self.dist_km = dist_km
        self.vel_kmh = vel_kmh
        self.semaforos = semaforos

class Rota:
    delay_sinal_padrao = 45.0

    nome: str
    trechos: list
    delay_sinal: float

    def __init__(self, nome='', trechos=None, delay_sinal=delay_sinal_padrao):
        self.nome = nome
        self.delay_sinal = delay_sinal
        
        if trechos is None:
            self.trechos = []
        else:
            self.trechos = trechos

    def distancia_total_km(self) -> float:
        distancia_total = 0.0
        for trecho in self.trechos:
            distancia_total += trecho.dist_km
        return distancia_total

    def total_de_semaforos(self) -> int:
        total_semaforos = 0
        for trecho in self.trechos:
            total_semaforos += trecho.semaforos
        return total_semaforos

    def tempo_total_min(self) -> float:
        tempo_h = 0.0
        for trecho in self.trechos:
            if trecho.vel_kmh > 0:
                tempo_h += trecho.dist_km / trecho.vel_kmh

        total_semaforos = self.total_de_semaforos()
        delay_min_por_sinal = self.delay_sinal / 60.0
        paradas_min = total_semaforos * delay_min_por_sinal
        tempo_total_min = (60 * tempo_h) + paradas_min

        return tempo_total_min

    def velocidade_media_kmh(self) -> float:
        distancia_total = self.distancia_total_km()
        tempo_total = self.tempo_total_min()

        if tempo_total == 0.0:
            return 0.0

        horas = tempo_total / 60.0
        velocidade_media = distancia_total / horas
        return velocidade_media

    def atende_janela(self, inicio_min: float, fim_min: float) -> bool:
        tempo = self.tempo_total_min()
        return inicio_min <= tempo <= fim_min

    def custo_emissao(self, kg_co2_km: float) -> float:
        dist_total = self.distancia_total_km()
        emissao = dist_total * kg_co2_km
        return emissao

def is_valid_float(texto_entrada: str) -> bool:
    if not texto_entrada:
        return False
    texto_limpo = texto_entrada.strip()
    
    if len(texto_limpo) > 0:
        primeiro_caractere = texto_limpo[0]
        if primeiro_caractere == '+' or primeiro_caractere == '-':
            texto_limpo = texto_limpo[1:]
    
    dot_count = 0
    digit_count = 0
    for caractere in texto_limpo:
        if '0' <= caractere <= '9':
            digit_count += 1
        elif caractere == '.':
            dot_count += 1
        else:
            return False
            
    return dot_count <= 1 and digit_count > 0

def is_valid_int(texto_entrada: str) -> bool:
    if not texto_entrada:
        return False
    texto_limpo = texto_entrada.strip()
    
    if len(texto_limpo) > 0:
        primeiro_caractere = texto_limpo[0]
        if primeiro_caractere == '+' or primeiro_caractere == '-':
            texto_limpo = texto_limpo[1:]
    
    return texto_limpo.isdigit() and len(texto_limpo) > 0

def ler_float_positivo(prompt: str) -> float:
    valor_lido = -1.0
    entrada_valida = False
    while not entrada_valida:
        entrada_usuario = input(prompt)
        if is_valid_float(entrada_usuario):
            valor_tentativa = float(entrada_usuario)
            if valor_tentativa >= 0:
                valor_lido = valor_tentativa
                entrada_valida = True
            else:
                print("O valor deve ser positivo ou zero.")
        else:
            print("Entrada inválida. Por favor, insira um número válido (float/decimal).")
    return valor_lido

def ler_int_positivo(prompt: str) -> int:
    valor_lido = 0
    entrada_valida = False
    while not entrada_valida:
        entrada_usuario = input(prompt)
        if is_valid_int(entrada_usuario):
            valor_tentativa = int(entrada_usuario)
            if valor_tentativa > 0:
                valor_lido = valor_tentativa
                entrada_valida = True
            else:
                print("O número deve ser maior que zero.")
        else:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    return valor_lido

def ler_int_nao_negativo(prompt: str) -> int:
    valor_lido = -1
    entrada_valida = False
    while not entrada_valida:
        entrada_usuario = input(prompt)
        if is_valid_int(entrada_usuario):
            valor_tentativa = int(entrada_usuario)
            if valor_tentativa >= 0:
                valor_lido = valor_tentativa
                entrada_valida = True
            else:
                print("O número não pode ser negativo.")
        else:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    return valor_lido

def ler_dados_rota(nome_rota: str) -> Rota:
    print(f"\n--- Leitura de Dados para {nome_rota} ---")
    
    delay_sinal_lido = Rota.delay_sinal_padrao
    entrada_valida = False
    while not entrada_valida:
        entrada_usuario_delay = input(f"Atraso médio por semáforo (segundos, Padrão: {Rota.delay_sinal_padrao:.1f}s): ")
        
        if not entrada_usuario_delay:
            delay_sinal_lido = Rota.delay_sinal_padrao
            entrada_valida = True
        elif is_valid_float(entrada_usuario_delay):
            valor_tentativa = float(entrada_usuario_delay)
            if valor_tentativa >= 0:
                delay_sinal_lido = valor_tentativa
                entrada_valida = True
            else:
                print("O atraso deve ser um valor positivo ou zero.")
        else:
            print("Entrada inválida. Por favor, insira um número ou deixe em branco.")

    num_trechos = ler_int_positivo("Quantos trechos esta rota possui? ")

    lista_de_objetos_trecho = []
    i = 1
    while i <= num_trechos: 
        print(f"Trecho {i}:") 
        
        distancia_trecho = ler_float_positivo("Distância (km): ") 
        
        velocidade_trecho = 0.0
        valido_velocidade = False
        while not valido_velocidade:
            velocidade_tentativa = ler_float_positivo("Velocidade Média (km/h): ") 
            if velocidade_tentativa > 0:
                velocidade_trecho = velocidade_tentativa
                valido_velocidade = True
            else:
                print("A velocidade deve ser um valor estritamente positivo (> 0).")
                
        semaforos_trecho = ler_int_nao_negativo("Número de semáforos: ") 
        
        novo_trecho = Trecho(
            dist_km=distancia_trecho,
            vel_kmh=velocidade_trecho,
            semaforos=semaforos_trecho
        )
        lista_de_objetos_trecho.append(novo_trecho)
        
        i += 1 
    
    return Rota(nome_rota, lista_de_objetos_trecho, delay_sinal_lido)

def programa_principal():
    print("--- Simulação de Logística de Rotas ---")
    
    kg_co2_km = ler_float_positivo("\nInforme o fator de emissão (kg CO2 por km rodado): ")
            
    inicio_janela = 0.0
    fim_janela = 0.0
    entrada_valida = False
    while not entrada_valida:
        print("\n--- Janela de Entrega (em minutos) ---")
        inicio_tentativa = ler_float_positivo("Início da janela de entrega (minutos): ")
        fim_tentativa = ler_float_positivo("Fim da janela de entrega (minutos): ")
        
        if inicio_tentativa >= 0 and fim_tentativa > inicio_tentativa:
            inicio_janela = inicio_tentativa
            fim_janela = fim_tentativa
            entrada_valida = True
        else:
            print("O início deve ser >= 0 e o fim deve ser estritamente maior que o início.")

    num_rotas = ler_int_positivo("\nQuantas rotas você deseja modelar? ")
            
    rotas = []
    i = 1
    while i <= num_rotas: 
        nome = input(f"Digite o nome da Rota {i}: ")
        rotas.append(ler_dados_rota(nome))
        i += 1

    print("\n" + "="*50)
    print("Resultado da simulação") 
    print(f"Janela de Entrega: [{inicio_janela:.2f} min - {fim_janela:.2f} min]")
    print(f"Fator de Emissão: {kg_co2_km:.4f} kg CO2/km")
    print("="*50)

    for rota in rotas:
        tempo_total = rota.tempo_total_min()
        dist_total = rota.distancia_total_km()
        vel_media = rota.velocidade_media_kmh()
        emissao = rota.custo_emissao(kg_co2_km)
        atende = rota.atende_janela(inicio_janela, fim_janela)

        print(f"\n--- Rota: {rota.nome} ---")
        print(f"Tempo Total de Viagem: {tempo_total:.2f} minutos") 
        print(f"Distância Total: {dist_total:.2f} km") 
        print(f"Velocidade Média Global: {vel_media:.2f} km/h") 
        print(f"Custo de Emissão (CO2): {emissao:.4f} kg") 
        print(f"Atende Janela de Entrega: {'SIM' if atende else 'NÃO'} (Tempo: {tempo_total:.2f} min)")
        print("\n[Ranking por Tempo Total]")

    i = 0
    while i < len(rotas):
        j = 0
        while j < len(rotas) - 1:
            if rotas[j].tempo_total_min() > rotas[j + 1].tempo_total_min():
                aux = rotas[j]
                rotas[j] = rotas[j + 1]
                rotas[j + 1] = aux
            j += 1
        i += 1

    pos = 1
    for rota in rotas:
        print(f"{pos}) {rota.nome} | Tempo: {rota.tempo_total_min():.2f} min | Vel. média: {rota.velocidade_media_kmh():.1f} km/h")
        pos += 1

    print(f"\n[Rotas que atendem a janela {inicio_janela:.0f}–{fim_janela:.0f} min]")

    for rota in rotas:
        if rota.atende_janela(inicio_janela, fim_janela):
            print(f"- {rota.nome} (Tempo: {rota.tempo_total_min():.2f} min)")

    print("\n[Comparativo de Emissões]")

    for rota in rotas:
        print(f"{rota.nome} | Dist: {rota.distancia_total_km():.2f} km | Emissão: {rota.custo_emissao(kg_co2_km):.2f} kg CO₂")    

if __name__ == "__main__":
    programa_principal()