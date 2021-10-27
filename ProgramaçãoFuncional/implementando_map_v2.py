#!python

def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)

if __name__ == '__main__':
    lista = [2, 5, 3, 8, 4]
    print(list(mapear(lambda x: x ** 3, lista)))