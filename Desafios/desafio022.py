#Programa que lê o nome completo de uma pessoa e mostra:
# -Nome com todas as letras maiusculas
# -Nome com todas as letras minusculas
# -Quantas letras ao tod o (sem considerar espaços)
# -Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))

print('Maiuscula:', nome.upper())
print('Minuscula:', nome.lower())
print('Sem espaços:', len(nome.replace(' ', '')))
dividido = nome.split()
print('Primeiro nome', len(dividido[0]))