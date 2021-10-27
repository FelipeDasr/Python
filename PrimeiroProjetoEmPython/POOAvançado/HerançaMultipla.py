#!python

class Animal():
    @property
    def capacidades(self):
        return ("dormir", "comer", "beber")

class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ("amar", "falar", "estudar")

class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ("Fazer teia", "anadar pelas paredes")

class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ("bater em bandidos", "atirar teia entre prédios")

john = Homem()
print(f"John: {john.capacidades}")

aranha = Aranha()
print(f"Aranha: {aranha.capacidades}")

peter = HomemAranha()
print(f"Peter parker: {peter.capacidades}")