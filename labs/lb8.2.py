import turtle as tr
from random import uniform
from math import sqrt


def fun8(x, y):
    R = 6
    if (x < -6) or (x > 6):
        flag = 0
    if (y ** 2 >= 2 * R * y - (x + R) ** 2 and -6 <= x <= 0 and 0 <= y <= 6) or (y ** 2 <= R ** 2 - x ** 2 and 0 <= x <= 6 and
                                                                                 -6 <= y <= 0):
        flag = 1
    else:
        flag = 0
    return flag


aX = [-8, 8]
aY = [-8, 8]
Dx = 300
Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
tr.setup(Dx, Dy, 200, 200)
tr.reset()
Nmax = 10000
tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])
tr.title("lab8.2")
tr.width(2)
tr.ht()
tr.tracer(0, 0)
tr.up()
mfun = 0
for n in range(Nmax):
    x = uniform(aX[0], aX[1])
    y = uniform(aY[0], aY[1])
    tr.goto(x, y)
    if fun8(x, y) != 0:
        tr.dot(3, "green")
        mfun += 1
    else:
        tr.dot(3, "#ffccff")
tr.color("blue", "blue")
tr.up()
tr.goto(aX[0], 0)
tr.down()
tr.goto(aX[1], 0)
tr.up()
tr.goto(0, aY[1])
tr.down()
tr.goto(0, aY[0])
tr.up()
for x in range(aX[0], aX[1]):
    tr.goto(x, 0.1)
    tr.down()
    tr.goto(x, 0)
    tr.up()
    tr.sety(-0.4)
    coords = str(x)
    tr.write(coords)

for y in range(aY[0], aY[1]):
    tr.goto(0, y)
    tr.down()
    tr.goto(0.1, y)
    tr.up()
    tr.setx(0.2)
    coords = str(y)
    tr.write(coords)

poli = [0, 0.1, 0, -0.1, 0]
Arrbeg = int(aX[1])
Xpoli = [Arrbeg, Arrbeg - 0.1, Arrbeg + 0.3, Arrbeg - 0.1, Arrbeg]
tr.goto(Xpoli[0], poli[0])
tr.begin_fill()
tr.down()
for i in range(1, 5):
    tr.goto(Xpoli[i], poli[i])
tr.end_fill()  # заливаем стрелку
# Надпишем ось Х
tr.up()
tr.goto(Arrbeg, -0.7)
tr.write("Х", font=("Arial", 14, "bold"))
#
# на ОСИ	у
Arrbeg = int(aY[1])
Ypoli = [Arrbeg, Arrbeg - 0.1, Arrbeg + 0.3, Arrbeg - 0.1, Arrbeg]
tr.up()
tr.goto(poli[0], Ypoli[0])
tr.begin_fill()
tr.down()
for i in range(1, 5):
    tr.goto(poli[i], Ypoli[i])
tr.end_fill()
# Надпишем ось У
tr.up()
tr.goto(0.2, Arrbeg)
tr.write("Y", font=("Arial", 14, "bold"))
Sf = (aX[1] - aX[0]) * (aY[1] - aY[0]) * mfun / Nmax
tr.goto(1, 9)
meseg = "N = {0:8d}\nNf = {1:8d}\nSf = {2:8.2f}".format(Nmax, mfun, Sf)
tr.write(meseg, font=("Arial", 12, "bold"))
print(meseg)
#
# Комментировать при работе в IDLE
tr.done()
