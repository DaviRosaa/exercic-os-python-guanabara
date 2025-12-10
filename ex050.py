numeros = input("Digite seis números inteiros, separados por espaço: ").split()
soma = 0
for c in numeros:
    if int(c) % 2 == 0:
        soma = soma + int(c)
print(soma)