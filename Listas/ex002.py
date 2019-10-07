num = [1, 3, 4, 2, 5]
num[2] = 20  # Adiciona o valor 20 na posição 2 da lista
print(num)

num.append(7)  # Adiciona o valor 7 no final da lista
print(num)

num.sort()   # Deixa a lista em ordem crescente
print(num)

num.sort(reverse=True)  # Deixa a lista em ordem decrescente
print(num)

print(f'Essa lista tem {len(num)} elementos')

num.insert(2, 0)  # Adiciona o 0 na posição 2 da lista
print(num)

num.insert(2, 2)  # Adiciona o 2 na posição 2 da lista
print(num)

num.pop(3)  # Elimina o elemento da posição 3 da lista
print(num)

num.remove(2)  # Elimina a primeira ocorrencia do valor 2
print(num)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 5')


