from time import sleep
print("==========LOJAS GUANABARA==========")
produtos=float(input("Qual o preço das compras? R$").strip())
pagamento=input("formas de pagamento:\n[1] á vista dinheiro/cheque\n[2] á vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\n\n")
if pagamento=="1":
    print("Carregando....")
    sleep(2)
    print(f"{produtos-(produtos*0.1)}")
elif pagamento=="2":
    print("Carregando....")
    sleep(2)
    print(f"{produtos-(produtos*0.05)}")
elif pagamento=="3":
    print("Carregando....")
    sleep(2)
    print(f"{produtos}")
elif pagamento=="4":
    parcelas = int(input("Em Quantas parcelas vai ser? "))
    print("Carregando....")
    sleep(2)
    valor_parcela=(produtos/parcelas)*0.2
    print(f"O valor de cada parcela irá ficar {valor_parcela+(produtos/parcelas):.2f} e ao todo sua compra vai ficar: {produtos+(produtos*0.20)}")
else:
    print("Opção Inválida, tente novamente!")
    exit()
