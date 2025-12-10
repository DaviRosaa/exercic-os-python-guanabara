total_idade = 0
contador_menor = 0

mais_velho_idade = 0
mais_velho_sexo = ""

for pessoa in range(1,5):
    print(f"{'-'*5} {pessoa}ª pessoa {'-'*5}")


    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ")

    total_idade = total_idade + idade

    # Descobre o mais velho
    if idade > mais_velho_idade:
        mais_velho_idade = idade
        mais_velho_sexo = sexo.upper()  # salva M ou F

    # Conta menores
    if idade < 20:
        contador_menor += 1

# Descobrir frase do sexo do mais velho
if mais_velho_sexo == "M":
    frase_velho = "O homem mais velho tem"
else:
    frase_velho = "A mulher mais velha tem"


print(f"\nA média de idade do grupo é {total_idade / 4:.1f}")
print(f"{frase_velho} {mais_velho_idade} anos")
print(f"Ao todo são {contador_menor} pessoas menores de 20 anos")
