#!python

from functools import reduce

pessoas  = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Ana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

soma_idade = reduce(lambda idade, p: idade + p['idade'], pessoas, 0)
print(soma_idade)
