#Programa lê um numero inteiro e pede para o usuario
# qual será a base de conversão
# 1 para binario
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um valor inteiro: '))
print('-='*20)
print(' - 1 para binario\n',
      '- 2 para octal\n',
      '- 3 para hexadecimal')
print('-='*20)
base = int(input('Qual a base de conversão: '))

if base == 1:
    binario = bin(num)[2:]  #[2:] começa da segunda posição e vai ate o final
    print('Valor de {} em binario: {}'.format(num, binario))
elif base == 2:
    octal = oct(num)[2:]
    print('Valor de {} em octal: {}'.format(num, octal))
elif base == 3:
    hexa = hex(num)[2:]
    print('Valor de {} em hexadecimal: {}'.format(num, hexa))
else:
    print('Escolha uma opção valida')