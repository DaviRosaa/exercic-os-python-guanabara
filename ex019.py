import random
nome1=(str(input("Primeiro Aluno:")))
nome2=(str(input("Segundo Aluno:")))
nome3=(str(input("Terceiro Aluno:")))
nome4=(str(input("Quarto Aluno:")))
lista=[nome1,nome2,nome3,nome4]
print(f"O nome sorteado foi \033[35m{random.choice(lista)}\033[m")