#Programa que verifica se o ano é bissexto

ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print('{} é bissexto'.format(ano))
else:
    print(('{} não é bissexto'.format(ano)))