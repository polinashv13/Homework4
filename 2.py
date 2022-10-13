import random
c = int(input("Введите размерность массива с "))
d = int(input("Введите размерность массива d "))
masc = []
masd = []
for i in range(c):
    masc.append(random.randint(0,10))
for r in range(d):
    masd.append(random.randint(0,15))
for s in set(masc):
    if s in masd:
        print(s)