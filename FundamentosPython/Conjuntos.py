a = {1, 2, 3, 4, 5}
a = set("cod3r")
print(a)
print(4 in a, "Cod3r" in a)
print({1, 2, 3} == {3, 2, 1, 3})
c1 = {1, 2}
c2 = {2, 3}
numInter = c1.intersection(c2) #quais elementos c1 e c2 tem igual, mostrado pelo indice
c1.update(c2) #adicionar os elementos de c2 em c1 sem repetir valores iguais
saoIguais = c2 <= c1 # verificando se c2 é subconjunto de c1
print(c1)
c1 -= {2}
print(c1)