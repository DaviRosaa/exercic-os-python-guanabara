from random import randint
computador = randint(0,10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10")
print("Séra que você consegue adivinhar qual foi? ")
palpites = 1
acertou = False
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
print(f"Parabèns, você acertou! com {palpites} palpites")


