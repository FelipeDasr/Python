#!python
from math import pi
import sys  # para pegar argumentos do argumento no terminal
import os  # para limpar a tela do terminal

ERRO = '\033[91m'  #cor vermelha
NORMAL = '\033[0m' #cor default

def ajuda():
    print("\nEh necessario informar o raio do circulo")
    print("\nSintaxe: {} <raio>\n".format(sys.argv[0]))


def circulo(raio):  # criando uma função
    circunferencia = pi * raio ** 2
    return circunferencia

if __name__ == "__main__":
    os.system("cls") or None

    if len(sys.argv) < 2:
        ajuda()
        sys.exit(1)  # retornando com erro

    elif not sys.argv[1].isnumeric():
        ajuda()
        print(ERRO + "O raio deve ser um numero!!\n" + NORMAL)
        sys.exit(1)

    raio = float(sys.argv[1])  # lista de argumentos no índice 1.
    circunferencia = circulo(raio)
    print("Circunferencia: {:.2f}".format(circunferencia))
