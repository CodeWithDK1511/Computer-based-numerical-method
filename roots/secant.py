import numpy as np

def root_secant(fn, init=0, step=1.0, eps=1e-5, maxiter=50) :
    x0 = init
    i = 0
    errors = np.zeros(maxiter+1)
    errors[i] = abs(fn(x0))
    while i < maxiter and errors[i] >= eps :
        val = fn(x0)
        dfn = (fn(x0) - fn( x0 - step ))/step
        x0 = x0 - val / dfn
        i = i + 1
        errors[i] = abs(val)
        
    if i >= maxiter :
        print('Good Solution not found in ', i, ' iterations!')
    else :
        print('Found Solution after ', i, ' iterations.')

    return x0, errors
