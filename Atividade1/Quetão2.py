#Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a
#fórmula: VOLUME = 3.14159 * R2 * ALTURA.

raio = float(input("Informe seu raio: "))
altura = float(input("Informe sua altura: "))

volume = (3.14159 * raio * 2 * altura)

print(f"Seu volume é {volume:.2f}")