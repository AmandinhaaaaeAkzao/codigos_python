#Receber o valor do salário 
salario = float(input("Digite o valor do salário: "))
financiamento = float (input("Digite o valor do financiamento pretendido: "))

# Verificar se o financiamento é menor ou igual a 5 vezes o salário 
if financiamento <= 5 * salario: 
    print ("Financiamento concedido")

else: 
    print ("Financiamento negado")

#Mensal final 
print ("Obrigado por nos consultar")
