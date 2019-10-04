# mostra os numeros pares entre 1 e 50

print('-=' *20)
print('Os valores pares de 1 a 50 são:')
for i in range(1, 51):
    if i % 2 == 0:
        print('{} é par'.format(i))
print('-=' *20)