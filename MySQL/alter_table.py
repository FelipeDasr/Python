from mysql.connector import ProgrammingError
from db import nova_conexao

sql = 'ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        
    except ProgrammingError as erro:
        print(f'Erro: {erro}')