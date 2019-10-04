celsius = float(input('Digite o valor os graus em C°: '))
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15
rankine = celsius * 9/5 + 491.67
print('A temperatura convertida é de {:.2f} fahrenheit'.format(fahrenheit))
print('A temperatura convertida é de {:.2f} kelvin'.format(kelvin))
print('A temperatura convertida é de {:.2f} rankine'.format(rankine))
