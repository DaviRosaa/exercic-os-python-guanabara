contador = 0
n1 = int(input("Digite um número: "))
for c in range(1,n1+1):
        if n1 % c == 0:
            contador = contador + 1
print(contador)
if contador == 2:
    print("Número primo")
else:
    print("Não é número primo")


