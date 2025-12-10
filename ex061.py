print("Gerador de PA\n-=-=-=-=-=-=-=-")
primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Qual a razão: "))
termo_geral = primeiro_termo + (11-1) * razao
while primeiro_termo < termo_geral:
    print(primeiro_termo,end=" ")
    primeiro_termo = primeiro_termo + razao

