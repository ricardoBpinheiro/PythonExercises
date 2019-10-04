#Programa lê um numero de 0 a 9999 e mostra cada um dos digitos separados
# Ex: 1834
# Unidade: 4, Dezena: 3 , Centena: 8, Milhar: 1

#Explicação da formula
# Divisão inteira
# 1234 // 100 = 12
# 12 % 10 = 12/10 = 1
# sobra o valor 2

num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10 #Pega o numero faz a divisão inteira dele por 1 e depois pega o resto da divisao sendo divido por 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))