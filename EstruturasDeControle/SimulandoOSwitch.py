#!python
def getDiaSemana(dia):
    dias = {
        1: "Domingo",
        2: "Segunda",
        3: "Terca",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sabado"
    }
    return dias.get(dia, "Dia Invalido")

def getTipoDia(dia):
    if dia == 1 or dia == 7:
        return "Fim de semana"
    elif dia in range(2, 7):
        return "Dia util"
    else:
        return "Dia Invalido"

if __name__ == "__main__":
    for dia in range(1, 8):
        print("{} eh {}".format(getDiaSemana(dia), getTipoDia(dia)))


        