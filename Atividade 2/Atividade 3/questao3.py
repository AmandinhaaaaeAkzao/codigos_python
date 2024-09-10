# Função para classificar a idade
def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif 12 <= idade < 18:
        return "Adolescente"
    elif 18 <= idade <= 60:
        return "Adulto"
    else:
        return "Idoso"

# Leitura da idade
idade = int(input("Digite a idade: "))

# Classificação e saída do resultado
categoria = classificar_idade(idade)
print(f"A pessoa é classificada como: {categoria}")

