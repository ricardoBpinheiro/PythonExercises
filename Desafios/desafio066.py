n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um numero (999 para sair): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} valores é {soma}')