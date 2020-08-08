# Função enumerate

lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
    print(i, lista[i])

print("-=" * 30)
print("Enumerate")
# Retorna o valor de i e nome
for i, nome in enumerate(lista):
    print(i, nome)
