import time


def contagem(i, f, p):
    if p < 0:  # Se o passo for negativo, troca o sinal
        p *= -1
    if p == 0:   # Se o passo for 0, vira 1
        p = 1
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont -= p
        print('Fim!')


def linha():
    print('-=' * 30)


linha()
contagem(1, 10, 1)
linha()
contagem(10, 0, 2)
linha()

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

linha()
contagem(inicio, fim, passo)
