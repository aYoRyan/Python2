def imprimir_numeros_naturais(N):
    if N < 0:
        print("Por favor, insira um número inteiro positivo.")
        return
    
    for i in range(N + 1):
        print(i)

# Solicita ao usuário para inserir o número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))
imprimir_numeros_naturais(numero)