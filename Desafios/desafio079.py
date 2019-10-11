i = 0
lista = []
aux = 0

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Valor duplicado! Não adicionado.')

    opcao = str(input('Quer continuar? [S/N] ')).upper()

    if opcao == 'N':
        break

lista.sort()
print(f'Voce digitou os valores {lista}')
