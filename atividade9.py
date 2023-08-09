def palavras_em_maiusculas(lista_strings):
    return [palavra.upper() for palavra in lista_strings]

# Exemplo de uso da função
lista_exemplo = ["python", "é", "uma", "linguagem", "de", "programação"]
lista_maiusculas = palavras_em_maiusculas(lista_exemplo)
print(lista_maiusculas)
