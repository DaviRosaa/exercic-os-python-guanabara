ano=int(input("Em que ano você está: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Esse ano é ano bissexto")
else:
    print("Esse ano não em um ano bissexto")

