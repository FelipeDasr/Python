from db import nova_conexao

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute('SELECT telefone, nome FROM contatos')

    print(cursor.fetchone())