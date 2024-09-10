# Recebe o sexo e o peso da pessoa
sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")
peso = float(input("Digite o peso da pessoa (em kg): "))

# Calcula o peso ideal com base no sexo
if sexo == 'M':
    peso_ideal = (72.7 * peso) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * peso) - 44.7
else:
    peso_ideal = None
    print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")

# Mostra o peso ideal se o sexo for válido
if peso_ideal is not None:
    print(f"O peso ideal para uma pessoa do sexo {sexo} com peso {peso} kg é: {peso_ideal:.2f} kg")

    

