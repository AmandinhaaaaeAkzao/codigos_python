def contar_multiplos(a, b):
    # Contador para múltiplos de 7 e 11
    contador = 0

    # Itera sobre o intervalo [a, b] (inclusive)
    for numero in range(a, b + 1):
        if numero % 7 == 0 and numero % 11 == 0:
            contador += 1
    
    return contador

def main():
    try:
        # Solicita ao usuário dois números inteiros positivos
        a = int(input("Digite o primeiro número inteiro positivo (a): "))
        b = int(input("Digite o segundo número inteiro positivo (b): "))

        # Verifica se os números são positivos e se a é menor ou igual a b
        if a <= 0 or b <= 0:
            print("Os números devem ser inteiros positivos.")
        elif a > b:
            print("O primeiro número deve ser menor ou igual ao segundo número.")
        else:
            # Conta os múltiplos de 7 e 11 no intervalo [a, b]
            total_multiplos = contar_multiplos(a, b)
            print(f"Total de números entre {a} e {b} que são múltiplos de 7 e 11: {total_multiplos}")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros válidos.")

if __name__ == "__main__":
    main()
