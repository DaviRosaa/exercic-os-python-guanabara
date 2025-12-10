from time import sleep

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

opcao = 0

while opcao != 5:
    print('''\n[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')

    opcao = int(input(">>>>>> Qual a sua opção: "))

    if opcao == 1:
        print(f"A soma entre {valor1} + {valor2} é {valor1 + valor2}")

    elif opcao == 2:
        print(f"A multiplicação entre {valor1} x {valor2} é {valor1 * valor2}")

    elif opcao == 3:
        print(f"O maior valor é {max(valor1, valor2)}")

    elif opcao == 4:
        print("Informe os números novamente:")
        valor1 = int(input("Digite um valor: "))
        valor2 = int(input("Digite outro valor: "))

    elif opcao == 5:
        print("Finalizando...")
        sleep(1)

    else:
        print("Opção inválida! Tente novamente.")

print("Fim do programa! Volte sempre!")
