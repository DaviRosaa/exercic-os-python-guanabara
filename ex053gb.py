frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''


for letra in range(len(junto) -1, -1, -1):# começa no fim, vai até 0 e anda ao contrário.
    print(junto[letra],end="")
    inverso += junto[letra]

print(f" O inverso é {inverso}")
if inverso == junto:
    print("Isso é um palíndromo")
else:
    print("Isso não é um palíndromo")
