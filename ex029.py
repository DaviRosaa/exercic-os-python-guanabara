velocidade=float(input("Qual a velocidade por km que seu carro passou pelo radar? "))
valor=(float((velocidade-80)*7))
if velocidade>80:
    print(f"Voçe foi multado e sua multa foi no valor de R${valor:.2f}")
else:
    print("Tenha um bom dia! e dirija com segurança")
