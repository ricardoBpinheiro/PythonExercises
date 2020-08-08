# funções lambda
# Cria uma função que so vai ser usada uma unica vez

valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor_dobrado = map(lambda i: i*2, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)

