import numpy as np


def MakeMatr(n, m, a, b):
    Matr = (b-a)*np.random.random(size=(n, m)) + a
    return Matr


def PrintMatr(Matr):
    (nRow, nCol) = Matr.shape
    for Row in range(nRow):
        for Col in range(nCol):
            fo.write("{0: 7.3f}".format(Matr[Row][Col]))
        fo.write('\n')
    fo.write('\n')


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
    fo.write('\n')
    for i in range(nRow):
        for Col in range(nCol):
            fo.write("{0: 7.3f}".format(Matr[nom[i]][Col]))
        fo.write('\n')


fi = open(r"lab1_pb_in_3.txt", "rt")
fo = open(r"lab1_pb_ou_3.txt", "wt")
fi.readline()
fi.readline()
num = 0
for line in fi:
    if line == "\n":
        continue
    num += 1
    fo.write("{0} набор значений\n".format(num))
    (n, m) = line.split()
    n = int(n)
    m = int(m)
    MyMatr = MakeMatr(n, m, -10, 10)
    PrintMatr(MyMatr)

    col = ZeroCol(MyMatr)
    if col > -1:
        fo.write("First col with zero element {0}\n".format(col+1))
    else:
        fo.write("No one zero element in matrix\n")

    nom = SortMatr(MyMatr)
    CorOut(MyMatr, nom)
fi.close()
fo.close()
