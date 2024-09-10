somar_pesos = 0
somar_idades = 0

for contador in range(5):
    peso = float (input("Informe seu peso {contador+1}: "))
    idade = int (input("Informe sua idade{contador+1}: "))

    somar_pesos = somar_pesos + peso 
    somar_idades = somar_idades + idade 


print(f"A média de pesos do time é {soma_pesos/5}")
print(f"A média de idade do time é {somar_idades/5}")


