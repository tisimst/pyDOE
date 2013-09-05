import numpy as np

def genfact(levels):
    """
    Create a general full-factorial design
    
    Parameters
    ----------
    levels : array-like
        An array of integers that indicate the number of levels of each input
        design factor.
    
    Returns
    -------
    mat : 2d-array
        The design matrix with coded levels 1 to k for a k-level factor
    
    Example
    -------
    ::
    
        >>> genfact([2, 4, 3])
        array([[ 1.,  1.,  1.],
               [ 2.,  1.,  1.],
               [ 1.,  2.,  1.],
               [ 2.,  2.,  1.],
               [ 1.,  3.,  1.],
               [ 2.,  3.,  1.],
               [ 1.,  4.,  1.],
               [ 2.,  4.,  1.],
               [ 1.,  1.,  2.],
               [ 2.,  1.,  2.],
               [ 1.,  2.,  2.],
               [ 2.,  2.,  2.],
               [ 1.,  3.,  2.],
               [ 2.,  3.,  2.],
               [ 1.,  4.,  2.],
               [ 2.,  4.,  2.],
               [ 1.,  1.,  3.],
               [ 2.,  1.,  3.],
               [ 1.,  2.,  3.],
               [ 2.,  2.,  3.],
               [ 1.,  3.,  3.],
               [ 2.,  3.,  3.],
               [ 1.,  4.,  3.],
               [ 2.,  4.,  3.]])

    """
    n = len(levels)  # number of factors
    nb_lines = np.prod(levels)  # number of trial conditions
    H = np.zeros((nb_lines, n))
    
    level_repeat = 1
    range_repeat = np.prod(levels)
    for i in xrange(n):
        range_repeat /= levels[i]
        lvl = []
        for j in xrange(levels[i]):
            lvl += [j+1]*level_repeat
        rng = lvl*range_repeat
        level_repeat *= levels[i]
        H[:, i] = rng
     
    return H
    
def ff2n(n):
    """
    Create a 2-Level full-factorial design
    
    Parameters
    ----------
    n : int
        The number of factors in the design.
    
    Returns
    -------
    mat : 2d-array
        The design matrix with coded levels -1 and 1
    
    Example
    -------
    ::
    
        >>> ff2n(3)
        array([[-1., -1., -1.],
               [ 1., -1., -1.],
               [-1.,  1., -1.],
               [ 1.,  1., -1.],
               [-1., -1.,  1.],
               [ 1., -1.,  1.],
               [-1.,  1.,  1.],
               [ 1.,  1.,  1.]])
    
    """
    H = genfact([2]*n)
    H[H==1] = -1
    H[H==2] = 1
    
    return H