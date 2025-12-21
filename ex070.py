print("DIGA O NOME DOS PRODUTOS!\n")
soma = 0
acumulador = 0
menor_preco = None
while True:
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Qual o preço do produto: "))
    opcao = str(input("Quer continuar? [S/N]: ").upper())
    if preco is None or preco < menor_preco:
        menor_preco = preco
        print(f"O produto mais barato tem o nome dê {nome} e custa {menor_preco}R$")
    soma += preco
    if preco > 1000:
        acumulador += 1
    if opcao == "N":
        break
print(f"O total do gasto da compra foi: {soma}\n{acumulador} custam mais de mil reais")

