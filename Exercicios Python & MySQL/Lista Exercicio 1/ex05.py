# Escreva um programa que receba dois números
# e um sinal, e faça a operação matemática definida pelo sinal.

n1 = float(input("Digite o 1° numero: "))
n2 = float(input("Digite o 2° numero: "))

sinal = str(input("Informe a operação matematica: "))

if n1 == 0 and n2 == 0:
    print("Não é possivel realizar divisão por zero")
    exit()
else:
    if sinal in "+,-,/,%,*":
        if sinal == "+":
            print(f"O resultado {n1 + n2}")
        if sinal == "-":
            print(f"O resultado {n1 - n2}")
        if sinal == "/":
            print(f"O resultado {n1 / n2}")
        if sinal == "%":
            print(f"O resultado {n1 % n2}")
        if sinal == "*":
            print(f"O resultado {n1 * n2}")
    else:
        print("Operação não reconhecida")
        exit()
