numero=int(input("Digite um número para conversão: "))
print("1 para binário 2 para octal e 3 para hexadecimal:\n\n ")
opcao=int(input("Qual a opção? ").strip())
if opcao==1:
    print(f"\033[34m{numero:b}\033[m") #implementação do :b e exclusão do bin
elif opcao==2:
    print(f"\033[34m{numero:o}\033[m") #implementação do :o e exclusão do oct
elif opcao==3:
    print(f"\033[34m{numero:x}\033[m") #implementação do :x e exclusão do hex()
else:
    print("Opção inválida, digite outro número")

