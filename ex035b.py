print("-=-"*30)
print("Analisador de Triângulo")
print("-=-"*30)
segmento1=float(input("Primeiro segmento: "))
segmento2=float(input("Segundo segmento: "))
segmento3=float(input("Terceiro segmento: "))

segmento="maior"
if segmento2+segmento3>segmento1 and segmento1+segmento2>segmento3 and segmento1+segmento3>segmento2:
    triangulo="pode formar um triângulo"
else:
    triangulo="não pode formar um triângulo"
print(f"{triangulo}")

