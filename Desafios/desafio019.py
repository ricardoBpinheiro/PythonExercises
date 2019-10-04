import random

aluno1 = str(input('Digite o primeiro aluno: '))
aluno2 = str(input('Digite o segundo aluno: '))
aluno3 = str(input('Digite o terceiro aluno: '))
aluno4 = str(input('Digite o quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]

print('Quem vai apagar o quadro é', random.choice(lista))
