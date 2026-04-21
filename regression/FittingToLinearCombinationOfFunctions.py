import numpy as np

def gauss_eliminate(eqns, debug=False):
    nrows = eqns.shape[0]
    ncols = eqns.shape[1]

    for r_piv in range(nrows - 1):
        pivot = np.ix_(abs(eqns[r_piv:, r_piv]) ==
                       abs(eqns[r_piv:, r_piv]).max())[0][0] + r_piv

        if eqns[pivot, r_piv] != 0:
            if pivot != r_piv:
                eqns[[r_piv, pivot]] = eqns[[pivot, r_piv]]

                if debug:
                    print('Pivot row: ', pivot)
                    print('Swapping Rows: ', r_piv, pivot)
                    print('Swapped Equations Array: ')
            for row in range(r_piv+1, nrows):
                k = eqns[r_piv, r_piv] / eqns[row, r_piv]
                eqns[row] = k*eqns[row] - eqns[r_piv]
                if debug:
                    print('Multiplicative Factor: ', k)
                    print('After reduction of row: ', row+1)
    print()

    return eqns


def back_substitute(eqns):
    nrows = eqns.shape[0]
    ncols = eqns.shape[1]
    sol = np.zeros((nrows, 1))

    for var_to_compute in range(nrows-1, -1, -1):
        eqn_num = var_to_compute
        if eqns[eqn_num, var_to_compute] == 0:
            print('Unique solution does not exist!')
            return False

        rhs = eqns[var_to_compute][ncols-1]  # Step 3: Insert code

        psum = 0.0
        for i in range(ncols-1):
            psum += eqns[var_to_compute][i] * sol[i]
        rhs = rhs - psum  
        sol[var_to_compute] = rhs / eqns[eqn_num, var_to_compute]

    return sol

def f0(x) :
    return 1

def f1(x) :
    return x

def f2(x) :
    return x**2

def f3(x) :
    return x**3

def create_comb_A(X, m) :
    A = np.zeros((X.shape[0], m))
    Y0 = np.array([[f0(x) for x in X]])
    Y1 = np.array([[f1(x) for x in X]])
    Y2 = np.array([[f2(x) for x in X]])
    Y3 = np.array([[f3(x) for x in X]])
    A = np.concatenate((Y0.T, Y1.T, Y2.T, Y3.T), axis=1)
    print("\nMatrix A :\n",A)
    return A


def solve_comb(X, Y, m) :                   # m is no. of functions
    A = create_comb_A(X, m)
    G = A.T.dot(A)
    H = A.T.dot(Y).reshape(A.shape[1], 1)      # To get a proper vector
    print("\nMatrix G : \n",G)
    print("\nMatrix H : \n",H)
    RA = gauss_eliminate(np.concatenate((G, H), axis=1))
    ans = back_substitute(RA)
    return ans