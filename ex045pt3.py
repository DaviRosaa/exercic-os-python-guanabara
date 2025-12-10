from random import randint
jogada=input("Escolha uma jogada\n [1] PEDRA\n [2] PAPEL\n [3] TESOURA\nQual é sua jogada? ")
computador=randint(1,3)
if jogada == "1":
    escolha1 = "pedra"
    print(f"A sua escolha foi: {escolha1}")
elif jogada == "2":
    escolha1 = "papel"
    print(f"A sua escolha foi: {escolha1}")
elif jogada == "3":
    escolha1 = "tesoura"
    print(f"A sua escolha foi: {escolha1}")



if computador == 1:
    escolha = "pedra"
    print(f"A escolha do computador foi {escolha}")
elif computador == 2:
    escolha = "papel"
    print(f"A escolha do computador foi {escolha}")
elif computador == 3:
    escolha = "tesoura"
    print(f"A escolha do computador foi {escolha}")

if (jogada == "1" and computador == 3 or
    jogada == "2" and computador == 1 or  #GENIAL
    jogada == "3" and computador == 2):
    print("Você Ganhou!")
elif (jogada == "1" and computador == 1 or
    jogada == "2" and computador == 2 or    #GENIAL
    jogada == "3" and computador == 3):
    print("EMPATE!")
else:
    print("Você perdeu!")
