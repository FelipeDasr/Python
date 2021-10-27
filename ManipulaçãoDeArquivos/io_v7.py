#!python3

import csv

with open("Pessoa.csv") as arquivo:
    with open("Pessoas.txt", "w") as arquivoSaida:
        for registro in csv.reader(arquivo):
            arquivoSaida.write('Nome: {} Idade {}'.format(*registro))