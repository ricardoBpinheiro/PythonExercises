# zip = compactar listas

lista1 = [1, 2, 3, 4, 5]
lista2 = ["celular", "computador", "impressora", "controle", "monitor"]
lista3 = ["R$ 1000", "R$ 2000", "R$ 600", "R$ 200"]

# Concatena a lista1 com a lista2
# posição 0 das listas vao ficar na mesma linha
for numero, nome in zip(lista1, lista2):
    print(numero, nome)

print("-=" * 30)
# Concatena 3 listas
for numero, nome, preco in zip(lista1, lista2, lista3):
    print(numero, nome, preco)
