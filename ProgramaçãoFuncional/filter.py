#!python

pessoas  = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Ana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
menores = list(map(lambda n: n['nome'], menores))
print(menores)

maiores = filter(lambda p: p['idade'] >= 18, pessoas)
maiores = list(map(lambda n: n['nome'], maiores))
print(maiores)

#desafio: filtrar nomes com >=6 caracteres

maiores_6 = filter(lambda n: len(n['nome']) >= 6, pessoas)
maiores_6 = list(map(lambda p: p['nome'], maiores_6))
print(maiores_6)