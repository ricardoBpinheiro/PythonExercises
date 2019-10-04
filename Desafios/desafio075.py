valores = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')),
           int(input('Digite o ultimo numero: ')))


print(f'Voce digitou os valores {valores}')
if 3 in valores:
    print(f'O valor 3 apareceu na posição {valores.index(3) + 1}')
else:
    print('O valor 3 não apareceu em nenhuma posição')
    
if 9 in valores:
    print(f'O valor 9 apareceu {valores.count(9)} vezes')
else:
    print('O valor 9 não apareceu em nenhuma posição')

print(f'Os valores pares foram:')
for n in valores:  # para cada valor em valores
    if n % 2 == 0:
        print(n, end=' ')
