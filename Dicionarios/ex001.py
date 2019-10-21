# Tuplas ()
# Listas []
# Dicionarios {}

# dados = dict()
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'   # Acrescenta mais um elemento 'sexo' no dicionario
print(dados.values())  # Mostra todos valores do dicionario
print(dados.keys())   # Mostra as chaves do dicionario
print(dados.items())
del dados['idade']  # Deleta o elemento idade
