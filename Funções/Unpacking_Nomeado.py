#!python

def resultadoF1(**podium):
    for posicao, piloto in podium.items():
        print(f"{posicao} -> {piloto}")

resultadoF1(
    primeiro="L. Hamilton",
    segundo="M. Verstappen",
    terceiro="S. Vettel"
)