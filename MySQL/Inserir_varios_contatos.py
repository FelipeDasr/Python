from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = """
    INSERT INTO contatos (nome, telefone)
    VALUES (%s, %s)
    """
args = (
    ('Feh', '3763-2436'),
    ('Lucia', '4141-2342'),
    ('Pedra', '1545-12343'),
    ('Joana', '7343-4231'),
    ('Claudia', '1231-1451'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()

    except ProgrammingError as erro:
        print(f'Erro: {erro.msg}')
    