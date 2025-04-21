# Gerar um numero aleatorio
# Verificar se o usuario acertou
# Contabilizando as tentativas

import random

def jogo_advinhacao():
    print("Bem-vindo ao Jogo da Advinhação")
    print("Tente advinhar um número aleatório de 1 a 100!")

    # Gerar o numero aleatorio
    numero_secreto = random.randint(1, 100)

    # Inicializar variaveis que vao ajudar o sistema a contabilizar as jogadas
    tentativas = 0
    acertou = False

    while not acertou:

        palpite = int(input("Digite o seu palpite: "))

        tentativas += 1

        # Verificar o palpite
        if palpite == numero_secreto:
            print(f"Parabéns, você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
            acertou = True
        elif palpite < numero_secreto:
            print("O Número secreto é maior. Tente novamente")
        else:
            print("O Número secreto é menor. Tente novamente")

# Inicializar o programa
if __name__ == "__main__":
    jogo_advinhacao()

# Tentativas maximas
# Que sao deduzidas a cada tentativa
# E quando acaba da um game over