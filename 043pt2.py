peso=float(input("Qual o seu peso? ").strip())
altura=float(input("Qual a sua altura? ").strip())
imc=peso/(altura**2)
print(f"O seu imc é dê: {imc:.1f}.", end=" ")
if imc < 18.5:
    print("E voçê está abaixo do seu peso ideal")
elif 18.5 <= imc < 25:
    print("E voçê está no seu peso ideal")
elif 25 <= imc < 30:
    print("E voçê está sobrepeso")
elif 30 <= imc < 40:
    print("E voçê está obeso")
else:
    print("E voçê está em obesidade mórbida")