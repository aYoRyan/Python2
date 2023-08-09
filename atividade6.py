import random

def lancar_dado():
    return random.randint(1, 6)

# Simulação do lançamento de dois dados e cálculo da soma
dado1 = lancar_dado()
dado2 = lancar_dado()
soma = dado1 + dado2

# Impressão dos resultados
print(f"Lançamento do dado 1: {dado1}")
print(f"Lançamento do dado 2: {dado2}")
print(f"Soma dos valores obtidos: {soma}")
