from random import sample as embaralhamento
nome1=(input("Digite o nome do aluno"))
nome2=(input("Digite o nome do aluno"))
nome3=(input("Digite o nome do aluno"))
nome4=input("Digite o nome do aluno")
lista=[nome1,nome2,nome3,nome4]
ordem=embaralhamento(lista, 4)
print(f"A ordem de embaralhamento foi:"," ".join(ordem))
