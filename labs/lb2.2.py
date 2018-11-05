from math import sqrt

R = float(input('Введите R: '))
x = float(input('Введите x: '))
y = float(input('Введите y: '))


def okr1(x):
    return -1 * sqrt(R ** 2 - ((x + R) ** 2)) + R


def okr2(x):
    return -1 * sqrt(R ** 2 - (x ** 2))


if (-R <= x <= 0 <= y <= R and y <= okr1(x)) or (R >= x >= 0 >= y >= -R and y >= okr2(x)):
    print('Попадает')
else:
    print('Не попадает')
