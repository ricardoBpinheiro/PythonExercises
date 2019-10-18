lista = []
for i in range(0, 5):
    num = (int(input(f'Digite o {i}° numero: ')))

    if i == 0 or num > lista[len(lista)-1]:
        lista.append(num)
        print('Adicionado na ultima posição da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor adicionado na posicao {pos}')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
