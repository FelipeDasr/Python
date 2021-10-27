#!python3
from mysql.connector import connect

BD = connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'felipe12'
)

cursor = BD.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print('-', database[0])