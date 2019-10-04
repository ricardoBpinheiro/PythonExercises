# Melhorar o desafio028, o usuario vai tentar até acertar o numero
# no final mostrar quantas tentativas foram necessarias ate acertar o numero.

import random

num = 0
cont = 0
numcom = random.randint(0, 10)

while num != numcom:
    num = int(input('Digite um numero entre 0 e 10: '))
    if num != numcom:
        cont += 1
        print('Numero errado, tente novamente')
    if num == numcom:
        print('O numero {} que vc escreveu esta correto :)'.format(numcom))
        print('Foram {} tentativas até acertar'.format(cont+1))
