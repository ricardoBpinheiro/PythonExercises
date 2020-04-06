# Criar um script que gerá um valor aleatoriamente, guarda este valor,
# e pergunta repetidamente para o usuário chutar o valor gerado até que ele acerte.

# Requisitos:
# Gravar Resposta do User   (x)
# Se o user chutou baixo    (x)
# Se o user chutou alto     (x)
# Se o User acertou         (x)
# Opção de desistir após 20 tentativas  (x)

import random

numeroaleatorio = random.randint(1, 100)
aux = []
i = 20
contavezes = 0
numerousuario = 0
while numerousuario != numeroaleatorio:
    numerousuario = int(input('\nAcerte o numero [1-100]: '))
    if numerousuario > 100 or numerousuario <= 0:
        print('Digite um valor entre 1 e 100 ')
    else:
        aux.append(numerousuario)
        if numerousuario == numeroaleatorio:  # se acertou
            print('-=' * 15)
            print('-= Parabens você acertou!!! -=')
            print('-=' * 15)
        else:  # se errou
            contavezes += 1
            if numerousuario > numeroaleatorio:
                print('CHUTOU ALTO!')
            if numerousuario < numeroaleatorio:
                print('CHUTOU BAIXO!')
            print('-=' * 16)
            print('-= Você errou tente novamente -=')
            print('-=' * 16)
            print('Os numeros chutados foram: ')
            for c, v in enumerate(aux):
                print(f'{v}', end=' ')
            print('')
            if len(aux) > 16:
                i += 2
                print('-=' * i)
            else:
                print('-=' * i)
            if contavezes > 30:
                resposta = str(input('Quer desistir? [S/N]: ')).upper()
                if resposta in 'SSIM':
                    print('Voce desistiu!')
                    print(f'O numero era {numeroaleatorio}')
                    exit()
