#!python
produto = {"Nome": "Placa de video", "preco": 14.99, "importada": True, "estoque": 789}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print("{} = {}".format(chave, valor))