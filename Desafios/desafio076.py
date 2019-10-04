n = 0

listagem = ('Lapis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Penal', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('--' * 20)
print(' ' * 10, 'LISTAGEM DE PREÇOS')
print('--' * 20)

for n in range(0, len(listagem)):
    if n % 2 == 0:
       print(f'{listagem[n]:.<30}R${listagem[n+1]}')
    #if n % 2 == 1:
    #  print(f'{listagem[n]:30}')

print('--' * 20)
