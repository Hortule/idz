from math import sqrt
import turtle as tr

def Fun1(x):
    if x <= -6:
        y = 1
    elif -6 < x < -4:
        y = -0.5 * x - 2
    elif -4 <= x <= 0:
        y = sqrt(4 - (x + 2) ** 2)
    elif 0 < x < 2:
        y = -1 * sqrt(1 - (x - 1) ** 2)
    else:
        y = -1 * x + 2
    return y


def Axis(txy, ax='X'):
        a = txy[0]
        b = txy[1]
        tr.up()
        if ax == 'X':
            pb = [a, 0]
            pe = [b, 0]
        else:
            pb = [0, a]
            pe = [0, b]
        tr.goto(pb)
        tr.down()
        tr.goto(pe)


def Mark(txy, ax='X'):
    a = txy[0]
    b = txy[1]
    tr.up()
    for t in range(a, b):
        if ax == 'X':
            pb = [t, 0]
            pe = [t, 0.2]
            pw = [t, -0.5]
        else:
            pb = [0, t]
            pe = [0.2, t]
            pw = [0.2, t]
        tr.goto(pb)
        tr.down()
        tr.goto(pe)
        tr.up()
        tr.goto(pw)
        tr.write(str(t))


def Arrow(txy, ax='X'):
    a = [0.1, 0, -0.1]
    b = [-0.1, 0.3, -0.1]
    tr.up()
    tr.goto(0, 0)
    tr.begin_poly()
    for i in range(2):
        tr.goto(a[i], b[i])
    tr.end_poly()
    p = tr.get_poly()
    tr.register_shape("myArrow", p)
    tr.resizemode("myArrow")
    tr.shapesize(1, 2, 1)
    if ax == 'X':
        tr.tiltangle(0)
        tr.goto(txy[1] + 0.2, 0)
        pw = [int(txy[1]), -1.0]
    else:
        tr.tiltangle(90)
        tr.goto(0, txy[1] + 0.2)
        pw = [0.2, int(txy[1])]
    tr.stamp()
    tr.goto(pw)
    tr.write(ax, font=("Arial", 14, "bold"))


def main():
    aX = [-12, 12]
    aY = [-3, 5]
    Dx = 800
    Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
    tr.setup(Dx, Dy)
    tr.reset()
    Nmax = 1000
    tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])
    tr.title("Lab8")
    tr.width(2)
    tr.color("blue", "blue")
    tr.ht()
    tr.tracer(0, 0)
    Axis(aX, 'X')
    Mark(aX, 'X')
    Arrow(aX, 'X')
    Axis(aY, 'Y')
    Mark(aY, 'Y')
    Arrow(aY, 'Y')
    tr.color("green")
    tr.width(3)
    dx = (aX[1] - aX[0])/Nmax
    x = aX[0]
    y = Fun1(x)
    if (y is None):
        tr.up()
        tr.goto(x, 0)
    else:
        tr.goto(x, y)
        tr.down()
    while x <= aX[1]:
        x = x + dx
        y = Fun1(x)
        if (y is None):
            tr.up()
            continue
        else:
            tr.goto(x, y)
            tr.down()


if __name__ == "__main__":
    main()

tr.mainloop()













