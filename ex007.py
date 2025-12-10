print("calculadora de média escolar")
n1=float(input("digite sua nota do primeiro bimestre").strip())
n2=float(input("digite sua nota do segundo bimestre").strip())
n3=float(input("digite sua nota do terceiro bimestre").strip())
n4=float(input("digite sua nota do quarto bimestre").strip())
s=float(n1+n2+n3+n4)
d=f"{s / 4:.1f}"
print(f"O resultado da sua média escolar durante o ano letivo é \033[33m{d}\033[m")