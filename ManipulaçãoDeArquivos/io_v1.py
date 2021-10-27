#!python

Arquivo = open("Pessoa.csv")
Dados = Arquivo.read()
Arquivo.close()

for registro in Dados.splitlines():
    print("Nome: {}, Idade: {}".format(*registro.split(",")))