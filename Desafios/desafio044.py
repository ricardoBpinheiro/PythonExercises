# Programa calcula o preço de um produto conforme a forma de pagamento

produto = float(input('Digite o preço do produto: '))
print('-='*20)
print(' 1 - para dinheiro/cheque (à vista)\n'
      ' 2 - para cartão (à vista)\n'
      ' 3 - para 2x cartão\n'
      ' 4 - para 3x ou + cartão (juros)')
print('-='*20)
forma = int(input('Digite a forma de pagamento: '))

dinheiro = (produto * 10) / 100  # desconto
cartao = (produto * 5) / 100     # desconto
parcela = (produto * 120) / 100  # juros + produto

if forma == 1:
    print('Valor do produto com 10% de desconto')
    print('Total: {}'.format(produto + dinheiro))
elif forma == 2:
    print('Valor do produto com 5% de desconto')
    print('Total: {}'.format(produto + cartao))
elif forma == 3:
    print('Valor do produto')
    print('Total: {}'.format(produto))
elif forma == 4:
    print('Valor do produto com 20% de juros')
    print('Total: {}'.format(parcela))
else:
    print('Opção invalida')


