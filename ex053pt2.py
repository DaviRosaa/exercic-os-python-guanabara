frase = input("Digite uma frase: ").upper().strip()
frase_junta = frase.replace(" ","")
inverso = ""
for c in frase_junta[::-1]:
    inverso = inverso + c
print(inverso)
if frase_junta == inverso:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")




