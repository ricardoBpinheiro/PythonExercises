familia = [['Ricardo', 19], ['Terezinha', 54], ['Joel', 53], ['Fernando', 24], ['Alexandre', 27]]

# [['Ricardo', 19], ['Terezinha', 54], ['Joel', 53], ['Fernando', 24], ['Alexandre', 27]]
#       0       1         0        1       0    1         0        1         0        1
#           0                  1              2                3                  4

print(familia[0])    # Mostra a lista da posicao 0
print(familia[0][0])  # Vai na posicão 0 e pega a posicao 0
# Ricardo
print(familia[2][1])  # Vai na posicão 2 e pega a posicao 1
# 53
print(familia[4][0])  # Vai na posicão 4 e pega a posicao 0
# Alexandre
print('-=' * 10)
for pessoa in familia:
    print(pessoa)
print('-=' * 10)
for pessoa in familia:
    print(pessoa[0])
print('-=' * 10)
for pessoa in familia:
    print(pessoa[1])
print('-=' * 10)
for pessoa in familia:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')
