from time import sleep
distancia=float(input("Qual a distancia da viagem? "))
print("Carregando....")
sleep(3)
preco=distancia*0.50 if distancia<=200 else distancia*0.75
print(f"O preço da passagem vai ser {preco:.2f}")
