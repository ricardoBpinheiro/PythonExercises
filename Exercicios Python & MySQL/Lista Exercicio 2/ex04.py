# Escreva um programa que exiba um menu
# e pergunte o que o usuário deseja fazer.
# Se o usuário digitar 1, o programa deve
# chamar uma função que lê um arquivo de texto.
# Se o usuário apertar 2, o programa deve imprimir
# o conteúdo do arquivo lido anteriormente.
# Se o usuário apertar três o programa deve ser fechado.


def ler_arquivo():
    arquivo = open("arquivo.txt", "r")
    return arquivo


def mostra_conteudo():
    arquivo = ler_arquivo()
    ler = arquivo.read()
    print(ler)


def menu():
    print("-=" * 20)
    print("MENU")
    print("1 - Ler arquivo")
    print("2 - Imprime conteudo do arquivo")
    print("3 - Sair")
    print("-=" * 20)


opcao = 0
while opcao != '3':
    menu()
    opcao = input("Digite uma opção > ")

    if opcao == '1':
        ler_arquivo()
        print("Arquivo aberto")
    if opcao == '2':
        print("-=" * 20)
        print("Conteudo: ")
        mostra_conteudo()
