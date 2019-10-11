
cont = 0
maior = 0
menor = 0
i = 0

for i in range(0, 5):
    num = int(input('Digite um valor: '))
    cont += 1

    if cont == 1:
        maior = num
        menor = num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('-=' * 10)
print('{} -> Maior'.format(maior))
print('{} -> Menor'.format(menor))
print('-=' * 10)