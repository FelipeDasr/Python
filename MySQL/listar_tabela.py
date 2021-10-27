#!python3
from db import nova_conexao

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute("SHOW TABLES")

    for i, tables in enumerate(cursor):
        print(f'- {tables[0]}')