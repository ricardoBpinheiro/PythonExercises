cont = 0
lista = []
while True:
    num = int(input('Digite um valor: '))
    cont += 1
    lista.append(num)
    opcao = str(input('Quer continuar? [S/N] ')).upper()

    if opcao == 'N':
        lista.sort(reverse=True)
        print('-=' * 30)
        print(f'Voce digitou {cont} elementos')
        print(f'Os valores em ordem decrescente são {lista}')
        if 5 in lista:
            print('O valor 5 faz parte da lista!')
        else:
            print('O valor 5 não faz parte da lista!')
        break
