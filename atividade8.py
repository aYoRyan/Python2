def encontrar_maior_menor_palavra(lista_palavras):
    if not lista_palavras:
        return None, None  # Retorna None se a lista estiver vazia

    maior_palavra = min(lista_palavras, key=len)
    menor_palavra = max(lista_palavras, key=len)

    return maior_palavra, menor_palavra

# Exemplo de uso do programa
numero_palavras = int(input("Digite o número de palavras na lista: "))

lista_palavras = []
for i in range(numero_palavras):
    palavra = input(f"Digite a palavra {i+1}: ")
    lista_palavras.append(palavra)

maior, menor = encontrar_maior_menor_palavra(lista_palavras)

if maior and menor:
    print(f"A maior palavra é: {maior}")
    print(f"A menor palavra é: {menor}")
else:
    print("A lista está vazia.")
