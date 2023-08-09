def encontrar_maior_menor_numero(sequencia_numeros):
    if not sequencia_numeros:
        return None, None  # Retorna None se a sequência estiver vazia

    maior_numero = max(sequencia_numeros)
    menor_numero = min(sequencia_numeros)

    return maior_numero, menor_numero

# Exemplo de uso do programa
sequencia_numeros = input("Digite uma sequência de números separados por espaço: ")
lista_numeros = [int(numero) for numero in sequencia_numeros.split()]

maior, menor = encontrar_maior_menor_numero(lista_numeros)

if maior and menor:
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
else:
    print("A sequência está vazia.")
