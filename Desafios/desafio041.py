#Programa verifica a categoria de um atleta pela idade

ano = int(input('Digite seu ano de nascimento: '))
idade = 2019 - ano

if idade <= 9:
    print('Mirim')
elif idade <= 14 and idade > 9:
    print('Infantil')
elif idade <= 19 and idade > 14:
    print('Junior')
elif idade <= 20 and idade > 19:
    print('Senior')
elif idade > 20:
    print('Master')