import random
opcoes = ["pedra", "papel", "tesoura"]

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "pedra"):
         return "Voce venceu!"
    else:
        return "Comptador venceu!"

while True:
    jogador_escolha = input("Escolha pedra, papel ou tesoura ou sair para terminar): ").lower()

    if jogador_escolha == "sair":
        print("Obrigado por jogar!")
        break
    elif jogador_escolha not in opcoes:
        print("Escolha inválida, tente novamente.")
        continue

    computador_escolha = random.choice(opcoes)
    print(f"Computador escolheu: {computador_escolha}")

    resultado = determinar_vencedor(jogador_escolha, computador_escolha)
    print(resultado)