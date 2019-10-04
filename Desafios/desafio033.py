#lê 3 numeros e mostra o maior e menor entre eles

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num1 > num2 and num1 > num3 and num2 > num3:
    print('O numero maior entre eles é {}'.format(num1))
    print('O numero menor entre eles é {}'.format(num2))
if num1 > num2 and num1 > num3 and num3 > num2:
    print('O numero maior entre eles é {}'.format(num1))
    print('O numero menor entre eles é {}'.format(num3))
if num2 > num1 and num2 > num3 and num1 > num3:
    print('O numero maior entre eles é {}'.format(num2))
    print('O numero menor entre eles é {}'.format(num3))
if num2 > num1 and num2 > num3 and num3 > num1:
    print('O numero maior entre eles é {}'.format(num2))
    print('O numero menor entre eles é {}'.format(num1))
if num3 > num1 and num3 > num2 and num1 > num2:
    print('O numero maior entre eles é {}'.format(num3))
    print('O numero menor entre eles é {}'.format(num2))
if num3 > num1 and num3 > num2 and num2 > num1:
    print('O numero maior entre eles é {}'.format(num3))
    print('O numero menor entre eles é {}'.format(num1))