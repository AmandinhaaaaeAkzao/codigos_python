def processar_lista(lista):
    # Inicializa os contadores e a soma
    quantidade_negativos = 0
    soma_positivos = 0
    
    # Percorre cada número na lista
    for numero in lista:
        if numero < 0:
            quantidade_negativos += 1
        elif numero > 0:
            soma_positivos += numero
    
    # Exibe os resultados
    print(f"Quantidade de números negativos: {quantidade_negativos}")
    print(f"Soma dos números positivos: {soma_positivos}")

def main():
    # Solicita ao usuário que insira 8 números
    numeros = []
    print("Digite 8 números:")
    for i in range(8):
        while True:
            try:
                numero = float(input(f"Número {i + 1}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
    
    # Processa a lista de números
    processar_lista(numeros)

if __name__ == "__main__":
    main()
