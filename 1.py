r = int(input("Ведите размерность массива: "))
masr = []
print("Введите элементы массива")
for i in range(r):
    masr.append(float(input()))
m = 0
ind = -1
for i in range(r):
    if masr[i] > m:
        m=masr[i]
        ind=i
for i in range(ind+1,r):
    masr[i] = 0
print(masr)