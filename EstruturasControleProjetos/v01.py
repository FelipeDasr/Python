#!python
def fibonacci():
    penultimo = 0
    ultimo = 1
    print("{}, {}".format(penultimo, ultimo))
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=", ")
        penultimo = ultimo
        ultimo = proximo

if __name__ == "__main__":
    fibonacci()