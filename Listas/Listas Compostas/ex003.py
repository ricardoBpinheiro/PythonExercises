galera = list()
dado = list()
totalmaior = totalmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # Cria uma copia da lista galera
    dado.clear()

for pessoa in galera:  # Para cada pessoa na lista
    if pessoa[1] >= 21:   # pessoa[0] = nome / pessoa[1] = idade
        print(f'{pessoa[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totalmenor += 1
print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade')