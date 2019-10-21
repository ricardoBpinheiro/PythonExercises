pessoas = {'nome': 'Ricardo', 'sexo': 'M', 'idade': 22}
for k in pessoas.values():
    print(k)            # Printa os valores do dicionario
print('-=' * 10)

for k in pessoas.items():
    print(k)            # Printa os valores os itens do dic
print('-=' * 10)

for k, v in pessoas.items():
    print(f'{k} = {v}')     # Printa formatado dos valores com os itens
print('-=' * 10)

del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')     # Deletando um item do dicionario
print('-=' * 10)

pessoas['nome'] = 'Rodolfo'
for k, v in pessoas.items():    # Modificando o valor de um item
    print(f'{k} = {v}')
print('-=' * 10)

pessoas['peso'] = 60
for k, v in pessoas.items():   # Adicionando um item ao dicionario
    print(f'{k} = {v}')
