from time import sleep
from random import randint

escolhas = ("Pedra","Papel","Tesoura")
computador = randint(0,2)

entrada = input("Suas opções\n [0]Pedra\n [1]Papel\n [2]Tesoura\n Qual é sua jogada? ")

# ---- validação de número ----
if not entrada.isnumeric() :
    print("Código inválido")
else:
    jogador = int(entrada)

    print()
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")

    if jogador < 0 or jogador > 2:
        print("Código inválido")
    else:
        print(f"{'-=-' * 11}")
        print(f"A sua escolha foi: {escolhas[jogador]}")
        print(f"A escolha do computador foi: {escolhas[computador]}")
        print(f"{'-=-' * 11}")

        if computador == 0:
            if jogador == 0:
                print("EMPATE!")
            elif jogador == 1:
                print("Você venceu!")
            elif jogador == 2:
                print("Computador ganhou!")

        if computador == 1:
            if jogador == 1:
                print("EMPATE!")
            elif jogador == 2:
                print("Você venceu!")
            elif jogador == 0:
                print("Computador ganhou!")

        if computador == 2:
            if jogador == 0:
                print("Você venceu!")
            elif jogador == 1:
                print("Computador venceu!")
            elif jogador == 2:
                print("EMPATE!")
