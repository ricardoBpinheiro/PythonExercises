times = 'Flamengo', 'Palmeiras', 'Santos', 'Corinthians',\
        'Internacional', 'Bahia', 'São Paulo',\
        'Gremio', 'Ahletico-PR', 'Atletico', 'Goiás', 'Botafogo',\
        'Fortaleza', 'Vasco', 'Ceará', 'Fluminense',\
        'Cruzeiro', 'CSA', 'Avai', 'Chapecoense'

print(times)
print('-='*20)
print(f'5 Primeiros colocados: {times[:5]}')
print('-='*20)
print(f'5 Ultimos colocados: {times[15:]}')
print('-='*20)
print(f'Ordem alfabetica: {sorted(times)}')
print('-='*20)
print('Chape esta na posição', times.index('Chapecoense'))

