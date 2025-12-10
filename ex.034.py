salario=float(input("Qual o salário? "))
if salario > 1250:
    novo_salario = salario + (salario * 10 / 100)
else:
    novo_salario = salario + (salario * 15 / 100)

print(f"Seu novo salário é R$ {novo_salario:.2f}")