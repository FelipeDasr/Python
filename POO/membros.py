#!python

class Data:
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


if __name__ == "__main__":
    d1 = Data()
    d1.dia = 9
    d1.mes = 6
    d1.ano = 2020

    print(d1)

