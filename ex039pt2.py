from datetime import date
atual_ano=date.today().year
sexo=str(input("Voçê é homem ou mulher? "))
nascimento="batata"
if sexo=="homem" or sexo=="Homem" or sexo=="HOMEM": #também poderia ser usado sexo.lower()
    nascimento=int(input("Digite o seu ano de nascimento: "))
elif sexo=="mulher" or sexo=="Mulher" or sexo=="MULHER": #também poderia ser usado sexo.lower()
    print("Voçê não precisa fazer alistamento militar")
    exit()
else:
    print("Sexo invalído")
    exit()
ano1=atual_ano-nascimento
ano2=18-ano1
ano3=atual_ano-18
ano4=ano1-18
if ano1<18:
    print(f"Voçê vai se alistar daqui {ano2} anos")
    print(f"O ano que você irá se alistar vai ser {atual_ano+ano2} ")
elif ano3>18:
    print(f"Já passou do tempo de alistamento: {ano4}")
    print(f"O ano que voçê deveria ter se alistado era {nascimento+18}")
else:
    print(f"voçê tem que alistar no atual ano de {atual_ano}. Vá IMEDIATAMENTE")
