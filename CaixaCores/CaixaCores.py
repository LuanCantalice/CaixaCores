cores = []

def AdicionarCor():
    cor = input( "Você deseja adicionar qual cor? ")
    cores.append(cor)
    print("Nova cor adicionada:", cor)

def ListarCores():
    print("As cores adicionadas são:")
    for a in cores:
        print(a)

def ExibirMenu():
    perg = input("Você deseja adicionar mais alguma cor? 1 para sim 2 para não: ")
    if (perg == "1"):
        AdicionarCor()
    else:
        pass
    perg2 = input("Digite 1 para adicionar mais cores, 2 para listar as cores existentes e 3 para sair: ")
    if (perg2 == "1"):
        AdicionarCor()
    elif(perg2 == "2"):
        ListarCores()
        perg3 = input("Você deseja adicionar mais alguma cor? 1 para sim 2 para sair: ")
        if (perg3 == "1"):
            AdicionarCor()
            perg4 = input(" Deseja sair ou listar? 1 para listar 2 para sair ")
            if (perg4 == "1"):
                ListarCores()
            else:
                exit()

AdicionarCor()
ListarCores()
ExibirMenu()