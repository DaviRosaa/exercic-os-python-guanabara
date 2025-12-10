from random import randint
from time import sleep
print(f"{("-=-"*20)}\n Vou pensar em um número de 0 a 5. Tente adivinhar.....\n{("-=-"*20)}")
n=randint(0,5)

numero_sorteado=int(input("Qual o número de 0 a 5 que vai ser sorteado? "))
print("carregando.....")
sleep(3)
if numero_sorteado==n:
    print(f"Parabens você acertou: {n}")
else:
    print(f"Parabens você errou: {n}")