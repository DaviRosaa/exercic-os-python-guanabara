from datetime import date
ano=int(input("Qual ano você quer saber se é bissexto?"))
if ano==0:
    ano=date.today().year
    print(ano)
if ano%4==0 and ano%100!=0 or ano%400==0:
    bissexto="É bissexto"
else:
    bissexto="Não é bissexto"
print(f"O ano: {bissexto}")