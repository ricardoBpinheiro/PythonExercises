aluno = list()
n = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], media])

    opcao = str(input('Quer continuar? [S/N] ')).upper()

    if opcao == 'N':
        print('-=' * 30)
        break

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 15)
for i, l in enumerate(aluno):
    print(f'{i:<4} {l[0]:<10} {l[2]:>7}')
print('--' * 15)

while True:
    n = int(input('Mostrar notas de qual aluno: (999 interrompe): '))
    if n == 999:
        print('--' * 20)
        print('FINALIZANDO')
        break
    if n <= len(aluno) - 1:    # numero do aluno nao pode ser menor que a quantidade de alunos na lista
        print(f'Notas de {aluno[n][0]} são {aluno[n][1]}')
