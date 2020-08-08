# recebe soma de todos valores de uma lista

from functools import reduce


def soma(x, y):
    return x + y


lista = [1, 3, 5, 10, 20]

# reduce(função, valores)
soma = reduce(soma, lista)
print(soma)
