# Faz a comparação entre dois valores e ve qual é maior

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

if num1 > num2:
    print('O numero {} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} é maior que {}'.format(num2, num1))
else:
    print('Os valores são iguais')