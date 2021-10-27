#!python 

try:
    arquivo = open("Pessoa.csv")

    for registro in arquivo:
        print("Nome: {}, Idade: {}".format(*registro.strip().split(",")))

finally:
    arquivo.close()
