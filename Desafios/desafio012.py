produto = float(input('Informe o preço do produto: '))
desconto = (produto*5) / 100

print('O produto com 5% de desconto custa: {:.2f}'.format(produto - desconto))