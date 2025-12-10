idade_total = 0
idade_do_mais_velho = 0
nome_do_mais_velho = ""
contador_mulheres = 0
for pessoa in range(1,5):
    print(f"======{pessoa}ª pessoa======")
    nome = input("Nome: ")
    idade = int(input("idade: "))
    idade_total = idade_total + idade
    sexo = input("Sexo [M/F]: ").upper()

    if sexo == "M":
        if idade > idade_do_mais_velho:
            idade_do_mais_velho = idade
            nome_do_mais_velho = nome

    if sexo == "F":
        if idade < 20:
            contador_mulheres += 1


print(f"A média de idade do grupo é {idade_total / 4:.2f} anos")
print(f"O homem mais velho é {nome_do_mais_velho} e tem {idade_do_mais_velho} anos ")
print(f"Ao todo {contador_mulheres} é a quantidade de mulheres que tem menos de 20 anos")
