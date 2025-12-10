sexo = input("Informe o seu sexo [M/F]: ").upper()
if sexo == "M" or sexo == "F":
    print("Ok, sexo registrado com sucesso!")
while sexo not in ["M","F"]:
    sexo = input("Informe o seu sexo [M/f] ").upper()
    if sexo in "mM" or sexo in "Ff":
        print("Ok, sexo registrado com sucesso!")