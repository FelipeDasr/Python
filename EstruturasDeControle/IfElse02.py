#!python
def faixaEtaria(idade):
    if 0 <= idade < 18:
        return "Menor de idade!!"
    elif idade in range(18, 64):
        return "Adulto"
    elif idade in range(65, 100):
        return "Idoso"
    elif idade >= 100:
        return "Centanario"
    else:
        return "Idade invalida"

if __name__ == "__main__":
    idades = (17, 35, 87, 113, -2)
    for idade in idades:
        print(f"{idade}: {faixaEtaria(idade)}")