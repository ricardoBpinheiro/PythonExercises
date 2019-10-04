# programa lê o primeiro termo e a razão de um Progressão aritmetica
# mostra os 10 primeiros termos dessa progressão
# A = a1 + (n - 1) * r

num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
pa = 0

print('A PA dos valores informados')
for i in range(1, 11):
    pa = num + (i - 1) * razao
    print('{}° - {}'.format(i, pa))