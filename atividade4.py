def e_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")  # Convertendo para minúsculas e removendo espaços
    return palavra == palavra[::-1]

# Exemplo de uso da função
palavra_exemplo = "arara"
if e_palindromo(palavra_exemplo):
    print(f"{palavra_exemplo} é um palíndromo!")
else:
    print(f"{palavra_exemplo} não é um palíndromo.")
