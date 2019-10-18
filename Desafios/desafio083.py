# Digite a expressão: ((a+b)*c)(x+y(3+2/3)*z)
# Para cara '(' na expressão ele adiciona na pilha
# quando é encontrado um ')' ele remove o ultimo valor da pilha, ou seja encontrou o par
# no final se todos valores forem removidos da pilha a expressão é valida
expressao = str(input('Digite a expressão: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()  # Remove o ultimo valor da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida!')
else:
    print('Sua expressão esta invalida!')

# lista = 0
# lista1 = 0
# expressao = str(input('Digite a expressão: '))
#
# for c in expressao:
#     if c in '(':
#         lista += 1
#     if c in ')':
#         lista1 += 1
#
# if lista == lista1:
#     print('Sua expressão é valida!')
# else:
#     print('Sua expressão é invalida!')
