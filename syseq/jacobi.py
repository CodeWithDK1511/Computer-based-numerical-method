import numpy as np

def jacobi ( A,B , eps=1e-3):
    nrows = A.shape[0]
    sol = np.zeros((nrows,1))
    change = 1.0
    while ( change > eps ):
        psol = sol.copy()
        for i in range( nrows ):
            psum = 0
            for j in range ( nrows ):
                if ( i != j ):
                    psum += sol[j]* A[i][j]
            sol[i] = (B[0][i] - psum )/A[i][i]
        change = abs(sol - psol).max()
    return sol

