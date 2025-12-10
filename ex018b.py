cateto_oposto=(float(input("Digite o valor do cateto oposto")))
cateto_adjacente=(float(input("Digite o valor do cateto adjacente")))
hipotenusa_incompleta=cateto_oposto**2+cateto_adjacente**2
hipotenusa=hipotenusa_incompleta**(1/2)
print(str(f"A hipotenusa deste triangulo é {hipotenusa:.2f}"))
seno=cateto_oposto/hipotenusa
cosseno=cateto_adjacente/hipotenusa
tangente=cateto_oposto/cateto_adjacente
print(f"O seno é {seno:.2f} o cosseno é {cosseno:.2f} e a tangente {tangente:.2f}")