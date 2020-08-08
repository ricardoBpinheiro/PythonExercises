menu = 0


def abrir_arquivo():
    nome = input("Digite o nome do arquivo que deseja abrir: ")
    arquivo = open(nome)
    return arquivo


def ler_arquivo(arquivo):
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha.strip())


while menu != 3:
    print("(1) Abrir arquivo\n(2) Ler arquivo aberto\n(3) Sair")

    menu = input("Digite a opcao: ")

    if menu == '1':
        arquivo = abrir_arquivo()
    elif menu == '2':
        ler_arquivo(arquivo)
