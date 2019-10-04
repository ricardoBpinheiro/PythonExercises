# Sequencia de fibonacci
# 0 > 1 > 1 > 2 > 3 > 5 > 8 > 13

n = int(input('Quantos numeros? '))
cont = 0
i = 0
aux = 1
x = 0
print('-=' * 20)
print('Sequencia de Fibonacci com {} numeros'.format(n))
while cont < n:
    print('{} > '.format(i), end='')
    x = i
    i += aux
    aux = x
    cont += 1
