from random import randint
from time import sleep
print(f"{("-=-"*20)}\n Vou pensar em um número de 1 a 10. Tente adivinhar.....\n{("-=-"*20)}")
n = randint(1,10)
numero_sorteado=int(input("Qual o número de 1 a 10 que vai ser sorteado? "))
print("carregando.....")
sleep(3)
print(n)
contador = 1

while numero_sorteado != n:
    print("Tente mais uma vez.")
    numero_sorteado = int(input("Qual o seu palpite? "))
    contador += 1

if numero_sorteado == n:
    print("Parabens voçê acertou")
print(f"Número de tentativas: {contador}")

