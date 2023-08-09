def numeros_pares(lista_numeros):
    return [numero for numero in lista_numeros if numero % 2 == 0]

# Exemplo de uso da função
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares_resultado = numeros_pares(numeros)
print("Números pares na lista:", numeros_pares_resultado)
