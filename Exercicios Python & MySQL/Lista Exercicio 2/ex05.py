# Escreva um programa que leia um
# arquivo multi-fasta e armazene
# em um dicionário: cabeçalho da
# sequência como a chave e a sequência como valor

arquivo = open("seq.fasta")

linhas = arquivo.readlines()
mulifasta = {}

for linha in linhas:

    if linha[0] == ">":
        seq_atual = linha.strip()
        mulifasta[seq_atual] = ""
    else:
        mulifasta[seq_atual] = mulifasta[seq_atual] + linha.strip()

print(mulifasta)

print(mulifasta[">seq1"])
print(mulifasta[">seq2"])
print(mulifasta[">seq3"])
print(mulifasta[">seq4"])



