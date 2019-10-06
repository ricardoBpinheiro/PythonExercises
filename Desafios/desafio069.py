
idade = 0
opcao = ''
sexo = ''
mulheres = 0
homens = 0
total = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo: [M/F] ')).upper()
        if sexo == 'F' and idade < 20:
            mulheres += 1
            print('DEU BOAAA, MULHER')
        if sexo == 'M':
            print('DEU BOAAA, HOMEM')
            homens += 1
    print('-' * 20)

    if idade > 18:
        total += 1

    opcao = ' '
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer Continuar? [S/N] ')).upper()

    if opcao == 'N':
        print(f'Total de pessoas com mais de 18 anos: {total}')
        print(f'Ao todo temos {homens} homens cadastrados')
        print(f'E temos {mulheres} mulheres com menos de 20 anos')
        break
