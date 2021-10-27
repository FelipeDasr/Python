lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'joao', 'idade': 21},
    {'nome': 'maria', 'idade': 23},
    {'nome': 'carlos', 'idade': 34},
]

so_nomes = list(map(lambda nome: nome['nome'], lista_2))
print(so_nomes)

so_idades = list(map(lambda idade: idade['idade'], lista_2))
print(so_idades)

#desafio: usando map retorne frases <nome> tem <idade>

frases = list(
    map(lambda frase: f"{frase['nome']} tem {frase['idade']} anos", lista_2)
)

print(frases)
