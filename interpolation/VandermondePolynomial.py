import numpy as np

def makeA ( X ):
	l = len(X)
	A = []
	for i in range ( l ):
		A += [ [1] ]
		for j in range ( 1, l ):
			A[i] += [ X[i]**j ]
	return A 
	
def makeEqn (A,y) :
	for i in range ( len(A) ):
		A[i] += [ y[i] ]
	return A

def gaussElimination ( eqn ):
	row = len(eqn )
	for i in range ( row  ):
		if ( eqn[i][i] == 0 ):
			for j in range ( i+1 , row ):
				if ( eqn[j][i] != 0 ):
					temp = eqn[i]
					eqn[i] = eqn[j]
					eqn[ j ] = temp
					break
			if ( j == row ):
				print("Gauss Not posible")
				break
		for j in range ( i+1 , row ):
			f = eqn[j][i] / eqn[i][i]
			for k in range ( i , row+1 ):
				eqn[j][k] = eqn[j][k] - f * eqn[i][k]
	return eqn

def backSubstitution ( eqn ) :
	row = len (eqn )
	C = np.zeros(row)
	for i in range ( row-1 , -1 ,-1):
		sum = 0
		for j in range ( i+1 , row ):
			sum += eqn[i][j]*C[j]
		C[i] =  ( eqn[i][row ] - sum) / eqn[i][i]  
	return C
