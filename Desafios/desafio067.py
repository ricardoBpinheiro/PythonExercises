#Tabuada

num = 0
i = 1
total = 0
while True:
    num = int(input('Quer ver a tabuada de qual numero: '))
    if num < 0:
        break
    print('-=' * 20)
    while i <= 10:
        total = num * i
        print(f'{num} x {i} = {total}')
        i += 1
    print('-=' * 20)
    i = 1
print('Acabou')
