import math
import numpy as np
from scipy.linalg import toeplitz, hankel

__all__ = ['pbdesign']

def pbdesign(n, keep=None):
    """
    Generate a Plackett-Burman design
    
    Parameter
    ---------
    n : int
        The multiple of 4 higher than the number of factors.
    
    Optional
    --------
    keep : int
        The actual number of factors that the matrix will be used for 
        (default: n).
    
    Returns
    -------
    H : 2d-array
        An orthogonal design matrix with n rows, and (n-1) columns.
    
    Example
    -------
    Create a 5-factor design::
    
        >>> pbdesign(8)  # since 8 is the next heigher multiple of 4
        array([[ 1.,  1.,  1.,  1.,  1.,  1.,  1.],
               [-1.,  1., -1.,  1., -1.,  1., -1.],
               [ 1., -1., -1.,  1.,  1., -1., -1.],
               [-1., -1.,  1.,  1., -1., -1.,  1.],
               [ 1.,  1.,  1., -1., -1., -1., -1.],
               [-1.,  1., -1., -1.,  1., -1.,  1.],
               [ 1., -1., -1., -1., -1.,  1.,  1.],
               [-1., -1.,  1., -1.,  1.,  1., -1.]])

    And if we only want to keep the needed five columns::
    
        >>> pbdesign(8, keep=5)
        array([[ 1.,  1.,  1.,  1.,  1.],
               [-1.,  1., -1.,  1., -1.],
               [ 1., -1., -1.,  1.,  1.],
               [-1., -1.,  1.,  1., -1.],
               [ 1.,  1.,  1., -1., -1.],
               [-1.,  1., -1., -1.,  1.],
               [ 1., -1., -1., -1., -1.],
               [-1., -1.,  1., -1.,  1.]])
        
    
    """
    f, e = np.frexp([n, n/12., n/20.])
    k = [idx for idx, val in enumerate(np.logical_and(f==0.5, e>0)) if val]
    
    assert isinstance(n, int) and k!=[], 'Invalid inputs. n must be a multiple of 4.'
    
    k = k[0]
    e = e[k] - 1
    
    if k==0:  # N = 1*2**e
        H = np.ones((1, 1))
    elif k==1:  # N = 12*2**e
        H = np.vstack((np.ones((1, 12)), np.hstack((np.ones((11, 1)), 
            toeplitz([-1, -1, 1, -1, -1, -1, 1, 1, 1, -1, 1],
                     [-1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1])))))
    elif k==2:  # N = 20*2**e
        H = np.vstack((np.ones((1, 20)), np.hstack((np.ones((19, 1)),
            hankel(
            [-1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1],
            [1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1])
            ))))
    
    # Kronecker product construction
    for i in xrange(e):
        H = np.vstack((np.hstack((H, H)), np.hstack((H, -H))))
    
    if keep is not None:
        assert keep<=(H.shape[1]-1), 'Too many variables specified in "keep" for matrix'
        return H[:, 1:(keep + 1)]
    else:
        return H[:, 1:]
    
    