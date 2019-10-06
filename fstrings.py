nome = 'Ricardo'
idade = 67
salario = 11937.373434

print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')

print(f'O {nome} tem {idade} anos')  #Python 3.6+
print('O {} tem {} anos'.format(nome, idade))  #Python 3
print('O %s tem %d anos' % (nome, idade))  #Python 2

