import random
g = int(input("Введите размерность массива: "))
masg = []
for i in range(g):
    masg.append(random.randint(0,7))
mn = 8
for i in range(g):
    if masg[i] < mn:
        mn=masg[i]
Delta = int(input("Введите Delta: "))
c = 0
for i in masg:
    if i-Delta==mn:
        c=c+1
print(c)