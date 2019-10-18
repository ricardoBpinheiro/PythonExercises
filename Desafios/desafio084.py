pessoas = list()
dado = list()
cont = 0
maiorpeso = menorpeso = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))

    if len(pessoas) == 0:
        maiorpeso = dado[1]  # [1] Pega o peso
        menorpeso = dado[1]
    else:
        if dado[1] > maiorpeso:
            maiorpeso = dado[1]
        if dado[1] < menorpeso:
            menorpeso = dado[1]

    pessoas.append(dado[:])  # Cria uma copia da lista galera
    dado.clear()             # Limpa a lista secundaria
    cont += 1

    opcao = str(input('Quer continuar? [S/N] '))

    if opcao in 'nN':
        break
print(f'Ao todo, voce cadastrou {cont} pessoas')

print(f'Maior peso encontrado é {maiorpeso}, de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'{p[0]},')

print(f'Maior peso encontrado é {menorpeso}, de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'{p[0]},')

