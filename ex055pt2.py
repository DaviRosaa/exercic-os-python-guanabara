peso_maximo = None
peso_minimo = None

for pessoa in range(1, 6):
    peso = float(input(f"Peso da {pessoa}ª pessoa: "))

    # Se ainda não existe um maior peso, esse é o primeiro
    if peso_maximo is None or peso > peso_maximo:
        peso_maximo = peso

    # Se ainda não existe um menor peso, esse é o primeiro
    if peso_minimo is None or peso < peso_minimo:
        peso_minimo = peso

print(f"O maior peso lido foi {peso_maximo}")
print(f"O menor peso lido foi {peso_minimo}")
