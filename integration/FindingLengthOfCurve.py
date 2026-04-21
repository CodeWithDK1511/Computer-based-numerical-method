import numpy as np
from math import sqrt

np.set_printoptions(precision=2, suppress=True)

def curve_length(X, Y) :
    length = 0
    for i in range( len(X)-1):
        length += ( ( X[i+1] - X[i] )*sqrt( 1 + ( ( Y[i+1] - Y[i] )/ ( X[i+1] - X[i] )  )**2 ) )
    return length