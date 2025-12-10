n1 = int(input("Digite um número inteiro: "))
contador = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        contador = contador + 1
if 2 > contador < 2:
    print("Não é um número primo")
else:
    print("É um número primo")

