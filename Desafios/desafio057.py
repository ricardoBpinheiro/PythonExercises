#Programa lê o sexo de uma pessoa, mas so aceita 'M' e 'F'
#Caso nao seja esses valores, peça a digitação novamente
#até ter um valor correto

i = ''
while i != 'M' and i != 'F':
    i = str(input('Digite o sexo[M/F]: '))
    if i != 'M' and i != 'F':
        print('Digite um valor validooo')
print('Fim')
