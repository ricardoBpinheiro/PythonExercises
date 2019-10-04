nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua media foi {:.1f}'.format(media))
print('Parabens' if media >= 7 else 'Estuda mais!')
