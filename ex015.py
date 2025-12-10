dias=int(input("Quanto dias ele foi alugado?"))
km=float(input("Digite a quantidade de km's percorridos pelo carro"))
valor_dias=dias*60
valor_km=(km*0.15)
valor_total=valor_dias+valor_km
print(f"O total a pagar é de \033[33m{valor_total:.2f}\033[m")