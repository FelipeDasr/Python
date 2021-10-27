#!python
for x in range(1, 11):
    if x % 2 == 1:
        continue
    print(x)

for x in range(1, 11):
    if x == 5:
        break
    print(x)

print("Fim")