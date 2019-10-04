# Programa que calcula a media de duas notas e verifica se ele passou

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print('Aprovado')
elif media < 5:
    print('Reprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')