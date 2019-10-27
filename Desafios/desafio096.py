def calculaarea(l, c):
    a = l * c
    print(f'A area de um terrono {l}x{c} é de {a}m²')


print('Controle de Terrenos')
print('--' * 15)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calculaarea(largura, comprimento)
