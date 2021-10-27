#!python

class Data:
    def __init__(self, dia = 1, mes = 1, ano = 1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

if __name__ == "__main__":
    
    d1 = Data(ano = 2020)
    print(d1)