from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from contextlib import contextmanager

parametros = dict(
    host = 'localhost',
    port = '3306',
    user = 'root',
    passwd = 'felipe12',
    database = 'agenda'
)

@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if(conexao and conexao.is_connected()):
            conexao.close()