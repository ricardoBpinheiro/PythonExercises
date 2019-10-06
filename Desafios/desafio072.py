n = 0
numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', \
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze',\
          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',\
          'dezesete', 'dezoito', 'dezenove', 'vinte'

while True:
    n = int(input('Digite um numero entre 0 e 20: '))

    if n > 20 or n < 0:
        print('Tente Novamente')
    else:
        print(f'Voce digitou o numero {numeros[n]}')
        break

