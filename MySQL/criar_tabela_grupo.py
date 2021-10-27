from db import nova_conexao

sql_create = """
    CREATE TABLE IF NOT EXISTS grupos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(30)
    );
"""

sql_alter_0 = """
    ALTER TABLE contatos ADD grupo_id INT
"""

sql_alter_1 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES grupos(id)
"""

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql_create)
    cursor.execute(sql_alter_0)
    cursor.execute(sql_alter_1)

    cursor.execute('SHOW TABLES')
    
    for i, t in enumerate(cursor):
        print(f'{t[0]}')