from math import sqrt

print('Введите {beg, Xend, и Dx')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
print('Xbeg={0: 7.2f} Xend={1: 7.2f}'.format(xb, xe))
print(' Dx={0: 7.2f}'.format(dx))
xt = xb
print('+--------+--------+')
print('I    X   I    Y   I')
print('+--------+--------+')
while xt <= xe:
    if xt <= -6:
        y = 1
    elif -6 < xt < -4:
        y = -0.5 * xt - 2
    elif -4 <= xt <= 0:
        y = sqrt(4 - (xt + 2) ** 2)
    elif 0 < xt < 2:
        y = -1 * sqrt(1 - (xt - 1) ** 2)
    else:
        y = -1 * xt + 2
    print('I{0: 7.2f} I{1: 7.2f} I'.format(xt, y))
    xt += dx
print('+--------+--------+')