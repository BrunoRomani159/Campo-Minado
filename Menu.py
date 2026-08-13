from Funções import limpar_tela, jogar



def menu_principal():
    
    while True:
        limpar_tela()
        print("=========================")
        print("     CAMPO MINADO")
        print("=========================")
        print("1 - Jogar")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            jogar()
        elif opcao == "2":
            limpar_tela()
            print("Obrigado por jogar. Até a próxima!")
            break
        else:
            print("Opção inválida! Pressione ENTER para tentar novamente.")
            input()




if __name__ == "__main__":
    menu_principal()