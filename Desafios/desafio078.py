valores = []
cont = 0
maior = 0
menor = 0

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))
    cont += 1

    if cont == 1:
        menor = valores[i]
        maior = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

print(f'Você digitou os valores {valores}')

print(f'Maior: {maior} nas posicoes ', end='')
for j, v in enumerate(valores):
    if v == maior:
        print(f'{j}... ', end='')

print()

print(f'Menor: {menor} nas posicoes ', end='')
for j, v in enumerate(valores):
    if v == menor:
        print(f'{j}... ', end='')

