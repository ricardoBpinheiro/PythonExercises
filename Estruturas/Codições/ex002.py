nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua media foi {:.1f}'.format(media))

if media >= 7:
    print('Media boaaa')
else:
    print('Voce é burro')