# Percorre os números de 1 a 50
for i in range(1, 51):
    # Verifica se o número é múltiplo de 3 e 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Verifica se o número é múltiplo de 3
    elif i % 3 == 0:
        print("Fizz")
    # Verifica se o número é múltiplo de 5
    elif i % 5 == 0:
        print("Buzz")
    # Se não for múltiplo de 3 nem de 5, imprime o próprio número
    else:
        print(i)
