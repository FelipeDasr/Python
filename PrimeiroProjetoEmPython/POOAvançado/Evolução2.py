#python3

class Humano:
    #atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ("Habilits", "Erectus", "Neanderthalensis", "Sapiens")
        return ("Australopteco",) + tuple(f"Homo {adj}" for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

if __name__ == "__main__":
    jose = HomoSapiens("Jose")
    Humano.das_cavernas(jose)
    grokn = Humano("Grokn").das_cavernas()

    print(f"Evolucao (a partir da classe): {', '.join(HomoSapiens.especies())}")
    print(f"Evolucao (a partir da instancia): {', '.join(jose.especies())}")
    print(f"Homo Sapiens evoluido?: {HomoSapiens.is_evoluido()}")
    print(f"Jose eh evoluido?: {jose.is_evoluido()}")