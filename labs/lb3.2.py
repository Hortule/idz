from math import *
from random import *

def okr1(x):
    return -1 * sqrt(R ** 2 - ((x + R) ** 2)) + R


def okr2(x):
    return -1 * sqrt(R ** 2 - (x ** 2))


R = 3
flag = 0
print('    X       Y   Res')
print('-------------------')
for n in range(10):
    x = uniform(-3, 3)
    y = uniform(-3, 3)
    if (-R <= x <= 0 <= y <= R and y <= okr1(x)) or (R >= x >= 0 >= y >= -R and y >= okr2(x)):
        flag = 1
    else:
        flag = 0
    print('{0: 7.2f} {1: 7.2F}'.format(x, y), end=' ')
    if flag:
        print('Yes')
    else:
        print('No')
