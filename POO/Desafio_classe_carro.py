#!python

class Carro:
    def __init__(self, velMax = 180):
        self.velMax = velMax
        self.velAtual = 0

    def acelerar(self, delta = 5):
        vel = self.velAtual + delta
        self.velAtual = vel if vel <= self.velMax else self.velMax
        return self.velAtual

    def frear(self, delta = 5):
        vel = self.velAtual - delta
        self.velAtual = vel if vel >= 0 else 0
        return self.velAtual

        
if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(40):
        print(c1.acelerar(13))

    for _ in range(10):
        print(c1.frear(17))