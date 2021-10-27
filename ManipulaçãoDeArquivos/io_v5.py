#!python 

with open("Pessoa.csv") as arquivo:
    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))

if arquivo.closed:
    print("Arquivo fechado")
