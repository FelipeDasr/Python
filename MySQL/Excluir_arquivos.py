from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'DELETE FROM contatos WHERE nome = %s'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(sql)
        cursor.execute(sql, ('Pedra',))
        conexao.commit()

    except ProgrammingError as erro:
        print(f'Erro: {erro.msg}')

    else:
        print(f'{cursor.rowcount} registros deletados!!')