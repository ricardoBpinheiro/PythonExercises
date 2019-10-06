#Caixa eletronico

import math

aux = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
print('='*30)
print(' '*8, 'Gutty s Bank')
print('='*30)

valor = int(input('Que valor voce quer sacar: R$'))
while True:
    nota50 = valor / 50
    aux = valor % 50

    if aux == 0:
        break

    if aux > 0:

        nota20 = aux / 20
        aux = aux % 20

        nota10 = aux / 10
        aux = valor % 10

        nota1 = aux / 1
        break

if nota50 > 0:
    print(f'Notas de 50R$: {math.floor(nota50)}')

    if nota20 > 0:
        print(f'Notas de 20R$: {math.floor(nota20)}')

    if nota10 > 0:
        print(f'Notas de 10R$: {math.floor(nota10)}')

    if nota1 > 0:
        print(f'Notas de 1R$: {math.floor(nota1)}')
print('=' * 30)
print('Volte Sempre :)')

