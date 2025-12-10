nota1=float(input("Quanto você tirou na primeira avaliação? ").strip())
nota2=float(input("E na segunda avaliação? ").strip())
media=(nota1+nota2)/2
if media < 5.0:
    print(f"A sua média foi \033[31m{media:.1f}\033[m e voçê está \033[31mREPROVADO\033[m")
elif  5.0 <= media < 7.0:
    print(f"A sua média foi \033[33m{media:.1f}\033[m e voçê está de \033[33mRECUPERAÇÃO\033[m")
else:
    print(f"A sua média foi \033[32m{media:.1f}\033[m e voçê está \033[32mAPROVADO\033[m")
