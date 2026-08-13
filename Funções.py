import random
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def criar_tabuleiro(linhas, colunas):
    
    return [["0" for _ in range(colunas)] for _ in range(linhas)]


def criar_tabuleiro_visivel(linhas, colunas):
    
    return [["#" for _ in range(colunas)] for _ in range(linhas)]


def posicionar_minas(tabuleiro, qtd_minas, linha_inicial, coluna_inicial):
    
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    minas_colocadas = 0

    while minas_colocadas < qtd_minas:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)

        
        if (linha, coluna) == (linha_inicial, coluna_inicial):
            continue
        if tabuleiro[linha][coluna] == "M":
            continue

        tabuleiro[linha][coluna] = "M"
        minas_colocadas += 1

    calcular_numeros(tabuleiro)
    return tabuleiro


def calcular_numeros(tabuleiro):
    
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    for linha in range(linhas):
        for coluna in range(colunas):
            if tabuleiro[linha][coluna] == "M":
                continue

            contador = 0
            for dl in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dl == 0 and dc == 0:
                        continue
                    nl, nc = linha + dl, coluna + dc
                    if 0 <= nl < linhas and 0 <= nc < colunas:
                        if tabuleiro[nl][nc] == "M":
                            contador += 1

            tabuleiro[linha][coluna] = str(contador)


def mostrar_tabuleiro(tabuleiro_visivel):
    
    colunas = len(tabuleiro_visivel[0])

    
    cabecalho = "    " + " ".join(f"{c:2}" for c in range(colunas))
    print(cabecalho)
    print("   " + "---" * colunas)

    for i, linha in enumerate(tabuleiro_visivel):
        linha_formatada = " ".join(f"{celula:2}" for celula in linha)
        print(f"{i:2} | {linha_formatada}")
    print()


def revelar_celula(tabuleiro, tabuleiro_visivel, linha, coluna):
    
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    if not (0 <= linha < linhas and 0 <= coluna < colunas):
        return
    if tabuleiro_visivel[linha][coluna] != "#":
        return  

    tabuleiro_visivel[linha][coluna] = tabuleiro[linha][coluna]

    
    if tabuleiro[linha][coluna] == "0":
        for dl in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dl == 0 and dc == 0:
                    continue
                revelar_celula(tabuleiro, tabuleiro_visivel, linha + dl, coluna + dc)


def marcar_bandeira(tabuleiro_visivel, linha, coluna):
    
    if tabuleiro_visivel[linha][coluna] == "#":
        tabuleiro_visivel[linha][coluna] = "F"
        print("Bandeira colocada!")
    elif tabuleiro_visivel[linha][coluna] == "F":
        tabuleiro_visivel[linha][coluna] = "#"
        print("Bandeira removida!")
    else:
        print("Essa célula já está revelada, não é possível marcar.")


def verificar_vitoria(tabuleiro, tabuleiro_visivel):
    
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    for linha in range(linhas):
        for coluna in range(colunas):
            if tabuleiro[linha][coluna] != "M" and tabuleiro_visivel[linha][coluna] == "#":
                return False
    return True


def revelar_tudo(tabuleiro, tabuleiro_visivel):
    
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    for linha in range(linhas):
        for coluna in range(colunas):
            tabuleiro_visivel[linha][coluna] = tabuleiro[linha][coluna]


def pedir_posicao(linhas, colunas):
    
    while True:
        try:
            entrada = input("Digite linha e coluna (ex: 3 5): ").split()
            linha, coluna = int(entrada[0]), int(entrada[1])
            if 0 <= linha < linhas and 0 <= coluna < colunas:
                return linha, coluna
            else:
                print("Posição fora do tabuleiro. Tente novamente.")
        except (ValueError, IndexError):
            print("Entrada inválida. Digite dois números separados por espaço.")


def pedir_acao():
    
    while True:
        acao = input("Escolha a ação - (r) revelar ou (m) marcar bandeira: ").strip().lower()
        if acao in ("r", "m"):
            return acao
        print("Opção inválida. Digite 'r' ou 'm'.")


def escolher_dificuldade():
    
    print("\nEscolha a dificuldade:")
    print("1 - Fácil   (8x8, 10 minas)")
    print("2 - Médio   (12x12, 20 minas)")
    print("3 - Difícil (16x16, 40 minas)")

    while True:
        opcao = input("Opção: ").strip()
        if opcao == "1":
            return 8, 8, 10
        elif opcao == "2":
            return 12, 12, 20
        elif opcao == "3":
            return 16, 16, 40
        else:
            print("Opção inválida. Tente novamente.")


def jogar():
    
    limpar_tela()
    print("=== CAMPO MINADO ===")
    linhas, colunas, qtd_minas = escolher_dificuldade()

    tabuleiro = criar_tabuleiro(linhas, colunas)
    tabuleiro_visivel = criar_tabuleiro_visivel(linhas, colunas)

    primeira_jogada = True
    jogo_ativo = True

    while jogo_ativo:
        limpar_tela()
        print("=== CAMPO MINADO ===")
        print(f"Minas no tabuleiro: {qtd_minas}\n")
        mostrar_tabuleiro(tabuleiro_visivel)

        linha, coluna = pedir_posicao(linhas, colunas)
        acao = pedir_acao()

        if acao == "m":
            marcar_bandeira(tabuleiro_visivel, linha, coluna)
            input("Pressione ENTER para continuar...")
            continue

        
        if primeira_jogada:
            posicionar_minas(tabuleiro, qtd_minas, linha, coluna)
            primeira_jogada = False

        if tabuleiro[linha][coluna] == "M":
            
            revelar_tudo(tabuleiro, tabuleiro_visivel)
            limpar_tela()
            print("=== CAMPO MINADO ===\n")
            mostrar_tabuleiro(tabuleiro_visivel)
            print(" BOOM! Você pisou em uma mina. GAME OVER! ")
            jogo_ativo = False
        else:
            revelar_celula(tabuleiro, tabuleiro_visivel, linha, coluna)

            if verificar_vitoria(tabuleiro, tabuleiro_visivel):
                revelar_tudo(tabuleiro, tabuleiro_visivel)
                limpar_tela()
                print("=== CAMPO MINADO ===\n")
                mostrar_tabuleiro(tabuleiro_visivel)
                print(" PARABÉNS! Você revelou todas as Casas Seguras. VOCÊ VENCEU! ")
                jogo_ativo = False

    input("\nPressione ENTER para voltar ao menu...")