from math import sqrt

b = float(input('Введите b\n'))
try:
    z1 = sqrt(2*b + 2 * sqrt(b**2 - 4))/(sqrt(b**2 - 4)+b+2)
except ValueError:
    print('Отрицательное подкоренное выражение')
except ZeroDivisionError:
    print('Попытка делить на ноль')
else:
    print('z1: ' + str(z1))

try:
    z2 = 1/sqrt(b+2)
except ValueError:
    print('Отрицательное подкоренное выражение')
except ZeroDivisionError:
    print('Попытка делить на ноль')
else:
    print('z2: ' + str(z2))
