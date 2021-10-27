#!python

def mapear(funcao, lista):
    for elemento in lista:
        yield funcao(elemento)

if __name__ == "__main__":
    lista = [2, 6, 3, 8, 5] 
    print(list(mapear(lambda x: x ** 2, lista)))