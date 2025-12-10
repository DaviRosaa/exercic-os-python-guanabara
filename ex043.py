print("Calculadora de IMC")
peso=float(input("Qual o seu peso (kg)?"))
altura=float(input("Qual a sua altura?"))
imc=float(f"{peso/(altura**2)}")
print(f"seu imc é {imc:.1f}")
if imc < 18.5:
    print("Abaixo do seu peso ideal")
elif 18.5 <= imc < 25: #Se o mínimo é A e o máximo é B:
    print("peso ideal")
elif 25 <= imc <= 30: #Se o mínimo é A e o máximo é B:                                     < se o da direita for maior
                                                                                          #> se o da direita for menor
    print("sobre peso")
elif 30 <= imc < 40: #Se o mínimo é A e o máximo é B:
    print("Obesidade")
elif imc > 40:
    print("Obesidade mórbida")