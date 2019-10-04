#Programa que verifica 3 retas e diz se é um triangulo
print('-='*20)

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print('As retas formam um triagulo')
else:
    print('As retas não formam um triangulo')
