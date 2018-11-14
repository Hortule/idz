from random import uniform


fi = open(r"lab1_pb_in_2.txt", "rt")
fo = open(r"lab1_pb_ou_2.txt", "wt")
fi.readline()
fi.readline()
nm = 0
for line in fi:
    if line == "\n":
        continue
    nm += 1
    (count, c) = line.split()
    count = int(count)
    c = float(c)
    fo.write("{0} набор значений\n".format(nm))
    mas = []
    for i in range(0, count):
        mas.append(uniform(-5.0, 5.0))
    fo.write("начальное состояние\n{0}".format(mas))

    count2 = 0
    for i in range(0, count):
        if mas[i] > c:
            count2 += 1
    fo.write("\nCount of elements bigger then C: {0}\n".format(count2))

    bn = -1
    for i in range(0, count):
        if abs(mas[i]) > bn:
            bn = abs(mas[i])
            pos = i
    fo.write("Numbers after biggest module: \n")
    for i in range(pos, count):
        fo.write("{0} ".format(mas[i]))
    fo.write('\n')

    for i in range(0, count-1):
        for j in range(i, count):
            if mas[i] > mas[j]:
                prom = mas[i]
                mas[i] = mas[j]
                mas[j] = prom
    fo.write("Конечное состояние\n{0}\n\n".format(mas))
fi.close()
fo.close()
