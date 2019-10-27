def soma(a, b):
    s = a + b
    print(s)


def soma2(c, d):
    print(f'C = {c} e D = {d}')
    so = c + d
    print(f'A soma C + D = {so}')


def linha():
    print('--' * 30)


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a=3, b=997)

linha()

soma2(5, 5)
