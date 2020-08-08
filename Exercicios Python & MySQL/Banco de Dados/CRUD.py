import MySQLdb

host = "localhost"
user = "root"
password = ""
db = "escola"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

# c = con.cursor()  # Pega resultados e faz consultas
c = con.cursor(MySQLdb.cursors.DictCursor)  # Transforma as consultas em dicionarios


def select(fields, tables, where=None):  # campos, tabelas e where(nao obrigatorio) para fazer as consultas
    global c

    # SELECT (fields) FROM <tables>
    query = "SELECT " + fields + " FROM " + tables
    if where:
        query = query + " WHERE " + where

    c.execute(query)  # executa a query
    return c.fetchall()  # pega todos resultados e mostra na função


def insert(values, table, fields=None):  # Lista, tabela, caso quiser os fields
    global c, con  # precisa da con= conexao para fazer o commit

    # INSERT INTO <table> (fields) VALUES (),(),()
    # VALUES (...), (...),
    query = "INSERT INTO " + table
    if fields:  # se fields foi passado
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])  # Retorna os valores no parenteses que vao ser divididas por virgulas
    print(query)

    c.execute(query)  # executa a query
    con.commit()  # Insere no banco


def update(sets, table, where=None):
    # UPDATE table
    # SET field = value, field = value
    # WHERE

    global c, con  # c transforma em um dicionario
    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])  # Cada campo é separado por virgula no update

    if where:
        query = query + " WHERE " + where

    c.execute(query)  # executa a query
    con.commit()  # Insere no banco
    print(query)


def delete(table, where):  # Where é obrigatorio
    # DELETE FROM table
    # WHERE where
    global c, con

    query = "DELETE FROM " + table + " WHERE " + where
    c.execute(query)  # executa a query
    con.commit()


print("SELECT")
resultado = select("nome, cpf", "alunos", )
print(resultado[0]["nome"])
print(resultado[0]["cpf"])
print("O primeiro dado no BD é nome: " + resultado[0]["nome"] + " e CPF: " + resultado[0]["cpf"])

print("-=" * 50)
print("INSERT")
values = ["DEFAULT, 'Joao Pedro', '2000-01-01', 'Av louca, 123', 'Jaras do Sul', 'SC', '1234567891'",
          "DEFAULT, 'Maria Pedro', '2000-01-01', 'Av louca, 123', 'Jaras do Sul', 'SC', '1234567892'"]
insert(values, "alunos")

# print(select("*", "alunos"))  # Mostra todas colunas da tabela alunos

print("-=" * 50)
print("UPDATE")
# print(select("*", "alunos", "id_aluno = 8"))  # Busca o aluno com ID=8 na tabela alunos
update({"nome": "João Martins", "cidade": "Curitiba"}, "alunos", "id_aluno = 8")
print(select("*", "alunos", "id_aluno = 8"))

print("-=" * 50)
print("DELETE")
print(select("*", "alunos", "id_aluno = 9"))
delete("alunos", "id_aluno = 9")  # Deleta aluno com id 9
print(select("*", "alunos", "id_aluno = 9"))

