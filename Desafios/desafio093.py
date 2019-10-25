jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome do Jogador: '))
num = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, num):
    valor = int(input(f'Quantos gols na partida {i+1}? '))
    gols.append(valor)

jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {num} partidas')
for i, j in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {j} gols')
print(f'Foi um total de {jogador["total"]} gols')
