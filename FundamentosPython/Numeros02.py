from decimal import Decimal, getcontext

getcontext().prec = 4
numDec = Decimal(1) / Decimal(7)


print("\n{}".format(numDec))
maiorDec = Decimal.max(Decimal(1), Decimal(4))

print("\n{}".format(maiorDec))

getcontext().prec = 4
numDec2 = Decimal(4) + Decimal(4)

print("\n{}".format(numDec2))
maiorDec2 = Decimal.max(numDec, numDec2)

print("\n{}".format(maiorDec2))