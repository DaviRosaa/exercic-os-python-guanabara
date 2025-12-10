fatorial = int(input("Digite um número para\ncalcular seu fatorial: "))
multiplicador = 1
for c in range(fatorial,0,-1):
    print(end = "")
    if c >  1:
        print(" x ", end= "")
    multiplicador = multiplicador * c
print(f" = {multiplicador}")

