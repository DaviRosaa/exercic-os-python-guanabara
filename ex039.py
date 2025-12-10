ano=int(input("Em que ano voçê nasceu? ").strip())
ano1=2025-ano
alistamento="batata"
ano2=ano1-18
ano3=18-ano1
if ano1>18:
    alistamento=f"Já passou do tempo de alistamento: \033[31m{ano2}\033[m anos"
    print(f"O ano que você deveria ter se alistado era \033[31m{2025-ano2}\033[m")
elif ano1==18:
    alistamento="Voçê vai se alistar neste ano dê 2025"
else:
    alistamento=f"Voçe ainda não vai se alistar: \033[32m{ano3}\033[m anos para se alistar"
    print(f"O ano que você vai se alistar é: \033[32m{2025+ano3}\033[m")
print(alistamento)


