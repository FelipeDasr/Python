#!python
from math import pi

if __name__ == "__main__": #Verificando se esta sendo executado no modulo principal
    raio = float(input("Informe o raio: "))
    circunferencia = pi * raio ** 2
    print(f"Circunferencia: {circunferencia}")