print(f"{"-=-"*20}\n Analisador de triângulos \n{"-=-"*20}")
segmento1=float(input("Primeiro segmento:"))
segmento2=float(input("Segundo segmento"))
segmento3=float(input("Terceiro segmento"))
if segmento1+segmento2>segmento3 and segmento2+segmento3>segmento1 and segmento1+segmento3>segmento2:
    triangulo="Pode formar um triângulo"
else:
    triangulo="Não pode formar um triângulo"
print(f"{triangulo}")