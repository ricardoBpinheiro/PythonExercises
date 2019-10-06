palavras = ('APRENDER', 'LER', 'ESTUDAR', 'PYTHON', 'RICARDO',
            'FUTURO', 'CALENDARIO', 'OUTUBRO', 'TRABALHAR',
            'SETEMBRO', 'TRINTA', 'BATATA', 'RODOLFO')

print('-='*20)
print(' '*10, 'CONTADOR DE VOGAIS')
print('-='*20)

for i in palavras:
    print(f'\nNa palavra {i} temos', end=' ')
    for letra in i:
        if letra in 'ÁÃÂAÉÊEIÍÓÕÔOÚÛU':
            print(f'{letra}', end=' ')
print('\n')
print('-='*20)
