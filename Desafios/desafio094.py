lista = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO, Por favor, digite apenas M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO, Por favor, digite apenas S ou N')
    if opcao == 'N':
        break
print(lista)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
media = soma / len(pessoas)
print(f'B) A media de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da media: ', end='')
for p in lista:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('FIM')
