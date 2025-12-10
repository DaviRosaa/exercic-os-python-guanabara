ni = int(input("Digite um número: "))
print(f"Tabuada de \033[35m{ni}:\033[m")
print(f"-"*12)
for i in range(1, 11):   #amazing! decorar essa linha
    print(f"{ni} x {i} = {ni * i}") #e essa também
print(f"-"*12)