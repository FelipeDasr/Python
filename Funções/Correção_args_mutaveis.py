#!python

#problema

def fibonacci(sequencia=None):
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

inicio = fibonacci()
print(inicio, id(inicio))
print(fibonacci(inicio))
restart = fibonacci()
print(restart)