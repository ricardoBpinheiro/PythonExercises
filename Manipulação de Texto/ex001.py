#string[inicio:fim:passo]

frase = 'Minha frase teste no Python'
frase1 = 'Curso em Video Python'

print(frase[3])       #Pega a quarta posição da String inteira
print(frase[3:13])    #Começa na quarta posição e termina na decima segunda
print(frase[:13])     #Começa da primeira posição e termina na decima segunda
print(frase[13:])     #Começa na decima terceira posição e termina na ultima
print(frase[1:15:2])  #Começa na primeira posição, termina na decima quarta e mostra os caracteres pulando de 2 em 2
print(frase[3::2])
print(frase[::2])
print(frase1.count('o')) #Conta quantos caracteres informados possue a string
print(frase1.upper())    #Joga tudo pra maiusculo
print(frase1.lower())    #Joga tudo pra minusculo
print(frase1.capitalize()) #Deixa apenas a primeira posição maiuscula e o resto minusculo
print(len(frase1.strip())) #len=length conta quantos posições possue a string
print(frase1.replace('Python', 'Texto')) #Troca a palavra pela a outra
print('Curso' in frase) #Se a String possue a palavra informada
print('Curso' in frase1) #Se a String possue a palavra informada
print(frase1.find('Curso')) #Mostra a posição de inicio da palavra/Caracter informado
print(frase1.find('Python')) #Mostra a posição de inicio da palavra/Caracter informado
print(frase1.lower().find('vídeo'))
print(frase1.split()) #Reparte cada palavra da String em mais Strings

dividido = frase1.split()
print('Curso' in dividido[0])
print(dividido[0])
print(dividido[0][3])

texto = 'Hello World.' # Invertendo palavras
print(texto[::-1])

print("""Lorem Ipsum is simply dummy text
of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s.""")

