import numpy as np

def create_A(X) :
    A = np.zeros((2,2))
    sum_x = 0 
    sum_x2 = 0
    n = len(X)
    for i in range ( n ):
        sum_x += X[i]
        sum_x2 += X[i]**2
    # Fill your code here as per the steps given above.
    A[0][0] = sum_x2
    A[0][1] = sum_x
    A[1][0] = sum_x
    A[1][1] = n
    
    return A

def create_B(X, Y) :
    B = np.zeros((2,1))
    sum_xy = 0
    sum_y = 0
    for i in range( len(Y)):
        sum_y += Y[i]
        sum_xy += X[i]*Y[i]  
    B[0][0] = sum_xy
    B[1][0] = sum_y  
    return B