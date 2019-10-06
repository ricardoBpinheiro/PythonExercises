# Jogo de Par ou impar com o pc

import random

vitorias = 0
pc = 0
num = 0
escolha = ''
soma = 0

print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)

while True:
    num = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I] ')).upper()
    pc = random.randint(1, 10)
    soma = num + pc

    if escolha == 'P':
        if soma % 2 == 0:
            print('--' * 20)
            print(f'Voce jogou {num} e o computador {pc}. Total de {soma} DEU PAR')
            print('--' * 20)
            print('Você VENCEU!')
            vitorias += 1
            print('Vamos jogar novamente...')
            print('-=' * 20)
        else:
            print('--' * 20)
            print(f'Voce jogou {num} e o computador {pc}. Total de {soma} DEU IMPAR')
            print('--' * 20)
            print('Voce PERDEU!')
            if vitorias > 1:
                print(f'GAME OVER! Voce venceu {vitorias} vezes')
                break
            elif vitorias == 0:
                print(f'GAME OVER! Voce nao venceu nenhuma vez')
                break
            else:
                print(f'GAME OVER! Voce venceu {vitorias} vez')
                break

    if escolha == 'I':
        if soma % 2 != 0:
            print('--' * 20)
            print(f'Voce jogou {num} e o computador {pc}. Total de {soma} DEU IMPAR')
            print('--' * 20)
            print('Você VENCEU!')
            vitorias += 1
            print('Vamos jogar novamente...')
            print('-=' * 20)
        else:
            print('--' * 20)
            print(f'Voce jogou {num} e o computador {pc}. Total de {soma} DEU PAR')
            print('--' * 20)
            print('Voce PERDEU!')
            if vitorias > 1:
                print(f'GAME OVER! Voce venceu {vitorias} vezes')
                break
            elif vitorias == 0:
                print(f'GAME OVER! Voce nao venceu nenhuma vez')
                break
            else:
                print(f'GAME OVER! Voce venceu {vitorias} vez')
                break
