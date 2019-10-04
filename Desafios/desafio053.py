#Programa verifica se a frase é um palindromo
#Desconsiderar os espaços e acentos
#string[inicio:fim:passo]
txt = str(input('Digite uma frase: ').lower()).strip()

correcao = txt.replace(' ', '')
correcao2 = correcao[::-1]

if correcao == correcao2:
    print('A frase {} é um palindromo'.format(txt))
else:
    print('A frase nao é um palindromo')