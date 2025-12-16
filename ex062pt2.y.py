print("Gerador de PA")
a1 = int(input("\nPrimeiro termo: "))
razao = int(input("Qual a razão? "))

cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais

    while cont <= total:
        termo = a1 + (cont - 1) * razao       #primeiro_termo + razão
        print(termo, end=" ")
        cont += 1

    mais = int(input("\nQuer mais quantos termos? "))

print("\nFim do programa!")