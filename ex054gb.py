import datetime
maior = 0
menor = 0
ano_atual = datetime.date.today().year
for pessoas in range(1,8):
    nascimento = input(f"Em que ano a {pessoas}ª pessoa nasceu? ")
    if (ano_atual - int(nascimento) ) >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print(f"Exatamente {maior} são maiores de idade e exatamente {menor} são menores de idade")


