import numpy as np
np.set_printoptions(precision=2, suppress=True)  


def LU_decomposition(eqns ) :
    nrows = eqns.shape[0]
    ncols = eqns.shape[1]
    l = np.eye(eqns.shape[0])            # Step 2: Done for you
    
    for col in range( ncols-1 ):
        mrow = col
        for row in range( col+1 , nrows ):
            k = eqns[row][col] / eqns[mrow][col]
            l[row][col] = k
            for i in range ( ncols ):
                eqns[row][i]  = eqns[row][i] - k*eqns[mrow][i]
        # print("\n L : \n", l,"\n")
        # print("\n eq : \n",eqns,"\n")
    
    return ( l, eqns)

def fwd_substitute( l ) :
    nrows = l.shape[0]
    ncols = l.shape[1]
    Y = np.zeros((nrows,1))
    print("Y = ",Y)
    for i in range( nrows ):
        psum = 0
        for j in range( ncols -1 ):
            psum += Y[j]*l[i][j]
        Y[i] = l[i][ncols-1] -psum
    # print(Y)
    return Y
