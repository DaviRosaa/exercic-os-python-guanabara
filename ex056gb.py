idade_total = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
contador_mulheres = 0
for pessoa in range(1,5):
    print(f"===== {pessoa}ª pessoa =====")
    nome = input("Nome:")
    idade = int(input("idade: "))
    idade_total += idade
    sexo = input("Sexo: ")
    if pessoa == 1 and sexo in "Mm":
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if  sexo in "Mm" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo in "Ff" and idade < 20:
        contador_mulheres += 1

print(f"A média da idade do grupo todo é {idade_total / 4:.2f}")
print(f"O nome do homem mais velho é {nome_homem_mais_velho} e a idade dele é {idade_homem_mais_velho}")
print(f"Existem {contador_mulheres} mulheres com menos de 20 anos")






