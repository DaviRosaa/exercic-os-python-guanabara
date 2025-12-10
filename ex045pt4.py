from time import sleep
from random import randint
escolhas = ("Pedra","Papel","Tesoura")
computador = randint(0,2)
jogador=int(input("Suas opções\n [0]Pedra\n [1]Papel\n [2]Tesoura\n Qual é sua jogada? "))
print(f"") #genial
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
if jogador != 0 and jogador != 1 and jogador != 2:
    print("Código invalído")
else:
    print(f"{'-=-' * 11}\nA sua escolha foi: {escolhas[jogador]}\nA escolha do computador foi: {escolhas[computador]}\n{'-=-' * 11}")  # genial
    if computador == 0:
        if jogador == 0:
            print("EMPATE!")
        elif jogador == 1:
            print("Voçê venceu!")
        elif jogador == 2:
            print("Computador Ganhou!")
    if computador == 1:
        if jogador == 1:
            print("Empate!")
        elif jogador == 2:
            print("Você venceu!")
        elif jogador == 0:
            print("Computador Ganhou!")
    if computador == 2:
        if jogador == 0:
            print("Voçê venceu!")
        elif jogador == 1:
            print("Computador Venceu!")
        elif jogador == 2:
            print("Empate!")