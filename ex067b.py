cont = 0
while True:
    usuario = int(input("Digite um número inteiro: "))
    for c in range(1, 11):
        cont += 1
        print(f"{usuario} x {cont} = {usuario * cont}")
    if usuario < 0:
        print("Programa encerrado")
        break