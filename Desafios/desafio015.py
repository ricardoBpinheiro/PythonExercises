#Aluguel de carro
dias = int(input('Informe a quantidade de dias: '))
kmRodados = int(input('Informe os kms rodados: '))

valortotal = (dias * 60) + (kmRodados * 0.15)

print('O valor total do aluguel é de {:.2f} reais'.format(valortotal))
