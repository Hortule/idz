import numpy as np


def MakeMatr(n, m, a, b):
    Matr = (b-a)*np.random.random(size=(n, m)) + a
    return Matr


def PrintMatr(Matr):
    (nRow, nCol) = Matr.shape
    for Row in range(nRow):
        for Col in range(nCol):
            print("{0: 7.3f}".format(Matr[Row][Col]), end="")
        print()
    print()


def ZeroCol(Matr):
    (nRow, nCol) = Matr.shape
    for Col in range(nCol):
        for Row in range(nRow):
            if Matr[Row][Col] == 0:
                return Col
    return -1


def SortMatr(Matr):
    (nRow, nCol) = Matr.shape
    har = []
    nom = []
    for Row in range(nRow):
        har.append(0)
        nom.append(Row)
        for Col in range(1, nCol):
            if Matr[Row][Col] < 0:
                har[Row] += Matr[Row][Col]
    for i in range(0, nRow-1):
        for j in range(i, nRow):
            if har[i] < har[j]:
                promh = har[i]
                promn = nom[i]
                nom[i] = nom[j]
                har[i] = har[j]
                nom[j] = promn
                har[j] = promh
    return nom


def CorOut(Matr, nom):
    (nRow, nCol) = Matr.shape
    print()
    for i in range(nRow):
        for Col in range(nCol):
            print("{0: 7.3f}".format(Matr[nom[i]][Col]), end="")
        print()


n = int(input('input matrix size N: '))
m = int(input('input matrix size M: '))
MyMatr = MakeMatr(n, m, -10, 10)
PrintMatr(MyMatr)

col = ZeroCol(MyMatr)
if col > -1:
    print("First col with zero element {0}".format(col+1))
else:
    print("No one zero element in matrix")

nom = SortMatr(MyMatr)
CorOut(MyMatr, nom)
