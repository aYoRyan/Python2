def celsius_pro_fahren(celsius):
    return (celsius * 9/5) + 32

def fahren_pro_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função para escolher a conversão
def escolher_conversao():
    print("Escolha o bagulho:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    opcao = int(input("Digite o número da opção desejada: "))
    return opcao

# funncaozada
def main():
    opcao = escolher_conversao()

    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_pro_fahren(celsius)
        print(f"{celsius}°C equivale a {fahrenheit:.2f}°F.")
    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahren_pro_celsius(fahrenheit)
        print(f"{fahrenheit}°F equivale a {celsius:.2f}°C.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou utro ne pae.")



if __name__ == "__main__":
    main()
