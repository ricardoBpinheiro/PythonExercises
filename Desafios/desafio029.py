# Programa lê a velocidade de um carro
# Se for maior que 80km/h ele leva multa
# Cada km acima do limite vai custar R$7,00

vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    multa = (vel - 80) * 7
    print('A velocidade registrada foi de {}, a multa é de {}R$'.format(vel, multa))
else:
    print('Velocidade no limite permitido')
