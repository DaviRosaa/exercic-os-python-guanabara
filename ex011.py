largura=float(input("Qual a largura da sua parede"))
altura=float(input("Qual a altura da sua parede"))
area=int(largura*altura)
tinta=area/2

print(f"A area da sua parede é de: \033[44m{area}m\033[m e será necessário \033[44m{tinta}l\033[m de tinta")