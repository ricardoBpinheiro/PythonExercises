#Programa que calcula o preço de uma viagem
# viagens de até 200km sao cobradas R$0.50
# viagens mais longas são cobradas R$0.45

dist = int(input('Digite a distancia da viagem: '))

if dist > 200:
    preco = dist * 0.45
    print('O preço de uma viagem de {}kms é de R${}'.format(dist, preco))
else:
    preco = dist * 0.50
    print('O preço de uma viagem de {}kms é de R${}'.format(dist, preco))
