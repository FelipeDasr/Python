frase = "Python eh uma boa linguagem"

estaPresente = "boa" in frase

print("'boa'{} presente na frase".format((" esta" if estaPresente else " nao esta")))

print("tamanho da frase: {}".format(len(frase)))

frase = frase.lower() #transformado a string em minúsculo

print(frase)

frase = frase.upper() #transformando a string em maisculo

print(frase)

lista = frase.split("A") #quebrando a frase e armazenadno em uma lista

print("\n\n{}".format(lista))