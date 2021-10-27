#!python3
from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = """
    INSERT INTO contatos (nome, telefone)
    VALUES (%s, %s)
    """
args = ('Felipe', '99697-2895')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()

    except ProgrammingError as erro:
        print(f'Erro: {erro.msg}')

    else:
        print('Registro incluido!!, ID gerado', cursor.lastrowid)
