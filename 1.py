r = int(input("Ведите размерность массива: "))
masr = []
print("Введите элементы массива")
for i in range(r):
    masr.append(float(input()))
m = max(masr)
for i in range(masr.index(m)+1,r):
    masr[i] = 0
print(masr)