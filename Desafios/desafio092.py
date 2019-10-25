import datetime

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.datetime.now().year - nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['ctps'] != 0:
    pessoa['anocontr'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['anocontr'] + 35) - datetime.datetime.now().year)

print('-=' * 30)

print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor de {v}')
