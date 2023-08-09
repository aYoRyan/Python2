def calcular_mediana(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    tamanho_lista = len(lista_ordenada)

    if tamanho_lista % 2 == 1:  # Se a lista tem tamanho ímpar
        mediana = lista_ordenada[tamanho_lista // 2]
    else:  # Se a lista tem tamanho par
        indice1 = tamanho_lista // 2 - 1
        indice2 = tamanho_lista // 2
        mediana = (lista_ordenada[indice1] + lista_ordenada[indice2]) / 2

    return mediana

# Exemplo de uso da função
numeros = [12, 7, 3, 21, 15, 9, 6]
mediana_resultado = calcular_mediana(numeros)
print("A mediana dos valores é:", mediana_resultado)
