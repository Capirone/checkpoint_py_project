import random

hp = 100
hp_troll = 100

def atacar():
    global hp_troll
    print("Você gira o dado e vê a eficácia da sua ação.")
    dado = random.randint(1, 20)
    if dado >= 15:
        print("Acerto crítico! Você causou muito dano.")
        hp_troll -= 50
    elif dado >= 10:
        print("Acerto normal! O inimigo foi ferido.")
        hp_troll -= 25
    else:
        print("Errou o golpe... o inimigo se esquivou.")

def esquivar():
    global hp
    print("Você gira o dado e vê a eficácia da sua ação.")
    dado = random.randint(1, 20)
    if dado >= 15:
        print("Esquivou totalmente!")
    elif dado >= 10:
        print("Pegou de raspão! Você perdeu 10 de vida.")
        hp -= 10
    else:
        print("Puts... acertou em cheio. Menos 20 de vida.")
        hp -= 20

def troll():
    global hp
    if acao_jogador == 1:
        print("Agora é a vez do troll >:(")
        dado = random.randint(1, 20)
        if dado >= 15:
            print("Acerto crítico! Ele causou muito dano.")
            hp -= 50
        elif dado >= 10:
            print("Acerto normal! Você foi ferido.")
            hp -= 25
        else:
            print("Acerto fraco, segue a luta")
            hp -=10
    else:
        print("")

print("Você é um guerreiro tentando resgatar a princesa do castelo e precisa passar por alguns desafios.")

while hp_troll > 0 and hp > 0:
    acao_jogador = int(input(
        f"Andando até o castelo, você encontra um troll protegendo a ponte. O que você faz?\n"
        f"1 - Atacar\n"
        f"2 - Esquivar\n"
        f"HP do Troll: {hp_troll} | Seu HP: {hp}\n"
        f"Digite sua escolha: "
    ))

    if acao_jogador == 1:
        atacar()
    elif acao_jogador == 2:
        esquivar()

    troll()

if hp_troll <= 0:
    print("🎉 PARABÉNS! Você derrotou o troll e resgatou a princesa!")
elif hp <= 0:
    print("💀 Você foi derrotado... mas ainda há esperança para a próxima tentativa!")
