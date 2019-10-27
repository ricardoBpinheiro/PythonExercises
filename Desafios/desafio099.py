def maior(* num):
    cont = mai = 0
    print('-=' * 30)
    print('Analisando os valores passados ')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado for {mai}')


maior(2, 4, 1, 3, 7, 3, 10)
maior(4, 6, 3, 1)
maior(2, 3, 1)
maior(5, 9)
maior(5)
maior()
