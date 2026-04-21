import numpy as np

def root_bisection(fn, high=100, low=0, eps=1e-5, maxiter=50):
    errors = np.zeros(maxiter)
    i = 0
    mid = ( low + high ) /2
    errors[i] = abs(fn(mid))
    while  i < maxiter-1 :
        mid = ( low + high ) /2.0
        fmid = fn(mid)
        i = i + 1
        errors[i] = abs(fmid)
        flow = fn(low)
        if ( ( flow < 0 and fmid < 0 ) or ( flow > 0 and fmid > 0 ) ):
            low = mid
        else :
            high = mid
        if errors[i] < eps:
            break
    if i >= maxiter :
        print('Good SFound Solution after ', 0, ' iterations.')
    else :
        print('Found Solution after ', i, ' iterations.')
    return mid, errors