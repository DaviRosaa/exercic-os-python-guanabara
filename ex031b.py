distancia=float(input("Qual a distancia da viagem? "))
distancia_maior=distancia*0.45
distancia_menor=distancia*0.50
if distancia<=200:
    print(f"O preço da passagem irá ser menor: {distancia_menor:.2f}")
else:
    print(f"O preço da passagem irá ser maior: {distancia_maior:.2f}")
