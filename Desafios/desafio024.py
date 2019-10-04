#Programa lê o nome da cidade e diz se ela começa ou nao com o nome "SANTO"

cidade = str(input('Digite o nome da cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')