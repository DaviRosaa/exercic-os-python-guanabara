n1=int(input("\033[34mDigite um número\033[m").strip())
n2=f"\033[34m{n1*2}\033[m"
n3=f"\033[33m{n1*3}\033[m"
n4=n1**(1/2) #para se fazer uma raiz, deve se colocar o sinal de potència, após colocar (1/2) entre parenteses
print(f"O seu número é {n1} o seu dobro é {n2} seu triplo é {n3} e por fim sua raiz quadrada é \033[31m{n4:.2f}\033[m")