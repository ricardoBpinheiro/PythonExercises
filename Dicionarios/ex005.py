estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # Copia os valores para dentro da lista
print(brasil)

print('-=' * 10)
for e in brasil:  # for para a lista
    for k, v in e.items():  # for para o dicionario
        print(f'O campo {k} tem valor {v}')

print('-=' * 10)
for e in brasil:  # for para a lista
    for v in e.values():  # for para o dicionario
        print(v, end=' ')
    print()
