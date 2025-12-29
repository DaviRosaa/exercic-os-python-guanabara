print("Banco DEV")
valor = int(input("Qual valor voçê quer sacar? R$"))
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced                        #Primeira forma com Substração
        total_ced += 1
    else:
        if total_ced > 0:
            print(f"O total de {total_ced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
