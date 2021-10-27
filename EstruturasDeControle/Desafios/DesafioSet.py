#!python
PalavrasProibidas = {"futebol", "religiao", "politica"}
textos = [
    "Joao gosta de futebol e politica",
    "A praia foi divertida"
]

for texto in textos:
    intercecao = PalavrasProibidas.intersection(set(texto.lower().split()))
    if intercecao:
        print("Texto possui palavras proibidas:", intercecao)
    else:
        print("Texto autorizado:", texto)
