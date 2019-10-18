listaprincipal = list()
temp = list()
listapar = list()
listaimpar = list()

for i in range(1, 8):
    temp.append(int(input(f'Digite o {i}° numero: ')))

    if temp[0] % 2 == 0:
        listapar.append(temp[:])
        temp.clear()
        # print(listapar)
    else:
        listaimpar.append(temp[:])
        temp.clear()
        # print(listaimpar)

listaprincipal.append(listaimpar[:])
listaprincipal.append(listapar[:])

listaprincipal[0].sort()
listaprincipal[1].sort()
print(f'Os valores impares digitados foram: {listaprincipal[0]}')
print(f'Os valores pares digitados foram: {listaprincipal[1]}')

print('-=' * 30)

# Resposta :p
num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite p {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores pares digitados foram: {num[1]}')
