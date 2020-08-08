# Escreva um programa que compare se
# duas sequências digitadas pelo usuário são iguais.


def verifica_igualdade(x, y):
    if x == y:
        print('São iguais!!')
    else:
        print('São diferentes!!')


valor = int(input("Digite um numero: "))
valor2 = int(input("Digite outro numero: "))

verifica_igualdade(valor, valor2)
