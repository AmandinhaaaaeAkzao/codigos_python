# Função para verificar se o aluno foi aprovado
def verificar_aprovacao(nota_final, frequencia):
    if nota_final >= 7 and frequencia >= 75:
        return "Aprovado"
    else:
        return "Reprovado"

# Leitura da nota final e da frequência
nota_final = float(input("Digite a nota final do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

# Verificação e exibição do resultado
resultado = verificar_aprovacao(nota_final, frequencia)
print(f"O aluno foi: {resultado}")
