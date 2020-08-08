w = open("arquivo2.txt", "w")  # abre arquivo arquivo
w2 = open("arquivo3.txt", "a")  # adiciona texto toda vez que executa

w.write("Esse é o meu arquivo brabo")  # escreve texto dentro do arquivo
w2.write("Esse é o meu arquivo brabo\n")

w.close()  # Fecha arquivo
