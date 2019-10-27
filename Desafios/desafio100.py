from random import randint

numeros = list()


def sorteia():
    print(f'Sorteando {5} valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
        print(f'{num} ', end='', flush=True)
    print('Pronto')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia()
somapar(numeros)
