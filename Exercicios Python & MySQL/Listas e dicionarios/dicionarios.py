meu_dicionario = {"A": "ricardo", "B": "fernando", "C": "alexandre"}

# Imprime a chave do dicionario
print(meu_dicionario["A"])
print(meu_dicionario["B"])
print(meu_dicionario["C"])

print("-=" * 20)

# Imprime os valores do dicionario
for chave in meu_dicionario:
    print(meu_dicionario[chave])

print("-=" * 20)

# Imprime a chave e os valores do dicionario
for chave in meu_dicionario:
    print(chave + "-" + meu_dicionario[chave])

print("-=" * 20)
# Converte os dicionarios em tuplas
for i in meu_dicionario.items():
    print(i)

print("-=" * 20)
# retorna somente os valores
for i in meu_dicionario.values():
    print(i)

print("-=" * 20)
# retorna somente as chaves
for i in meu_dicionario.keys():
    print(i)
