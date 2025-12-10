nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite sua segunda nota: "))
media=(nota1+nota2)/2
if media>7:
    media1="passou de ano"
else:
    media1="não passou de ano"
print(f"Sua média foi {media} e voçê {media1}")