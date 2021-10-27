from db import nova_conexao

sql = 'UPDATE contatos SET nome = %s WHERE id = %s'
args = ('Marcos', 3)

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql, args)
    conexao.commit()

    print(f'{cursor.rowcount} foram afetadas!!')