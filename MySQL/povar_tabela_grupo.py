from db import nova_conexao

sql = """
    INSERT INTO grupos(descricao)
    VALUES (%s)
"""

args = (
    ('familia',),
    ('trabalho',),
)

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.executemany(sql, args)
    conexao.commit()

    print(f'{cursor.rowcount} linhas foram afetadas')