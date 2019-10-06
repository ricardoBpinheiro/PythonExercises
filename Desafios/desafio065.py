# lê varios numeros
# no final mostra a media de todos e o maior e menor dos valores.
# O programa deve pedir se o usuario quer ou nao continuar a digitar

soma = 0
media = 0
cont = 0
n = 0
maior = 0
menor = 0
opcao = ''

while opcao != 'N':
    num = int(input('Digite um valor: '))
    opcao = str(input('Quer continuar [S/N]: ')).upper()
    cont += 1
    soma += num
    media = soma / cont

    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    if opcao == 'N':
        print('-=' * 10)
        print('{:.1f} -> Media'.format(media))
        print('{} -> Maior'.format(maior))
        print('{} -> Menor'.format(menor))
        print('-=' * 10)
