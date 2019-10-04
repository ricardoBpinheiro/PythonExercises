#Programa que verifica 3 retas e diz se é um triangulo e que tipo
print('-='*20)

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    if reta1 == reta2 == reta3:
        print('Triangulo Equilatero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Triangulo Isosceles')
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print('Triangulo Escaleno')
else:
    print('As retas não formam um triangulo')
