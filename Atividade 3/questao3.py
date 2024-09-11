def calcular_temperaturas():
    temperaturas = []
    
    # Leitura das temperaturas
    print("Digite 7 temperaturas:")
    for i in range(7):
        while True:
            try:
                temperatura = float(input(f"Temperatura {i + 1}: "))
                temperaturas.append(temperatura)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
    
    # Calcula a média das temperaturas
    media = sum(temperaturas) / len(temperaturas)
    
    # Inicializa contadores
    acima_ou_igual_media = 0
    abaixo_media = 0
    
    # Contagem das temperaturas
    for temp in temperaturas:
        if temp >= media:
            acima_ou_igual_media += 1
        else:
            abaixo_media += 1
    
    # Exibição dos resultados
    print(f"\nMédia das temperaturas: {media:.2f}")
    print(f"Número de temperaturas iguais ou acima da média: {acima_ou_igual_media}")
    print(f"Número de temperaturas abaixo da média: {abaixo_media}")

if __name__ == "__main__":
    calcular_temperaturas()
