#!python3
from mysql.connector import ProgrammingError
from db import nova_conexao

excluir_tabela = "DROP TABLE emails"

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(excluir_tabela)
        print('Tabela excluida')

    except ProgrammingError as erro:
        print(f'Erro: {erro.msg}')