#Lê o peso de 5 pessoas e mostra o maior e o menor peso

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Digite o {}° peso: '.format(i)))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('Maior Peso: {}kg'.format(maior))
print('Menor peso: {}kg'.format(menor))
