x = [1, 2, 3, 4, 5]
y = []

for elemento in x:
    y.append(elemento ** 2)

print(x)
print(y)

print("")
print("-=" * 30)
print("List Comprehension")
# w = [valor_a_adcionar laço condição]
z = [1, 2, 3, 4, 5]
w = [i ** 2 for i in z]

print(z)
print(w)

print("")
print("-=" * 30)
print("List Comprehension parte 2")  # Imprime os impares

h = [1, 2, 3, 4, 5]
f = [i for i in x if i % 2 == 1]
print(f)
