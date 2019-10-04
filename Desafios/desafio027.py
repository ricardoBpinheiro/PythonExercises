#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.

nome = str(input('Digite seu nomem completo: ')).strip()

dividido = nome.split()

print('Primeiro nome: {}'.format(dividido[0]))
print('Ultimo nome: {}'.format(dividido[len(dividido)-1]))
