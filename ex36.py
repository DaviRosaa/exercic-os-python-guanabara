print(f"\033[32m{"-=-" * 10}\033[m")
print("\033[32m$$$ Empréstimo bancário $$$\033[m")
print(f"\033[32m{"-=-" * 10}\033[m")
valor_casa=float(input("Qual o valor da casa?").strip())
salario_comprador=float(input("Qual o seu salário").strip())
anos=int(input("Quantos anos de financiamento?").strip())
prestacao=valor_casa/(anos * 12)
print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos} anos."
    f" A prestação será de {prestacao:.2f}reais")
trinta_por_cento=float(0.3*salario_comprador)
if prestacao<trinta_por_cento:
    emprestimo="foi \033[32maprovado\033[m"
else:
    emprestimo="foi \033[31mNEGADO\033[m"
print(f"seu empréstimo {emprestimo}")

#MELHOR CÓDIGO QUE JÁ FIZ NA MINHA VIDA 🤩
