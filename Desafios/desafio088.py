import random
import time

lista = list()
jogos = list()
total = 1

print('-' * 30)
print(' ' * 5, 'JOGA NA MEGA SENA')
print('-' * 30)

quantidade = int(input('Quantos jogos voce quer que eu sorteie? '))
print('-=' * 3, f' SORTEANDO {quantidade} JOGOS ', '-=' * 3)

while total <= quantidade:
    cont = 0
    while True:
        numeros = random.randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            cont += 1
        if cont >= 6:   # Se ja sorteou 6 numeros
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)
print('-=' * 5, ' BOA SORTE ', '-=' * 5)
