# JOGO DA VELHA EM PYTHON

# Criando o tabuleiro
tabuleiro = [" " for _ in range(9)]

# Função para mostrar o tabuleiro
def mostrar_tabuleiro():
    print()
    print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
    print("---+---+---")
    print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
    print("---+---+---")
    print(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])
    print()

# Função para verificar se existe um vencedor
def verificar_vencedor(jogador):

    combinacoes = [
        [0, 1, 2], # Primeira linha
        [3, 4, 5], # Segunda linha
        [6, 7, 8], # Terceira linha
        [0, 3, 6], # Primeira coluna
        [1, 4, 7], # Segunda coluna
        [2, 5, 8], # Terceira coluna
        [0, 4, 8], # Diagonal principal
        [2, 4, 6]  # Diagonal secundária
    ]

    for combinacao in combinacoes:
        if all(tabuleiro[posicao] == jogador for posicao in combinacao):
            return True

    return False

# Função principal do jogo
def jogo():

    jogador_atual = "X"

    print("===== JOGO DA VELHA =====")
    print("Posições disponíveis:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:

        mostrar_tabuleiro()

        print("Vez do jogador:", jogador_atual)

        try:
            jogada = int(input("Escolha uma posição (1 a 9): ")) - 1
        except ValueError:
            print("Digite um número válido!")
            continue

        # Verifica se a posição é válida
        if jogada < 0 or jogada > 8:
            print("Posição inválida! Escolha de 1 a 9.")
            continue

        # Verifica se a posição está ocupada
        if tabuleiro[jogada] != " ":
            print("Essa posição já está ocupada!")
            continue

        # Marca a jogada
        tabuleiro[jogada] = jogador_atual

        # Verifica se alguém venceu
        if verificar_vencedor(jogador_atual):
            mostrar_tabuleiro()
            print("Parabéns! Jogador", jogador_atual, "venceu!")
            break

        # Verifica se houve empate
        if " " not in tabuleiro:
            mostrar_tabuleiro()
            print("O jogo terminou em empate!")
            break

        # Alterna entre os jogadores
        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"

# Inicia o jogo
jogo()
