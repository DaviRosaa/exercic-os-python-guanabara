print(f"{"-=-"*20}\n Analisador de triângulos \n{"-=-"*20}")
segmento1=float(input("Primeiro segmento: ").strip())
segmento2=float(input("Segundo segmento: ").strip())
segmento3=float(input("Terceiro segmento: ").strip())
if segmento1+segmento2>segmento3 and segmento2+segmento3>segmento1 and segmento1+segmento3>segmento2:
    print("Pode formar um triângulo",end=" ") #Novamente o uso do end=" ", aonde foi muito útil

    if segmento1==segmento2==segmento3:
        print("equilátero")
    elif segmento1==segmento2 or segmento2==segmento3 or segmento3==segmento1:
        print("Este triângulo é isósceles")
    elif segmento1 != segmento2 and segmento2 != segmento3 and segmento3 != segmento1: #Poderia fazer assim: elif segmento != segmento2 != segmento3 != segmento1:
        print("Este triângulo é escaleno")
else:
    print("Não pode formar um triângulo")

