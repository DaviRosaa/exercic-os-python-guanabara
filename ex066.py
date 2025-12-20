usuario = 0
soma = 0
contador = 0
while usuario != 999:
    usuario = int(input("Digite um número inteiro: "))
    if usuario == 999:
        break
    soma += usuario
    contador += 1
