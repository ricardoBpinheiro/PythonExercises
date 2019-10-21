import random
import time
import operator

jogo = {'jogador1': random.randint(1, 6),
        'jogador2': random.randint(1, 6),
        'jogador3': random.randint(1, 6),
        'jogador4': random.randint(1, 6)}

ranking = dict()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)
ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print('-=' * 30)
print(' =Ranking dos Jogadores= ')

for i, j in enumerate(ranking):
    print(f'    {i+1}° lugar: {j[0]} com {j[1]}')
    # time.sleep(1)
