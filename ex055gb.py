maior_peso = 0
menor_peso = 650
for pessoa in range(1,6):
    peso = float(input(f"Peso da {pessoa}ª pessoa: "))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso      # O maior começa sendo o primeiro valor.

                            # Depois cada novo valor tenta tomar o lugar dele.
    else:
        if peso > maior_peso:
            maior = peso
        if peso < menor_peso:
            menor = peso
print(f"O maior peso lido foi dê {maior_peso} ")
print(f"O menor peso lido foi dê {menor_peso} ")