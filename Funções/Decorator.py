def log(function):
    def decorator(*args, **kwargs):
        print(f"Inicio da chamada da funcao: {function.__name__}")
        print(f"Args: {args}")
        print(f"kwargs: {kwargs}")
        resultado = function(*args, **kwargs)
        print(f"Resultado da chamada: {resultado}")
        return resultado
    return decorator

@log
def soma(x, y):
    return x + y

@log
def sub(x, y):
    return x - y

print(sub(3, 6))
print(soma(3, 9))