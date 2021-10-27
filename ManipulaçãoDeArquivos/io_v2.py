#!python

arquivo = open('Pessoa.csv')

for registro in arquivo:
    print("Nome: {}, Idade: {}".format(*registro.split(',')))
arquivo.close()