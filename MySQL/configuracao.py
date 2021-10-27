#!python3
from mysql.connector import connect
from getpass import getpass

print(f'{15 * "*"} MySQL {15 * "*"}', end='\n')
USER = input('USER: ')
PASSWORD = getpass("PASSWORD: ")

conexao = connect(
    host = 'localhost',
    port = 3306,
    user = USER,
    passwd = PASSWORD
)

print(f'\n\n{conexao}')

input("\n\nPrecisone enter para continuar...")
