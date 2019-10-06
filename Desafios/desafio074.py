import random

numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), )

for i in numeros:
    print(f'{i} ', end='')

print(f'\nMaior numero -> {max(numeros)}')
print(f'Menor numero -> {min(numeros)}')

