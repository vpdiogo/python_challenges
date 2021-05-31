def computador_escolhe_jogada(n, m):
    c = 1
    p_restantes = n - c
    if (p_restantes % (m + 1) == 0):
        escolha_c = c 
    else:
        while c <= m and p_restantes >= 0:
            c = c + 1
            p_restantes = n - c
            if (p_restantes % (m + 1) == 0):
                escolha_c = c
    return escolha_c


def usuario_escolhe_jogada(n, m):
    j = m + 1
    while j > m:
        print()
        j = int(input("Quantas peças você vai tirar? "))
        if j > m:
            print()
            print("Oops! Jogada inválida! Tente de novo. ")
        else:
            escolha_j = j
    return escolha_j


def partida():        
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    count = n  
    placar = 0

    if (n % (m + 1) == 0):
        print()
        print("Você começa!")
        print()
        pecas_u = usuario_escolhe_jogada(n, m)
        pecas_res_u = count - pecas_u
        print()
        if pecas_u == 1:
        	print("Você tirou uma peça.")
        else:
        	print("Você tirou", pecas_u, "peças.")
        if pecas_res_u == 1:
            print("Agora resta apenas uma peça no tabuleiro")
        else:
            print("Agora restam", pecas_res_u, "peças no tabuleiro.")
        count = pecas_res_u
        while count > 0:
            pecas_c = computador_escolhe_jogada(count, m)
            pecas_res_c = count - pecas_c
            print()
            if pecas_c == 1:
            	print("O computador tirou uma peça.")
            else:
            	print("O computador tirou", pecas_c, "peças.")
            if pecas_res_c == 1:
                print("Agora resta apenas uma peça no tabuleiro")
            else:
                print("Agora restam", pecas_res_c, "peças no tabuleiro.")
            count = pecas_res_c
            if pecas_res_c == 0:
                print("Fim do jogo! O computador ganhou!")
                placar = 1
            else:
                pecas_u = usuario_escolhe_jogada(count, m)
                pecas_res_u = count - pecas_u
                print()
                print("Você tirou", pecas_u, "peças.")
                if pecas_res_u == 1:
                    print("Agora resta apenas uma peça no tabuleiro")
                else:
                    print("Agora restam", pecas_res_u, "no tabuleiro.")
                count = pecas_res_u
                if pecas_res_u == 0:
                    print("Fim do jogo! O usuário ganhou!")
                    placar = 2
        return placar
        
    else:
        print()
        print("Computador começa!")
        print()
        pecas_c = computador_escolhe_jogada(n, m)
        pecas_res_c = count - pecas_c
        if pecas_c == 1:
        	print("O computador tirou um peça.")
        else:
        	print("O computador tirou", pecas_c, "peças.")
        if pecas_res_c == 1:
            print("Agora resta apenas uma peça no tabuleiro")
        else:
            print("Agora restam", pecas_res_c, "peças no tabuleiro.")
        count = pecas_res_c
        while count > 0:
            pecas_u = usuario_escolhe_jogada(count, m)
            pecas_res_u = count - pecas_u
            print()
            if pecas_u == 1:
            	print("Você tirou uma peça.")
            else:
            	print("Você tirou", pecas_u, "peças.")
            if pecas_res_u == 1:
                print("Agora resta apenas uma peça no tabuleiro")
            else:
                print("Agora restam", pecas_res_u, "peças no tabuleiro.")
            count = pecas_res_u
            if pecas_res_u == 0:
                print("Fim do jogo! O usuário ganhou!")
                placar = 2
            else:
                pecas_c = computador_escolhe_jogada(count, m)
                pecas_res_c = count - pecas_c
                print()
                if pecas_c == 1:
                	print("O Computador tirou uma peça.")
                else:
                	print("O Computador tirou", pecas_c, "peças.")
                if pecas_res_c == 1:
                    print("Agora resta apenas uma peça no tabuleiro")
                else:
                    print("Agora restam", pecas_res_c, "peças no tabuleiro.")
                count = pecas_res_c
                if pecas_res_c == 0:
                    print("Fim do jogo! O computador ganhou!")
                    placar = 1
        return placar
    
def main():
    print("Bem-vindo ao jogo do NIM!  Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    print()

    opcao = 0
    while opcao != 1 and opcao != 2:   
        opcao = int(input())
        if opcao != 1 and opcao != 2:
            print("Opção inválida!")

    placar_u = 0
    placar_c = 0
    
    if opcao == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    if opcao == 2:
        print("Você escolheu um campeonato!")
        count = 1
        while count <= 3:
            print()
            print("**** Rodada ", count, "****")
            print()
            if partida() == 1:
                placar_c =  placar_c + 1
            else:
                placar_u = placar_u + 1
            count = count + 1
        print()
        print("**** Final do campeonato! ****")
        print()
        print("Placar: Você ", placar_u, "X", placar_c, "Computador")

main()
