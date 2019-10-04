nome = str(input('Qual o seu nome? '))
if nome == 'Ricardo':
    print('Que nome top!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Lucas':
    print('Que nome comum :p')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Nome feminino')
elif nome in 'Rogerio Roberto Ribas':
    print('Nome Masculino')
else:
    print('Nome normal :p')