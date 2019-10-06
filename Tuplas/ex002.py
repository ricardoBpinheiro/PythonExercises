lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'

for comida in lanche:
    print(f'{comida}')
print('\n')

for cont in range(0, len(lanche)):
    print(lanche[cont])

print('\n')
for pos, comida in enumerate(lanche):
    print(f'{comida}')