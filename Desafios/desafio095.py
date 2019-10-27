jogador = dict()
gols = list()
listajogador = list()

while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    num = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, num):
        valor = int(input(f'Quantos gols na partida {i+1}? '))
        gols.append(valor)
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    gols = []
    listajogador.append(jogador.copy())

    while True:
        opcao = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if opcao in 'NS':
            break
        print('ERRO, Por favor, digite apenas S ou N')
    if opcao == 'N':
        break
    print('--' * 30)
print('-=' * 30)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 30)
for k, v in enumerate(listajogador):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 30)

while True:
    num = int(input('Mostrar dados de qual jogador? '))
    if num == 999:
        print('<FINALIZANDO>')
        break
    if num >= len(listajogador):
        print(f'Error, não existe jogador com o codigo {num}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {listajogador[num]["nome"]}')
        for i, g in enumerate(listajogador[num]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('--' * 30)
print('Finalizando!')
