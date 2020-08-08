# Escreva um programa que resolva uma equação de segundo grau.
from math import sqrt


def bhaskara1(d, e, delt):
    resultado = (-e + sqrt(delt)) / (2 * d)
    return resultado


def bhaskara2(d, e, delt):
    resultado = (-e - sqrt(delt)) / (2 * d)
    return resultado


a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a == 0:
    print("Equação invalida")
    exit()

# Equação Completa
if a != 0 and b != 0 and c != 0:
    delta = ((b ** 2) - 4 * a * c)
    print("-="*20)
    if delta > 0:
        x = bhaskara1(a, b, delta)  # (-b + sqrt(delta)) / (2 * a)
        x1 = bhaskara2(a, b, delta)  # (-b - sqrt(delta)) / (2 * a)
        print(f"A equação é completa e tem resultado de x': {x} e x'': {x1} ")
    elif delta == 0:
        # x = (a / (2*a))
        x = bhaskara1(a, b, delta)
        print(f"A equação possui uma raiz que é x {x}")
    else:
        print("A equação não possui raizes")

# Equação Incompleta 1 c = 0
if a != 0 and b != 0 and c == 0:
    delta = ((b ** 2) - 4 * a * c)
    print("-=" * 20)
    if delta > 0:
        x = bhaskara1(a, b, delta)  # (-b + sqrt(delta)) / (2 * a)
        x1 = bhaskara2(a, b, delta)  # (-b - sqrt(delta)) / (2 * a)
        print(f"A equação é incompleta e tem resultado de x': {x} e x'': {x1} ")
    elif delta == 0:
        # x = (a / (2*a))
        x = bhaskara1(a, b, delta)
        print(f"A equação possui uma raiz que é x {x}")
    else:
        print("A equação não possui raizes")

# Equação Incompleta 2 b = 0
if a != 0 and b == 0 and c != 0:
    delta = ((b ** 2) - 4 * a * c)
    print("-=" * 20)
    if delta > 0:
        x = bhaskara1(a, b, delta)  # (-b + sqrt(delta)) / (2 * a)
        x1 = bhaskara2(a, b, delta)  # (-b - sqrt(delta)) / (2 * a)
        print(f"A equação é incompleta e tem resultado de x': {x} e x'': {x1} ")
    elif delta == 0:
        # x = (a / (2*a))
        x = bhaskara1(a, b, delta)
        print(f"A equação possui uma raiz que é x {x}")
    else:
        print("A equação não possui raizes")

# Equação Incompleta 3 | b e c = 0
if a != 0 and b == 0 and c == 0:
    x = 0
    x1 = 0
    print(f"A equação é incompleta e tem resultado de x'{x} e x''{x1} ")


