#!python
palavra = "paralelepipedo"
for letra in palavra:
    print(letra, end=",")
print("FIM\n\n")

aprovados = ["Rafaela", "Pedro", "Renato", "Maria"]
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(posicao, nome)

dias_semana = ("Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado")
for dia in dias_semana:
    print("Dia", dia)