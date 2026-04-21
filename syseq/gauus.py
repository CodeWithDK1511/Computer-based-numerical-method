import numpy as np
np.set_printoptions(precision=2, suppress=True)


def gauss_eliminate(eqns, debug=False):
    nrows = len(eqns)


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
