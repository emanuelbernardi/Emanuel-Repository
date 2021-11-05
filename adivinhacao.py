import random
def jogar():

    print("*********************************")
    print("Bem Vindo no jogo da Adivinhação")
    print("*********************************")

    numero_random = random.randrange(1, 101)
    numero_secreto = (numero_random)
    total_de_tentativa = 0
    pontos = 100

    print('qual nivel de dificuldade?')
    print("(1)Facil (2)Médio (3)Difícil ")

    nivel = int(input("Define nivel"))

    if (nivel == 1):
        total_de_tentativa = 20
    elif (nivel == 2):
        total_de_tentativa = 10
    else:
        total_de_tentativa = 5

    for rodada in range(1, total_de_tentativa + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativa))
        chute_str = input("digite seu numero entre 1 e 100;")
        print("Você Digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("voce deve colocar um N entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):

            print("Você Acertou e fez {} pontos".format(pontos))
            break

        else:
            if (maior):
                print("Você errou ! o seu chute foi maior ")
            elif (menor):
                print("Você errou ! o seu chute foi menor ")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if(__name__ == "__main_"):
    jogar()