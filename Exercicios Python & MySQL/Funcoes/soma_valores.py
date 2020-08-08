def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def divisao(x, y):
    return x / y


def multiplicacao(x, y):
    return x * y


s = soma(2, 3)
s1 = subtracao(2, 3)
d = divisao(2, 3)
m = multiplicacao(2, 3)

print(s)
print(s1)
print(d)
print(m)

print(soma(s, d))  # usa a função com valores de outras funcoes

