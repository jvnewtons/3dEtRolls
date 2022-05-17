from random import randint

programa = True

while programa == True:

    print("Você irá rolar uma FA(Força de Ataque) ou uma FD(Força de Defesa)?")
    print("[1]. FA")
    print("[2]. FD")
    print("[3]. Sair")
    tipo_jogada = int(input("Tipo de rolagem:"))

    while tipo_jogada != 1 and tipo_jogada != 2 and tipo_jogada != 3:
        print("Opa, parece que você digitou algo errado, digite somente 1 para calcular uma FA(Força de Ataque), 2 para")
        print("calcular uma FD(Força de Defesa) e digite 3 caso queira encerrar o programa")
        print("[1]. FA")
        print("[2]. FD")
        print("[3]. Sair")
        tipo_jogada = int(input("Tipo de rolagem:"))

    if tipo_jogada == 1:
        penalidade = int(input("Digite aqui se tiver alguma penalidade pro seu ataque, se não houver, apenas digite 0:"))
        while penalidade < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            penalidade = int(input("Digite aqui se tiver alguma penalidade pro seu ataque, se não houver, apenas digite 0:"))

        habilidade = int(input("Digite o valor de sua Habilidade:"))
        while habilidade < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            habilidade = int(input("Digite o valor de sua Habilidade:"))

        forca_pdf = int(input("Digite o valor de sua Força ou PdF(Se for um ataque a distância):"))
        while forca_pdf < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            forca_pdf = int(input("Digite o valor de sua Força ou PdF(Se for um ataque a distância):"))

        bonus = int(input("Digite aqui se tiver algum bônus para sua FA(o mesmo será aplicado em sua Força ou PdF):"))
        while bonus < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            bonus = int(input("Digite aqui se tiver algum bônus para sua FA(o mesmo será aplicado em sua Força ou PdF):"))

        bonus_fa = int(input("Digite aqui se tiver algum bônus para sua FA(o mesmo será aplicado em sua FA):"))
        while bonus_fa < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            bonus_fa = int(input("Digite aqui se tiver algum bônus para sua FA(o mesmo será aplicado em sua FA):"))

        atk_especial_p = int(input("Digite 1 se possuir ataque especial poderoso e 2 se não possuir:"))
        while atk_especial_p < 0 or atk_especial_p != 1 and atk_especial_p != 2:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            atk_especial_p = int(input("Digite 1 se possuir ataque especial poderoso e 2 se não possuir:"))

        atk_especial_pe = int(input("Digite 1 se possuir ataque especial perigoso e 2 se não possuir:"))
        while atk_especial_p < 0 or atk_especial_p != 1 and atk_especial_p != 2:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            atk_especial_pe = int(input("Digite 1 se possuir ataque especial poderoso e 2 se não possuir:"))


        forca_pdf_total = forca_pdf + bonus

        dado_d6 = randint(1, 6)

        if dado_d6 != 6 and atk_especial_pe != 1:
            fa = (dado_d6 + habilidade + forca_pdf_total + bonus_fa) - penalidade
            print("")
            print("[", "d6 =", dado_d6, "]")
            print("")
            print(dado_d6, "+", habilidade, "+", forca_pdf_total, "+", bonus_fa, "-", penalidade, "=", fa)
            print("Sua FA deu:", fa)
        elif dado_d6 == 6 or (dado_d6 == 5 and atk_especial_pe == 1):
            if atk_especial_p == 1:
                fa = (dado_d6 + habilidade + forca_pdf_total * 3 + bonus_fa) - penalidade
                print("")
                print("[", "d6 =", dado_d6, "]")
                print("")
                print(dado_d6, "+", habilidade, "+", forca_pdf_total, "*", "3", "+", bonus_fa, "-", penalidade, "=", fa)
                print("Sua FA deu:", fa)
            else:
                fa = (dado_d6 + habilidade + forca_pdf_total * 2 + bonus_fa) - penalidade
                print("")
                print("[", "d6 =", dado_d6, "]")
                print("")
                print(dado_d6, "+", habilidade, "+", forca_pdf_total, "*", "2", "+", bonus_fa, "-", penalidade, "=", fa)
                print("Sua FA deu:", fa)

        rolagem_inimiga = int(input("Digite aqui de quanto foi a FD do jogador ou do NPC que você está tentando atacar:"))
        while rolagem_inimiga < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            rolagem_inimiga = int(input("Digite aqui de quanto foi a FD do jogador ou do NPC que você está tentando atacar:"))

        if rolagem_inimiga >= fa:
            print("Você não causa dano, sua FA não venceu a FD do alvo.")
        else:
            dano = fa - rolagem_inimiga
            print(fa, "-", rolagem_inimiga, "=", dano)
            print("Você causa", dano, "de dano!")

        print("")
        print("Deseja repetir a rolagem, realizar outra ou sair do programa?")
        print("[1]. Repetir a rolagem")
        print("[2]. Continuar")
        print("[3]. Sair")
        sair = int(input("Escolha:"))
        while sair != 1 and sair != 2 and sair != 3:
            print("Opa, parece que você digitou algo errado, digite somente 1 para repetir a rolagem, 2 para")
            print("realizar outra rolagem e 3 para sair do programa.")
            print("[1]. Repetir rolagem")
            print("[1]. Continuar")
            print("[3]. Sair")
            sair = int(input("Escolha:"))
        if sair == 1:
            while sair == 1:
                dado_d6_repeat = randint(1, 6)
                if dado_d6_repeat != 6:
                    fa = (dado_d6_repeat + habilidade + forca_pdf_total + bonus_fa) - penalidade
                    print("")
                    print("[", "d6 =", dado_d6_repeat, "]")
                    print("")
                    print(dado_d6_repeat, "+", habilidade, "+", forca_pdf_total, "+", bonus_fa, "-", penalidade, "=", fa)
                    print("Sua FA deu:", fa)
                else:
                    fa = (dado_d6_repeat + habilidade + forca_pdf_total * 2 + bonus_fa) - penalidade
                    print("")
                    print("[", "d6 =", dado_d6_repeat, "]")
                    print("")
                    print(dado_d6_repeat, "+", habilidade, "+", forca_pdf_total, "*", "2", "+", bonus_fa, "-",
                          penalidade, "=",
                          fa)
                    print("Sua FD deu:", fa)
                rolagem_inimiga = int(
                    input("Digite aqui de quanto foi a FD do jogador ou do NPC que você está tentando atacar:"))
                while rolagem_inimiga < 0:
                    print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
                    rolagem_inimiga = int(
                        input("Digite aqui de quanto foi a FD do jogador ou do NPC que você está tentando atacar:"))

                if rolagem_inimiga >= fa:
                    print("Você não causa dano, sua FA não venceu a FD do alvo.")
                else:
                    dano = fa - rolagem_inimiga
                    print(fa, "-", rolagem_inimiga, "=", dano)
                    print("Você causa", dano, "de dano!")
                print("")
                print("Deseja repetir a rolagem, realizar outra ou sair do programa?")
                print("[1]. Repetir a rolagem")
                print("[2]. Continuar")
                print("[3]. Sair")
                sair = int(input("Escolha:"))
                while sair != 1 and sair != 2 and sair != 3:
                    print("Opa, parece que você digitou algo errado, digite somente 1 para repetir a rolagem, 2 para")
                    print("realizar outra rolagem e 3 para sair do programa.")
                    print("[1]. Repetir rolagem")
                    print("[1]. Continuar")
                    print("[3]. Sair")
                    sair = int(input("Escolha:"))

        elif sair == 2:
            continue
        else:
            print("Até mais!")
            programa = False

    elif tipo_jogada == 2:
        penalidade = int(input("Digite aqui se tiver alguma penalidade pra sua defesa, se não houver, apenas digite 0:"))
        while penalidade < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            penalidade = int(input("Digite aqui se tiver alguma penalidade pra sua defesa, se não houver, apenas digite 0:"))

        habilidade = int(input("Digite o valor de sua Habilidade:"))
        while habilidade < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            habilidade = int(input("Digite o valor de sua Habilidade:"))

        armadura = int(input("Digite o valor de sua Armadura:"))
        while armadura < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            armadura = int(input("Digite o valor de sua Armadura:"))

        bonus = int(input("Digite aqui se tiver algum bônus para sua FD(o mesmo será aplicado em sua Armadura):"))
        while bonus < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            bonus = int(input("Digite aqui se tiver algum bônus para sua FD(o mesmo será aplicado em sua Armadura):"))

        bonus_fd = int(input("Digite aqui se tiver algum bônus para sua FD(o mesmo será aplicado em sua FD):"))
        while bonus_fd < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            bonus_fd = int(input("Digite aqui se tiver algum bônus para sua FD(o mesmo será aplicado em sua FD):"))

        armadura_total = armadura + bonus

        dado_d6 = randint(1, 6)

        if dado_d6 != 6:
            fd = (dado_d6 + habilidade + armadura_total + bonus_fd) - penalidade
            print("")
            print("[", "d6 =", dado_d6, "]")
            print("")
            print(dado_d6, "+", habilidade, "+", armadura_total, "+", bonus_fd, "-", penalidade, "=", fd)
            print("Sua FD deu:", fd)
        else:
            fd = (dado_d6 + habilidade + armadura_total * 2 + bonus_fd) - penalidade
            print("")
            print("[", "d6 =", dado_d6, "]")
            print("")
            print(dado_d6, "+", habilidade, "+", armadura_total, "*", "2", "+", bonus_fd, "-", penalidade, "=", fd)
            print("Sua FD deu:", fd)

        rolagem_inimiga = int(input("Digite aqui de quanto foi a FA do jogador ou do NPC que está tentando te atacar:"))
        while rolagem_inimiga < 0:
            print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
            rolagem_inimiga = int(input("Digite aqui de quanto foi a FA do jogador ou do NPC que está tentando te atacar:"))

        if rolagem_inimiga <= fd:
            print("A FA inimiga não venceu sua FD, você não recebe dano!")
        else:
            dano = rolagem_inimiga - fd
            print(rolagem_inimiga, "-", fd, "=", dano)
            print("Você recebe", dano, "de dano. Ouch!")

        print("")
        print("Deseja repetir a rolagem, realizar outra ou sair do programa?")
        print("[1]. Repetir a rolagem")
        print("[2]. Continuar")
        print("[3]. Sair")
        sair = int(input("Escolha:"))
        while sair != 1 and sair != 2 and sair != 3:
            print("Opa, parece que você digitou algo errado, digite somente 1 para repetir a rolagem, 2 para")
            print("realizar outra rolagem e 3 para sair do programa.")
            print("[1]. Repetir rolagem")
            print("[1]. Continuar")
            print("[3]. Sair")
            sair = int(input("Escolha:"))
        if sair == 1:
            while sair == 1:
                dado_d6_repeat = randint(1, 6)
                if dado_d6_repeat != 6:
                    fd = (dado_d6_repeat + habilidade + armadura_total + bonus_fd) - penalidade
                    print("")
                    print("[", "d6 =", dado_d6_repeat, "]")
                    print("")
                    print(dado_d6_repeat, "+", habilidade, "+", armadura_total, "+", bonus_fd, "-", penalidade, "=", fd)
                    print("Sua FD deu:", fd)
                else:
                    fd = (dado_d6_repeat + habilidade + armadura_total * 2 + bonus_fd) - penalidade
                    print("")
                    print("[", "d6 =", dado_d6_repeat, "]")
                    print("")
                    print(dado_d6_repeat, "+", habilidade, "+", armadura_total, "*", "2", "+", bonus_fd, "-", penalidade, "=",
                          fd)
                    print("Sua FD deu:", fd)
                rolagem_inimiga = int(input("Digite aqui de quanto foi a FA do jogador ou do NPC que está tentando te atacar:"))
                while rolagem_inimiga < 0:
                    print("Opa! Só precisa colocar números positivos, tenta digitar novamente.")
                    rolagem_inimiga = int(input("Digite aqui de quanto foi a FA do jogador ou do NPC que está tentando te atacar:"))

                if rolagem_inimiga <= fd:
                    print("A FA inimiga não venceu sua FD, você não recebe dano!")
                else:
                    dano = rolagem_inimiga - fd
                    print(rolagem_inimiga, "-", fd, "=", dano)
                    print("Você recebe", dano, "de dano. Ouch!")
                print("")
                print("Deseja repetir a rolagem, realizar outra ou sair do programa?")
                print("[1]. Repetir a rolagem")
                print("[2]. Continuar")
                print("[3]. Sair")
                sair = int(input("Escolha:"))
                while sair != 1 and sair != 2 and sair != 3:
                    print("Opa, parece que você digitou algo errado, digite somente 1 para repetir a rolagem, 2 para")
                    print("realizar outra rolagem e 3 para sair do programa.")
                    print("[1]. Repetir rolagem")
                    print("[1]. Continuar")
                    print("[3]. Sair")
                    sair = int(input("Escolha:"))

        elif sair == 2:
            continue
        else:
            print("Até mais!")
            programa = False

    else:
        print("Até mais!")