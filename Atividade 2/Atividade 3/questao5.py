# Função para calcular o pagamento total
def calcular_pagamento(horas_trabalhadas, valor_por_hora):
    horas_normais = min(horas_trabalhadas, 40)  # Horas trabalhadas até 40 são normais
    horas_extras = max(horas_trabalhadas - 40, 0)  # Horas trabalhadas acima de 40 são extras

    pagamento_normal = horas_normais * valor_por_hora
    pagamento_extra = horas_extras * valor_por_hora * 1.5  # Bônus de 50% para horas extras

    return pagamento_normal + pagamento_extra

# Leitura da quantidade de horas trabalhadas e valor por hora
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: R$ "))

# Cálculo do pagamento total
pagamento_total = calcular_pagamento(horas_trabalhadas, valor_por_hora)

# Exibição do pagamento total
print(f"O pagamento total é: R$ {pagamento_total:.2f}")

