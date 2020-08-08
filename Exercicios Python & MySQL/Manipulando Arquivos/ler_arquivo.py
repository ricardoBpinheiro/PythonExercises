arquivo = open("arquivo.txt")
arquivo2 = open("arquivo.txt")
arquivo3 = open("arquivo.txt")


# Leitura de arquivos
linhas = arquivo.readlines()  # passa pra variavel o conteudo do arquivo.txt
texto_completo = arquivo2.read()

print(linhas)
print("-=" * 20)
print(texto_completo)
print("-=" * 20)
for linha in linhas:
    print(linha)
print("-=" * 20)
