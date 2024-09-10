# Função para calcular o valor da parcela e o valor total
def calcular_valores(valor_compra, parcelas):
    # Verifica se o número de parcelas está dentro do intervalo permitido
    if parcelas < 1 or parcelas > 24:
        return "Número de parcelas deve estar entre 1 e 24."
    
    taxa_juros = 0.015  # Taxa de juros de 1.5% ao mês

    if parcelas > 12:
        # Calcular o valor final da compra com juros
        valor_final = valor_compra * (1 + taxa_juros) ** parcelas
    else:
        # Sem juros
        valor_final = valor_compra

    # Calcular o valor da parcela
    valor_parcela = valor_final / parcelas

    return valor_final, valor_parcela

# Leitura do valor da compra e do número de parcelas
valor_compra = float(input("Digite o valor da compra: R$ "))
parcelas = int(input("Digite a quantidade de parcelas (1 a 24): "))

# Cálculo dos valores
resultado = calcular_valores(valor_compra, parcelas)

# Exibição dos resultados
if isinstance(resultado, tuple):
    valor_final, valor_parcela = resultado
    print(f"Valor total a ser pago: R$ {valor_final:.2f}")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
else:
    print(resultado)
