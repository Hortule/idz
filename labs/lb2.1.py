from math import sqrt


x = float(input('Введите значение аргумента: '))
if x <= -6:
    y = 1
    print("X = {0:.2f}    Y = {1:.2f}".format(x, y))
elif -6 < x < -4:
    y = -0.5 * x - 2
    print("X = {0:.2f}    Y = {1:.2f}".format(x, y))
    
elif -4 <= x <= 0:
    y = sqrt(4 - (x + 2) ** 2)
    print("X = {0:.2f}    Y = {1:.2f}".format(x, y))
elif 0 < x < 2:
    y = -1 * sqrt(1 - (x-1) ** 2)
    print("X = {0:.2f}    Y = {1:.2f}".format(x, y))
elif x >= 2:
    y = -1 * x + 2
    print("X = {0:.2f}    Y = {1:.2f}".format(x, y))

