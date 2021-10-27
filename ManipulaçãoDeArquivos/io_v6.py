#!python3

with open("Pessoa.csv") as arquivo:
    with open("Pessoa.txt", "w") as saida:
        for registro in arquivo:
            arquivo.write("Nome: {}, Idade: {}".format(*registro.strip().split(",")))

if arquivo.closed:
    print("Arquivo fechado")
