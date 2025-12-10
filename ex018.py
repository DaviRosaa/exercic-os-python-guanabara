from math import sin,cos,tan,radians
angulo=float(input("Digite o valor do angulo: ").strip())
angulo_formatado=radians(angulo)
print(f"O angulo de {angulo} tem o seno de \033[33m{sin(angulo_formatado):.2f}\033[m")
print(f"O angulo de {angulo} tem o cosseno de \033[33m{cos(angulo_formatado):.2f}\033[m")
print(f"O angulo de {angulo} tem a tangente de \033[33m{tan(angulo_formatado):.2f}\033[m")

