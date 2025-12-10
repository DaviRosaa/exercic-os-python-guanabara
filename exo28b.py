from random import randint
from time import sleep

print("-=-"*20)
print("Vou pensar em um número de 0 a 5, tente adivinhar....")
print("-=-"*20)
numero=int(input("Em que número pensei: "))
print("processando.....")
sleep(3)
numero1=randint(0,5)
if numero==numero1:
    print("parabéns voçê acertou")
else:
    print("Parabéns você errou")
print(numero1)