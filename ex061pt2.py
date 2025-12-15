print("Gerador de PA\n-=-=-=-=-=-")
a1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = a1
cont = 1
while cont <= 10:
    termo += razao
    print(termo,end=" ")
    cont = cont + 1