print("BANCO CEV\n")
contador = contador2 = contador3 = contador4 = 0
valor = int(input("Qual valor voçê quer sacar? R$"))
while True:
    if valor % 50 == 0:
        contador += 1
        print(f"Total de {contador} cédulas de R$50")
    if valor % 20 == 0:
        contador2 += 1
        print(f"Total de {contador2} cédulas de R$20")
    if valor % 10 == 0:
        contador3 += 1
        print(f"Total de {contador3} cédulas de R$10")
    if valor % 1 == 0:
        contador4 += 1
        print(f"Total de {contador4} cédulas de R$1")
        break










