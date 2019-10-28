def teste(b):
    global a
    a = 8
    b += 4                          # Escopo local
    c = 2                           # b=9 e c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5    # a vira 8
teste(a)                            # Escopo Global
print(f'A fora vale {a}')           # a=8
