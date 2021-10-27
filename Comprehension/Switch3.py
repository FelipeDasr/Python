def get_tipo_dia(dia):
    dia = {
        (1, 7): "Fim de semana",
        tuple(range(2, 7)): "Dia de semana",
    }
    dia_escolhido = (tipo for numeros, tipo in dia.items() if dia in numeros)
    return next(dia_escolhido, "Dia invalido!!!")

if __name__ == "__main__":
    for dia in range(0, 9):
        print(dia, get_tipo_dia(dia))