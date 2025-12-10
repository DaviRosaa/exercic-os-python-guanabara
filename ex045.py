from random import randint


print("Vamos jogar Jokenpô")
jogo1=(input("Escolha pedra, papel ou tesoura: ").strip())
jokenpo=randint(1,3)
if jokenpo==1:
    computador="pedra"
elif jokenpo==2:
    computador="papel"
else:
    computador="tesoura"
print(f"O computador jogou {computador}")

if computador==jogo1:
    print("Empate")
# --- consegui fazer até aqui, é isso ---


