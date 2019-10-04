#Programa que verifica se o jovem tem que se alistar no exercito

ano = int(input('Digite o ano de seu nascimento: '))
idade = 2019 - ano

if idade == 18:
    print('Você deve se alistar para o exercito')
elif idade < 18:
    falta = 18 - idade
    print('Faltam {} anos para você se alistar'.format(falta))
else:
    passou = idade - 18
    print('Ja se passaram {} anos de seu alistamento'.format(passou))