#Lê 6 valores e soma os pares, os impares desconsidera
soma = 0
for i in range(1, 6+1):
    num = int(input('Digite o {}° valor: '.format(i)))
    if num % 2 == 0:
        soma += num
print('A soma dos valores pares é {}'.format(soma))