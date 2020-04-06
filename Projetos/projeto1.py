# Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir)
# e permitir que o usuário rode o script quantas vezes quiser.

import random
import time

resposta = str(input('Você gosta de jogar dados? '))

c = 'SIM'
while c == 'SIM':
    if resposta in 'simsSimSIM':
        print('Rodando o dado!')
        time.sleep(1)
        print(random.randint(1, 6))
        c = str(input('Quer continuar jogando?[sim/não] ')).upper()
        if c == 'NÃO':
            print('Blz, vaza daqui então ;-;')
            exit()
    else:
        print('Blz, vaza daqui então ;-;')
        exit()
print('Blz, vaza daqui então ;-;')
