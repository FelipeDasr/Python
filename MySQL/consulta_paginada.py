from db import nova_conexao

sql = 'SELECT * FROM contatos LIMIT %s OFFSET %s'
args = (7, 2)

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql, args)

    print('\n'.join(str(contato) for contato in cursor.fetchall()))