def computador_escolhe_jogada(n, m):
    if (n % (m+1)) != 0 and (n % (m+1)) < m:
        return (n % (m+1))
    else:
        return m


def usuario_escolhe_jogada(n, m):
    Escolha = int(input("Quantas peças você vai tirar? "))

    while (Escolha > m) or (Escolha <= 0) or (n-Escolha < 0):
        print("Oops! Jogada inválida! Tente de novo.")
        Escolha = int(input("Quantas peças você vai tirar? "))

    return Escolha


def partida():
    nqtdP = int(input("Quantas peças? "))
    mLim = int(input("Limite de peças por jogada? "))

    if nqtdP < mLim:
        print("Você começa!")
        while nqtdP > 0:
            nqtdP -= usuario_escolhe_jogada(nqtdP, mLim)
            if nqtdP == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            if nqtdP == 0:
                print("Fim do jogo! Você ganhou!")
                return True
            nqtdP -= computador_escolhe_jogada(nqtdP, mLim)
            if nqtdP == 0:
                print("Fim do jogo! O computador ganhou!")
                return False

    if nqtdP % (mLim+1) == 0:
        print("Você começa!")
        while nqtdP > 0:
            nqtdP -= usuario_escolhe_jogada(nqtdP, mLim)
            if nqtdP == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            if nqtdP == 0:
                print("Fim do jogo! Você ganhou!")
                return True
            nqtdP -= computador_escolhe_jogada(nqtdP, mLim)
            if nqtdP == 0:
                print("Fim do jogo! O computador ganhou!")
                return False
    else:
        print("Computador começa!")
        while nqtdP > 0:
            nqtdP -= computador_escolhe_jogada(nqtdP, mLim)
            if nqtdP == 0:
                print("Fim do jogo! O computador ganhou!")
                return False
            nqtdP -= usuario_escolhe_jogada(nqtdP, mLim)
            if nqtdP == 0:
                print("Fim do jogo! Você ganhou!")
                return True


def campeonato():
    rodada = 0
    pontVc = 0
    pontComp = 0

    print("Voce escolheu um campeonato!")

    while rodada != 3:
        print("**** Rodada", rodada+1, "****")

        if partida():
            pontVc += 1
        else:
            pontComp += 1
        rodada += 1

    print("**** Final do campeonato! ****")

    print("Placar: Você", pontVc, "X", pontComp, "Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")

    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    opt = int(input())

    if opt == 1:
        partida()
    else:
        campeonato()


if __name__ == "__main__":
    main()
