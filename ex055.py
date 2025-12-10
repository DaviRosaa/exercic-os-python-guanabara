peso_maximo = 0
peso_minimo = 650
for pessoa in range(1,6):
    peso = float(input(f"Peso da {pessoa}ª pessoa: "))
    peso_maximo = max(peso,peso_maximo)
    peso_minimo = min(peso,peso_minimo)
print(f"O maior peso lido foi {peso_maximo}\nO menor peso lido foi {peso_minimo}")