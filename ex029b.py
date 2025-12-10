velocidade=float(input("Qual a velocidade atual do carro?"))
velocidade_permitida=(float(velocidade-80)*7)
print("tenha um bom dia")
if velocidade<=80:
    print(f"Voçê foi multado no valor de {velocidade_permitida}")