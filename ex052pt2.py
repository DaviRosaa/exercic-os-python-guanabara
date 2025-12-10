n1 = int(input("Digite um número inteiro: "))
contador = 0
for c in range(1,n1+1):
    if n1 % c == 0:
        contador = contador + 1
print(contador)
if contador > 2 or contador < 2:
    print(f"É um número que pode ser dividido por {contador} vezes \n E não é um número primo")
else:
    print(f"É um número que pode ser dividido por {contador} vezes \n E é um número primo")


