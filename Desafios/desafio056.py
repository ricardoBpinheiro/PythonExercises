#Lê nome, idade e sexo de quatro pessoas e mostra
# A media de idade X
# O nome do homem mais velho
# Quantas mulheres tem menos de 20 anos X

maior = 0
menor = 0
media = 0
somaidades = 0
idadehomem = 0
nomehomem = ''
qtdmulher = 0

for i in range(1, 3):
    print('------ {}° Pessoa ------'.format(i))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): '))
    print('-='*20)
    somaidades += idade
    mediaidade = somaidades / 4
    if i == 1 and sexo in 'Mm':
        idadehomem = idade
        nomehomem = nome
    if sexo in 'Mn' and idade > idadehomem:
        idadehomem = idade
        nomehomem = nome

    if sexo == 'F' and idade < 20:
        qtdmulher += 1

print('A media das idades é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(idadehomem, nomehomem))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(qtdmulher))
