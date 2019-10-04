#Programa lê uma frase e mostra
# - Quantas vezes a letra 'a' aparece
# - Qual a primeira posição que ela aparece
# - Em qual posição ela aparece pela ultima vez

frase = str(input('Digite uma frase: ')).strip()

print('A letra "a" aparece: {}'.format(frase.lower().count('a')))
print('A primeira posição: {}'.format(frase.lower().find('a')))
print('A ultima posição: {}'.format(frase.lower().rfind('a')))