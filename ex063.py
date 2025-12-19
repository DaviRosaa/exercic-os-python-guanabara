print("Sequência de Fibonacci")
termos = int(input("Quantos termos quer mostrar? "))
t1 = contador = 0
t2 = 1
soma = 0

while contador <= termos:
    print(t1,end=" ")
    soma = t1 + t2
    t1 = t2
    t2 = soma

    contador = contador + 1
