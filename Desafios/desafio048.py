#Calcula a soma de todos impares que são multiplos de tres no intervalo de 1 até 500
soma = 0
for i in range(1, 501):
    if i % 2 == 0:  # se é pai
        par = 0
    elif i % 3 == 0:
        #i += i
        soma += i
print('A soma de todos os valores é {}'.format(soma))  # se é impar