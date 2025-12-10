from datetime import date
atual=date.today().year
print("Confederação Nacional da natação")
ano=int(input("Em que ano você nasceu? ").strip())
confederacao=atual-ano
if confederacao <= 9:
    print(f"O atleta tem \033[34m{confederacao}\033[manos")
    print("Classificação: Mirim")
elif confederacao <= 14:
    print(f"O  atleta tem \033[34m{confederacao}\033[m anos")
    print("Classificação: infantil")
elif confederacao <= 19:
    print(f"O atleta tem \033[34m{confederacao}\033[m anos")
    print("Classificação: Junior")
elif confederacao <= 20:
    print(f"O atleta tem \033[34m{confederacao}\033[m anos")
    print("Classificação: Senior")
else:
    print(f"O atleta tem \033[34m{confederacao}\033[m anos")
    print("Classificação: Master")