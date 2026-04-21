import numpy as np

np.set_printoptions(suppress=True, precision=2)


def lagrange_interpolation(X, Y, x):
    l = len(Y)
    lagrange = 0
    for i in range(l):
        mulx = 1
        mulxi = 1
        for j in range(l):
            if (j != i):
                mulx *= (x - X[j])
                mulxi *= (X[i] - X[j])

        lagrange += ((mulx / mulxi) * Y[i])
    return lagrange