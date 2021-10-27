#!python

def cores_arco_iris():
    yield 'vermelho'
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'índigo'
    yield 'violeta'

if __name__ == "__main__":
    generator = cores_arco_iris()

    try:
        while True:
            print(next(generator))
    
    except:
        pass


