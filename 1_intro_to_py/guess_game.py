import random

def play():
    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    secret_number = random.randrange(1, 101)
    ponto = 100
    tent = 0

    print("Defina o nível de dificuldade")
    dific = int(input("(1)Fácil (2)Médio (3)Difícil\n"))

    if dific == 1:
        tent = 20
    elif dific == 2:
        tent = 10
    else:
        tent = 5

    for partida in range(tent):
        print("\nTentativa {} de {}".format(partida+1, tent))
        guess_str = input("Qual o seu chute? (Entre 1 e 100): ")
        guess = int(guess_str)

        certo = guess == secret_number
        maior = guess > secret_number
        menor = guess < secret_number

        if guess < 1 or guess > 100:
            print("Você deve digitar um número entre 1 e 100!")
            points -= 10
            continue

        if certo:
            print("Acertô miseravi!")
            ponto += (tent - partida) * dific
            break
        else:
            if maior:
                print("Errrrooouuu! Tente um número menor")
            elif menor:
                print("Errrrooouuu! Tente um número maior")

            ponto -= abs(secret_number - guess)

    print(f"Pontuação: {ponto}")
    print("\nFim do Jogo!")

if __name__ == "__main__":
    play()
