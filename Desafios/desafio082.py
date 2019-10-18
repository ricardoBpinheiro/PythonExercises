lista = []
listapar = []
listaimpar = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    opcao = str(input('Quer continuar? [S/N] ')).upper()

    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)

    if opcao == 'N':
        print('-=' * 30)
        print(f'Lista: {lista}')
        print(f'Lista Par: {listapar}')
        print(f'Lista Impar: {listaimpar}')
        break
