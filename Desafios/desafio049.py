#Tabuada

num = int(input('Digite um valor: '))

print('-='*7)
print(' Tabuada do {}'.format(num))
print('-='*7)
for i in range(1, 10+1):
    print('  {} x {} = {}'.format(i, num, num*i))
print('-='*7)