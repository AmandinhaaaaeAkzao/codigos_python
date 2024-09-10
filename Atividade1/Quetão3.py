






# Função para calcular a velocidade do projétil
def calcular_velocidade(distancia_km, tempo_min):
    # Convertendo distância de km para metros
    distancia_m = distancia_km * 1000
    
    # Convertendo tempo de minutos para segundos
    tempo_s = tempo_min * 60
    
    # Calculando a velocidade em metros por segundo
    velocidade_mps = distancia_m / tempo_s
    
    return velocidade_mps

# Solicitar entrada do usuário
distancia_km = float(input("Digite a distância percorrida em quilômetros: "))
tempo_min = float(input("Digite o tempo gasto em minutos: "))

# Calcular a velocidade
velocidade = calcular_velocidade(distancia_km, tempo_min)

# Exibir o resultado
print(f"A velocidade do projétil é {velocidade:.2f} metros por segundo.")
