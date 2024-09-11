import random

def simular_lancamentos():
    # Inicializa um dicionário para contar as ocorrências de cada número
    contagem = {i: 0 for i in range(1, 7)}
    
    # Simula 10 lançamentos de dados
    print("Lançamentos dos dados:")
    for _ in range(10):
        resultado = random.randint(1, 6)  # Sorteia um número entre 1 e 6
        print(resultado, end=' ')
        contagem[resultado] += 1
    
    print("\nContagem dos resultados:")
    
    # Exibe a contagem de cada número
    for numero, quantidade in contagem.items():
        print(f"Número {numero}: {quantidade} vez(es)")

if __name__ == "__main__":
    simular_lancamentos()
