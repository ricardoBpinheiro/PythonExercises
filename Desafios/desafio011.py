altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))
area = altura * largura
qtdTinta = area / 2

print('A area total é {}m2'.format(area))
print('A quantidade de tinta gasta é {:.2f} litros'.format(qtdTinta))