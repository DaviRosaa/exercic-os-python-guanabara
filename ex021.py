numero=int(input("Digite um número para ser convertido "))
conversao=input("1 para binário 2 para octal e 3 para hexadecimal: ")
binario=bin(numero).replace("0b","")
octal=oct(numero).replace("0o","")
hexadecimal=hex(numero).replace("0x","")

if conversao=="1":
    print(f"O seu número convertido em binário, ficou: {binario}")
    if conversao=="2":
        print(f"O seu número convertido em octal, ficou:  {octal}")
    if conversao=="3":
        print(f"O seu número convertido em hexadecimal, ficou: {hexadecimal}")
    else:
        print("Código invalído")
#Tecníca para retirar o: 0b, 0o e 0x. Que achei muito ótima e valída.
#Usuarío @joaomatheus7081