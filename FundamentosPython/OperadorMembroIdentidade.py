lista = {1, 2, 3, "Ana", "Carla"}

inLista = "Ana" in lista

print("Ana", ("nao está presente na lista", "esta presente na lista")[inLista])

x = 3
y = x

xyIguais = x is y
#xyDiferente = x is not y

print("y eh", ("diferente", "igual")[xyIguais], "a x")

listaA = {1, 2 ,3}
listaB = listaA
listaC = {1, 2, 3}

print("\n\n", listaA is listaB)
print("\n\n", listaC is listaA) 