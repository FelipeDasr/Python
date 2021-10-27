#!python
from math import pi


def circulo(raio):  # criando uma função
    circunferencia = pi * raio ** 2
    return circunferencia


if __name__ == "__main__":
    raio = float(input("Informe o raio: "))
    circunferencia = circulo(raio)
    print(f"Circunferencia: {circunferencia}")
