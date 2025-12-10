valor1=int(input("Primeiro valor: "))
valor2=int(input("Segundo valor: "))
valor3=int(input("Terceiro valor: "))
valor1_str=str(valor1)
valor2_str=str(valor2)
valor3_str=str(valor3)
if valor1_str>valor2_str and valor1_str>valor3_str:
    valor1="maior"
    print(f"O maior número foi: {valor1_str}")
if valor2_str>valor1_str and valor2_str>valor3_str:
    valor2="maior"
    print(f"O maior número foi: {valor2_str}")
if valor3_str>valor1_str and valor3_str>valor2_str:
    valor3="maior"
    print(f"O maior número foi: {valor3_str}")

    if valor1_str < valor2_str and valor1_str < valor3_str:
        valor1 = "menor"
        print(f"O menor número foi: {valor1_str}")
    if valor2_str < valor1_str and valor2_str < valor3_str:
        valor2 = "menor"
        print(f"O menor número foi: {valor2_str}")
    if valor3_str < valor1_str and valor3_str < valor2_str:
        valor3 = "menor"
        print(f"O menor valor foi {valor3_str}")

