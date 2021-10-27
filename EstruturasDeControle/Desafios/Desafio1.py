#!python
from random import randint


def sortearNum():
    return randint(1, 6)


for x in range(1, 6):
    if sortearNum() % 2 == 1:
        continue
    elif sortearNum() == x:
        print("ACERTOU", x)
        break
else:
    print("ERROU")
