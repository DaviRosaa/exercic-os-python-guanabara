usuario = 0
soma = 0
contador = 0
while usuario != 999:
    usuario = int(input("Digite um número inteiro[999 para parar]: "))
    if usuario == 999:
        break
    soma += usuario
    contador += 1

print(f"A soma de todos os números foi {soma} e quantidade de números foi: {contador}")