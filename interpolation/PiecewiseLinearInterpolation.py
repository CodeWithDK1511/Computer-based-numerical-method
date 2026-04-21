import numpy as np

np.set_printoptions(suppress=True, precision=2)

def linear_interpolation(X, Y, x_u) :
	for i in range( len(X)-1 ):
		if ( X[ i ] <= x_u <= X[i+1] ):
			a = (Y[i+1] - Y[i])/( X[i+1] - X[i] )	
			return a, Y[i]
	print(x_u ," is not between in given X and Y")
