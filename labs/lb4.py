from random import uniform


count = int(input("input count of elements N (N <= 30): "))
mas = []
for i in range(0, count):
    mas.append(uniform(-5.0, 5.0))
print("начальное состояние\n{0}".format(mas))


