# Escreva um programa que abra um arquivo
# digitado pelo usuário e imprima seu conteúdo na tela.

nome = input("Digite o nome do arquivo para abrir: ")
arquivo = open(nome)

linhas = arquivo.readlines()

for linha in linhas:
    print(linha)
