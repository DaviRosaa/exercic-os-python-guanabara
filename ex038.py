numero1=int(input("digite um número inteiro").strip())
numero2=int(input("digite outro número inteiro").strip())
if numero1>numero2:
    print("\033[34mO primeiro valor é maior\033[m")
elif numero2>numero1:
    print("\033[34mO segundo valor é maior\033[m")
else:
    print("\033[34mOs dois são iguais\033[m")