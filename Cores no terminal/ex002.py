nome = 'Ricardo'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Eae, tranquilo, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
print('Eae, tranquilo, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))
print('Eae, tranquilo, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))