def teste(b):
    b += 4                          # Escopo local
    c = 2                           # b=9 e c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)                            # Escopo Global
print(f'A fora vale {a}')           # a=5
# print(f'B dentro vale {b}')  #Error
# print(f'C dentro vale {c}')  #Error
