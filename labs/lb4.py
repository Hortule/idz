from random import uniform


count = int(input("input count of elements N (N <= 30): "))
c = float(input("input C: "))
mas = []
for i in range(0, count):
    mas.append(uniform(-5.0, 5.0))
print("начальное состояние\n{0}".format(mas))

count2 = 0
for i in range(0, count):
    if mas[i] > c:
        count2 += 1
print("Count of elements bigger then C: {0}".format(count2))

bn = -1
for i in range(0, count):
    if abs(mas[i]) > bn:
        bn = abs(mas[i])
        pos = i
print("Numbers after biggest module: ", end=' ')
for i in range(pos, count):
    print("{0} ".format(mas[i]), end=' ')
print()

for i in range(0, count-1):
    for j in range(i, count):
        if mas[i] > mas[j]:
            prom = mas[i]
            mas[i] = mas[j]
            mas[j] = prom
print("Конечное состояние\n{0}".format(mas))
