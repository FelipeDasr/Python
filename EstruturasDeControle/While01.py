#!python
from random import randint

NumeroInformado = -1
NumeroSecreto = randint(0, 9)

while NumeroInformado != NumeroSecreto:
    NumeroInformado = int(input("Informe um numero inteiro: "))

print("Numero secreto {} foi encontrado!".format(NumeroSecreto))