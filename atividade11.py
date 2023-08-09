import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        tentativa = int(input("Digite o seu palpite: "))
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            break
        elif tentativa < numero_secreto:
            print("O número secreto é maior. Tente novamente.")
        else:
            print("O número secreto é menor. Tente novamente.")

# Iniciar o jogo
jogo_adivinhacao()
