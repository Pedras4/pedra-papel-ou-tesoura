import random
escolhido = 0,1,2,3,4,5,6,7,8,9,10
computador_escolha = random.choice(escolhido)
humano_escolha = input("Qual é o numero de 0 a 10 que eu estou a pensar?")
    if humano_escolha == computador_escolha:
        print("Conseguiste acertar!")
        return
    else:
        return print("Não conseguiste acertar!")