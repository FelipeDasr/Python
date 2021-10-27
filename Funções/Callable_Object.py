#!python

class Potencia:
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente

quadrado = Potencia(2)

if callable(quadrado):
    print(f"2**2 => {quadrado(2)}")