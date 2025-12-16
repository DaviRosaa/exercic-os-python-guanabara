print("Gerador de PA\n-=-=-=-=-=-")
a1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

termo = a1
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais

    while cont <= total:
        print(termo, end=" ")
        termo += razao
        cont += 1

    mais = int(input("\nQuer mais quantos termos? "))

print("\nFim do programa!")
