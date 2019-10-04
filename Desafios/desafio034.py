#lê o salario e calcula o aumento
# salario acima de 1250 aumento de 10%
# salarios inferiores ou iguas a 1250 o aumento é de 15%

salario = float(input('Digite o salario: '))

if salario <= 1250:
    aumento = (salario * 15) / 100
    print('Salario com aumento de 15% {}'.format(salario+aumento))
else:
    aumento = (salario * 10) / 100
    print('Salario com aumento de 10% {}'.format(salario+aumento))