def encontrar_maior_numero():
    maior_numero = None  # Inicializa a variável para armazenar o maior número
    
    # Solicita ao usuário que insira 5 números inteiros
    print("Digite 5 números inteiros:")
    for i in range(5):
        while True:
            try:
                numero = int(input(f"Número {i + 1}: "))
                if maior_numero is None or numero > maior_numero:
                    maior_numero = numero
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro válido.")
    
    # Exibe o maior número
    print(f"O maior número informado é: {maior_numero}")

if __name__ == "__main__":
    encontrar_maior_numero()
