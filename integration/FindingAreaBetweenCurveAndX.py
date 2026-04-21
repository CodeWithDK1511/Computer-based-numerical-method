import numpy as np

np.set_printoptions(precision=2, suppress=True)

def area_trapezoid(X, Y) :
    area = 0.0
    for i in range(len(X)-1):
        h = X[i+1] - X[i]
        area += h * (Y[i+1] + Y[i])
    area /= 2
    return area

def area_simpson(X, Y) :
    h = X[1] - X[0]
    area = Y[0] + Y[-1]
    for i in range ( 1, len(X) -1 ):
        if i % 2 == 0:
            area += 2*Y[i]
        else :
            area += 4*Y[i]
    area *= h / 3
    return area


