#!python 

def executar(funcao):
    if callable(funcao):
        funcao()

def bomDia():
    print("Bom dia")

def boaTarde():
    print("Boa tarde")

executar(bomDia)
executar(boaTarde)

