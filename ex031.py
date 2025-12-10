distancia=float(input("Qual a distancia da viagem?"))
viagens_curtas=(float(0.50*distancia))
viagens_longas=(float(0.45*distancia))
if distancia<=200:
    print(f"O valor da passagem vai ficar: R${viagens_curtas:.2f}")
else:
    print(f"O valor da passagem vai ficar: R${viagens_longas:.2f}")