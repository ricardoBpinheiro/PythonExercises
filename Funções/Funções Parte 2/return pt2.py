def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'A fatorial de 5 é {f1}')
print(f'A fatorial de 4 é {f2}')
print(f'A fatorial de 0 é {f3}')
