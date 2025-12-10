from math import hypot
cateto_adjacente=float(input("Digite o valor do primeiro cateto"))
cateto_agudo=(float(input("Digite o valor do segundo cateto")))
hipotenusa=hypot(cateto_adjacente,cateto_agudo)
print(f"A hipotenusa é: {hipotenusa:.2f}")
