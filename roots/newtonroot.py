import numpy as np

def root_newton(fn, dfn, init, eps=1e-5, maxiter=50) :
    errors = np.zeros(maxiter)
    errors[0] = abs(fn(init))
    if errors[0] <= eps :
        print('Initial value is the solution!')
        return init, errors
    
    x0 = init
    i = 0
    while errors[i] >= eps and i < maxiter : 
        x0 = x0 - fn(x0) / dfn(x0)
        i = i + 1
        errors[i] = abs(fn(x0))
        
    if i >= maxiter :
        print('Good Solution not found in ', i, ' iterations!')
    else :
        print('Found Solution after ', i, ' iterations.')
        
    return x0, errors
