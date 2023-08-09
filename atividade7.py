def fatorial(numero):
    if numero < 0:
        return None  # Fatorial de números negativos não está definido
    elif numero == 0:
        return 1  # Fatorial de 0 é 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Exemplo de uso da função
numero = int(input("Digite um número inteiro: "))
resultado_fatorial = fatorial(numero)

if resultado_fatorial is not None:
    print(f"O fatorial de {numero} é: {resultado_fatorial}")
else:
    print("O fatorial de números negativos não está definido.")
