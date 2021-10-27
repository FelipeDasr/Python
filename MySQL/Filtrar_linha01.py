from db import nova_conexao

sql = 'SELECT * FROM contatos WHERE telefone = "99697-2895"'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)