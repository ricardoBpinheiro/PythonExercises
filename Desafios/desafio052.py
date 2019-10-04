#Programa verifica se o numero é primo

num = int(input('Digite um numero inteiro: '))
tot = 0

for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO numero {} for divisivel {} vezes'.format(num, tot))
if tot == 2: # Somente foi divido 2 vezes
    print('O numero é primo!!!')
else:
    print('O numero não é primo')
