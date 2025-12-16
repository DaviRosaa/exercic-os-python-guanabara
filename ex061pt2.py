print("Gerador de PA\n-=-=-=-=-=-")
a1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

termo = a1
cont = 1



while cont <= 10:
    print(termo, end=" ")
    termo += razao
    cont += 1



print("\nFim do programa!")


