fatorial = int(input("Digite um número para\ncalcular seu fatorial: "))
multiplicador = 1
while fatorial > 0:
    if fatorial == 1:
        print(fatorial, end=" = ")
    else:
        print(fatorial, end=" x ")
    multiplicador = multiplicador * fatorial
    fatorial = fatorial - 1

print(multiplicador)




