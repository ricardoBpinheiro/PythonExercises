# Programa que aprova o emprestimo bancario para a compra de uma casa
# Pede o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# Calcula o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario
# ou entao o emprestimo sera negado

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
ano = int(input('Quantos anos vai pagar: '))

prestacao = casa / (ano * 12)
porcentagem = (salario * 30) / 100

if prestacao > porcentagem:
    print('Você nao pode pegar o emprestimo')
    print('Prestação vai ser muito cara {:.2f}'.format(prestacao))
else:
    print('Voce pode pegar o emprestimo')
    print('Vai ficar {:.2f} cada mes por {} anos'.format(prestacao, ano))