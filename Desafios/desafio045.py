# Programa que faz o computador jogar jokenpô

import random
import time

print('-='*5)
print('1-Pedra\n'
      '2-Papel\n'
      '3-Tesoura')
print('-='*5)
escolha = int(input('>'))
pc = random.randint(1, 3)

print('-=' * 10)
print('Jo')
time.sleep(1)  # pausa de 1 segundo
print('Ken')
time.sleep(1)
print('Po')

if pc == 1 and escolha == 2:
    print('-=' * 10)
    print('Computador joga Pedra')
    print('Você Ganhou!!!')
elif pc == 1 and escolha == 3:
    print('-=' * 10)
    print('Computador joga Pedra')
    print('Você Perdeu')
elif pc == 2 and escolha == 1:
    print('-=' * 10)
    print('Computador joga Papel')
    print('Você Perdeu')
elif pc == 2 and escolha == 3:
    print('-=' * 10)
    print('Computador joga Papel')
    print('Você ganhou')
elif pc == 3 and escolha == 1:
    print('-=' * 10)
    print('Computador joga Tesoura')
    print('Você Ganhou')
elif pc == 3 and escolha == 2:
    print('-=' * 10)
    print('Computador joga Tesoura')
    print('Você Perdeu')
