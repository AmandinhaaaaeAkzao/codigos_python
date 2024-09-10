# Função para calcular o imposto de renda
def calcular_imposto(salario):
    if salario <= 1900:
        return 0
    elif 1901 <= salario <= 2800:
        return salario * 0.075
    elif 2801 <= salario <= 3700:
        return salario * 0.15
    else:
        return salario * 0.225

# Leitura do salário
salario = float(input("Digite o salário: R$ "))

# Cálculo e exibição do imposto
imposto = calcular_imposto(salario)
print(f"O imposto de renda devido é: R$ {imposto:.2f}")

