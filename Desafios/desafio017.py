import math
catoposto = float(input('Informe o cateto oposto: '))
catadjacente = float(input('Informe o cateto adjacente: '))

print('A hipotenusa é {:.2f}'.format(math.hypot(catoposto, catadjacente)))