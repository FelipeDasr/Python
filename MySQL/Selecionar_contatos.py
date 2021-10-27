from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'SELECT * FROM contatos'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    
    except ProgrammingError as erro:
        print(f'Erro: {erro}')

    else:
        print(f'\n ID  NOME{16*" "}  TELEFONE{12*" "}')
        for contato in contatos:
            print(f'{contato[2]:2d} | {contato[0]:20s} | {contato[1]}')