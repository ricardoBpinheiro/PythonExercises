#Lê a DN de sete pessoas e mostra quantas pessoas ainda nao
# tem 18 anos e quantas ja sao maiores

tot = 0
tot2 = 0
for i in range(1, 8):
    dn = int(input('Informe a DN da {}° pessoa: '.format(i)))
    idade = 2019 - dn
    if idade >= 21:
        tot += 1
    else:
        tot2 += 1
print('{} pessoas ainda nao sao maiores de idade'.format(tot2))
print('{} pessoas sao maiores de idade'.format(tot))
