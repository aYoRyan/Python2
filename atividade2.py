def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0  # Retorna 0 para evitar divisão por zero caso a lista esteja vazia
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media

# Exemplo de uso da função
numeros = [10, 20, 30, 40, 50]
media_resultado = calcular_media(numeros)
print("A média dos valores é:", media_resultado)
