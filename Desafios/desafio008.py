valor = int(input('Digite o valor em metros: '))
kilometros = valor / 1000
hectometros = valor / 100
decametros = valor / 10
decimetros = valor * 10
centimetros = valor * 100
milimetros = valor * 1000

print('Valor em kilometros {} dm'.format(kilometros))
print('Valor em hectometros {} hm'.format(hectometros))
print('Valor em decametros {} dam'.format(decametros))
print('Valor em decimetros {} dm'.format(decimetros))
print('Valor em centimetros {} cm'.format(centimetros))
print('Valor em milimetros {} mm'.format(milimetros))