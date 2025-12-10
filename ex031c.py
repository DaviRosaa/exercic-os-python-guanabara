distancia=float(input("Qual a distancia da viagem? "))
if distancia<=200:
    distancia1=distancia*0.50
else:
    distancia1=distancia*0.45
print(f"A sua passagem ficou {distancia1}")