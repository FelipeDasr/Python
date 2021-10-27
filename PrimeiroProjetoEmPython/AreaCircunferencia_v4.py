#!python
from math import pi

raio = float(input("Informe o raio: "))
circunferencia = pi * raio ** 2
print(f"Circunferencia: {circunferencia}")

print("Nome do modulo:", __name__)
print("Nomedo pacote:", __package__)