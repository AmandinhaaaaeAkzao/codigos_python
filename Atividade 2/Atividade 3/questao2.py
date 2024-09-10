# Função para verificar se um ano é bissexto
def is_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

# Leitura do ano
ano = int(input("Digite um ano: "))

# Verificação e saída do resultado
if is_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
