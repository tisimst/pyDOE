import numpy as np
from doe_factorial import ff2n
from doe_repeat_center import repeat_center

def bbdesign(n, center=1):
    """
    Create a Box-Behnken design
    
    Parameters
    ----------
    n : int
        The number of factors in the design
    
    Optional
    --------
    center : int
        The number of center points to include (default = 1).
    
    Returns
    -------
    mat : 2d-array
        The design matrix
    
    Example
    -------
    ::
    
        >>> bbdesign(3)
        array([[-1., -1.,  0.],
               [ 1., -1.,  0.],
               [-1.,  1.,  0.],
               [ 1.,  1.,  0.],
               [-1.,  0., -1.],
               [ 1.,  0., -1.],
               [-1.,  0.,  1.],
               [ 1.,  0.,  1.],
               [ 0., -1., -1.],
               [ 0.,  1., -1.],
               [ 0., -1.,  1.],
               [ 0.,  1.,  1.],
               [ 0.,  0.,  0.]])
        
    """
    assert n>=3, 'Number of variables must be at least 3'
    
    # First, compute a factorial DOE with 2 parameters
    H_fact = ff2n(2)
    # Now we populate the real DOE with this DOE
    
    # We made a factorial design on each pair of dimensions
    # - So, we created a factorial design with two factors
    # - Make two loops
    Index = 0
    nb_lines = n*H_fact.shape[0]
    H = np.zeros((nb_lines, n))
    H = repeat_center(n, nb_lines)
    
    for i in xrange(n - 1):
        for j in xrange(i + 1, n):
            Index = Index + 1
            
            H[max([0, (Index - 1)*H_fact.shape[0]]):Index*H_fact.shape[0], 
                i] = H_fact[:, 0]
            H[max([0, (Index - 1)*H_fact.shape[0]]):Index*H_fact.shape[0], 
                j] = H_fact[:, 1]

    H = np.c_[H.T, repeat_center(n, center).T].T
    
    return H