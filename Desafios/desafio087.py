matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
somacoluna = 0
maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            somacoluna += matriz[i][j]
        if i == 1:
            maior = matriz[i][j]
            if matriz[i][j] > maior:
                maior = matriz[i][j]
print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somacoluna}')
print(f'O maior valor da segunda linha é {maior}')
