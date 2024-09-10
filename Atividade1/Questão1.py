#Calcular e apresentar o valor do volume de uma caixa retangular, utilizando a
#fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA.

comprimento = float(input("Informe seu comprimento:" ))
largura = float(input("Informe seu largura:" ))
altura = float(input("Informe sua altura:" ))

volume = (comprimento * largura * altura)

print(f"Seu volume é {volume:.2f}")