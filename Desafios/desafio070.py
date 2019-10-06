total = 0
mais1000 = 0
produtobarato = ''
precobarato = 0
cont = 0

print('--'*20)
print(' '*10, 'Loja Super Baratão', ' '*10)
print('--'*20)

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1

    if cont == 1:
        precobarato = preco
        produtobarato = produto
    else:
        if preco < precobarato:
            precobarato = preco
            produtobarato = produto

    if preco > 1000:
        mais1000 += 1

    opcao = ' '
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        print('-'*10, 'Fim do Programa', '-'*10)
        print(f'Total da Compra: R${total}')
        print(f'Temos {mais1000} produtos custando mais de R$1000')
        print(f'Produto mais barato foi {produtobarato} que custa R${precobarato}')
        break

