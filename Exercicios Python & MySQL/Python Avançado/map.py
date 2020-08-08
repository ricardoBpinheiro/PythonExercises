# map = pega uma função e aplica a todos elementos de uma lista


def dobro(x):
    return x*2


valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# duas copias de listas
print(dobro(valor))

print("-=" * 30)
print("Função map")
print(list(map(dobro, valor)))

print("-=" * 30)
print("Função map")

valor_dobrado = map(dobro, valor)

for i in valor_dobrado:
    print(i)
