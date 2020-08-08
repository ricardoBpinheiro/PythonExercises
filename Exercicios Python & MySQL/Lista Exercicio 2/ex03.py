# Escreva um programa que receba
# uma sequência digitada pelo usuário
# e a salve num arquivo no formato fasta.

# from Bio import SeqIO

texto = input("Digite uma sequencia: ")
arquivo = open("sequencia.fasta", "w")

arquivo.write(">seq\n")
arquivo.write(texto)
arquivo.close()




