class ClasseSimples:
    cont = 0

    def __init__(self):
        self.contar()

        #ou
        #self.__class__.cont += 1

    @classmethod
    def contar(cls):
        cls.cont += 1

if __name__ == "__main__":
    lista = [ClasseSimples(), ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.cont)