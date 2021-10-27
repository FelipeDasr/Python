#!python3
from mysql.connector.errors import ProgrammingError
from db import nova_conexao

tabela_contatos = """
    
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(45),
        telefone VARCHAR(40)
    );

"""

tabela_emails = """

    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    );

"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_emails)

    except ProgrammingError as e:
        print(f'Erro: {e.msg}')