frase = str(input("Digite uma frase: ").strip().upper())
frase1=frase.replace(" ","")
print(frase1[::-1])
if frase1 == frase1[::-1]: # O slice padrão é da esquerda para direita. Se quiser ler da direita para esquerda use -1 no passo
    print("é um palíndromo")
else:
    print("Não é um palíndromo")
