import time
import random

lista = list()

j = 0


def maior():
    cont = 0
    mai = 0
    cont += 1
    print('-=' * 30)
    print('Analisando os valores passados')
    num = random.randint(1, 10)
    for i in range(1, num):
        numero = random.randint(1, 10)
        lista.append(numero)
        if cont == 1:
            mai = numero[i]
        else:
            if numero[i] > mai:
                mai = numero[i]

    print(f'{lista} foram informados {len(lista)} valores')
    print(f'O maior valor informado foi {mai}')
    lista.clear()
    cont += 1


while True:
    maior()
    j += 1
    if j == 6:
        break
