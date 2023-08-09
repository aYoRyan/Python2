def contar_ocorrencias_palavras(texto):
    # Remover caracteres indesejados e dividir o texto em palavras
    palavras = texto.lower().split()
    
    # Criar um dicionário para armazenar as ocorrências de cada palavra
    ocorrencias = {}
    
    # Contar as ocorrências de cada palavra
    for palavra in palavras:
        ocorrencias[palavra] = ocorrencias.get(palavra, 0) + 1

    return ocorrencias

# Exemplo de uso do programa
texto = input("Digite o texto: ")
ocorrencias_palavras = contar_ocorrencias_palavras(texto)

# Imprimir o resultado
print("Ocorrências de cada palavra:")
for palavra, ocorrencias in ocorrencias_palavras.items():
    print(f"{palavra}: {ocorrencias}")