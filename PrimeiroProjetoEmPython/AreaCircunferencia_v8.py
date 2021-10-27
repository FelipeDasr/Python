#!python
from math import pi
import sys #para pegar argumentos do argumento no terminal


def circulo(raio):  # criando uma função
    circunferencia = pi * raio ** 2
    return circunferencia


if __name__ == "__main__":
    raio = float(sys.argv[1])   #lista de argumentos no índice 1.
    circunferencia = circulo(raio)
    print(f"Circunferencia: {circunferencia}")
