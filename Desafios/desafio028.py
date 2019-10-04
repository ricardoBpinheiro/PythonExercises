#Computador gera um numero aleatorio de 0 a 5
#Usuario insere um numero nesse range e o programa analisa se o usuario acertou
import random

num = int(input('Digite um numero entre 0 e 5: '))

if num >= 0 and num < 6:
    numcom = random.randint(0, 5)

    if num == numcom:
        print('O numero que vc escreveu esta correto :)')
    else:
        print('Voce errou, o nr certo era {}'.format(numcom))
else:
    print('Numero invalido :P ')