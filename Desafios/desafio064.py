# Programa Lê varios numeros inteiros, no final da execução
# mostra a media entre todos os valores e qual foi o maior e o menor
# o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores

n = 'N'
qtd = 0
soma = 0

while n != 'S':
    num = int(input('Digite um numero: '))

    qtd += 1
    soma += num
    media = soma / qtd
    if num > 0:
        opcao = str(input('Quer continuar [S/N]: ')).upper()

        #num2 = int(input('Digite um numero: '))


