#Prorgrama lê o nome de uma pessoa e diz se ela tem "Silva" no nome

nome = str(input('Digite seu nome: ')).strip()
maisculo = nome[::].upper()
print('SILVA' in maisculo)
