# Escreva um programa que compare se
# duas sequências digitadas pelo usuário são iguais.

import re

valor = input("Digite um numero: ")
valor2 = input("Digite outro numero: ")

busca = re.match(valor, valor2)

if busca:
    print('São iguais!!')
    print(busca.group())
else:
    print('São diferentes!!')
