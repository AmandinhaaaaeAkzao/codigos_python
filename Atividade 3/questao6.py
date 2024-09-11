def verificar_numero_perfeito(n):
    if n <= 1:
        return False
    
    soma_divisores = 0
    
    # Calcula a soma dos divisores próprios positivos
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    
    # Verifica se o número é perfeito
    return soma_divisores == n

def main():
    try:
        # Recebe um número inteiro do usuário
        numero = int(input("Digite um número inteiro: "))
        
        # Verifica se o número é perfeito
        if verificar_numero_perfeito(numero):
            print(f"O número {numero} é um número perfeito.")
        else:
            print(f"O número {numero} não é um número perfeito.")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
