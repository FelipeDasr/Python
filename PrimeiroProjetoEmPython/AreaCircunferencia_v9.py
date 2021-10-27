#!python
from math import pi
import sys #para pegar argumentos do argumento no terminal
import os  #para limbar a tela do terminal


def circulo(raio):  # criando uma função
    circunferencia = pi * raio ** 2
    return circunferencia


if __name__ == "__main__":
    os.system("cls") or None

    if len(sys.argv) < 2:
        print("\nEh necessario informar o raio do circulo")
        print("\nSintaxe: {} <raio>\n".format(sys.argv[0]))
    
    else:
        raio = float(sys.argv[1])   #lista de argumentos no índice 1.
        circunferencia = circulo(raio)
        print("Circunferencia: {:.2f}".format(circunferencia))
