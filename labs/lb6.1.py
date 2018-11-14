from math import sqrt

fi = open(r"lab1_pb_in_1.txt", "rt")
fo = open(r"lab1_pb_ou_1.txt", "wt")
fi.readline()
fi.readline()

fo.write("+========+========+========+\n")
fo.write("I    B   I   Z1   I   Z2   I\n")
fo.write("+========+========+========+\n")

mas = {}

for line in fi:
    if line == "\n":
        continue
    b = float(line)
    mas[line] = []

    z1 = sqrt(2*b + 2 * sqrt(b**2 - 4))/(sqrt(b**2 - 4)+b+2)
    mas[line].append(z1)

    z2 = 1/sqrt(b+2)
    mas[line].append(z2)
    fo.write("I {0: .2f}  I{1: 6.2f}  I{2: 6.2f}  I\n".format(b, mas[line][0], mas[line][1]))
    fo.write("+--------+--------+--------+\n")
fi.close()
fo.close()
