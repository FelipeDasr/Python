#!python
def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))

for fib in fibonacci(20):
    print(fib)