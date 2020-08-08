# Escreva um programa que ordene
# uma lista numérica com três elementos.

num = []

for i in range(3):
    num.append(int(input(f"Digite o {i+1}° numero: ")))
    num.sort()

print(f"Numeros em ordem crescente {num}")

