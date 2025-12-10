salario=float(input("Será dado um aumento para cada funcionário. Com base de cada salário individual.\nQual o seu salário? "))
aumento=salario>1250
aumento2=salario<=1250
if salario>=1250:
    novo_salario=salario+(salario*0.10)
else:
     novo_salario=salario+(salario*0.15)
print(f"Seu salário reajustado foi dê: {novo_salario:.2f}")
