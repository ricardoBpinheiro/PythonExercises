# Ex: \033[0;33;44m
#
#
#  Styles (Estilo dos caracteres)
#   0 = none
#   1 = bold
#   4 = underline
#   7 = negative
#
#  Text (Cor do texto)
#   30 = Branco
#   31 = Vermelho
#   32 = Verde
#   33 = Amarelo
#   34 = Azul
#   35 = Magenta
#   36 = Ciano
#   37 = Cinza
#
#   Back (Cor de fundo)
#   40 = Branco
#   41 = Vermelho
#   42 = Verde
#   43 = Amarelo
#   44 = Azul
#   45 = Magenta
#   46 = Ciano
#   47 = Cinza

print('\033[4;30;43mOlá, Mundo!\033[m')
print('\033[1;32;45mOlá, Mundo!\033[m')
print('\033[7;40mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
