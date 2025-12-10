from random import randint

print("Vamos jogar Jokenpô")
jogo1 = input("Escolha pedra, papel ou tesoura: ").strip().lower()

jokenpo = randint(1, 3)

# Determinar a jogada do computador
if jokenpo == 1:
    computador = "pedra"
elif jokenpo == 2:
    computador = "papel"
else:
    computador = "tesoura"

print(f"O computador jogou: {computador}")

# --- Comparação de resultados ---
if jogo1 == computador:
    print("Empate!")

elif (jogo1 == "pedra" and computador == "tesoura") or \
     (jogo1 == "papel" and computador == "pedra") or \
     (jogo1 == "tesoura" and computador == "papel"):
    print("Você ganhou!")

elif jogo1 in ["pedra", "papel", "tesoura"]:
    print("Você perdeu!")

else:
    print("Opção inválida!")
