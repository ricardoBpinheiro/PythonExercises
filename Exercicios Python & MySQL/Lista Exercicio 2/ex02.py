# Escreva um programa que abra um arquivo
# digitado pelo usuário e imprima seu conteúdo na tela.

w = open("arquivo.txt", "w")  # abre arquivo pra escrever

escreve = str(input("Digite algo: "))
w.write(escreve)
w.close()

r = open("arquivo.txt", "r")  # abre arquivo pra escrever
ler = r.read()

print("Texto Digitado")
print("-=" * 20)
print(ler)

r.close()
