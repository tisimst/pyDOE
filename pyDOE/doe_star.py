import numpy as np

def star(n):
    """
    Create the star points of various design matrices
    
    Parameters
    ----------
    n : int
        The number of variables in the design
    
    Returns
    -------
    mat : 2d-array
        The unit-star-point portion of the design matrix (i.e. at +/- 1)
    
    Example
    -------
    ::
    
        >>> star(3)
        array([[-1.,  0.,  0.],
               [ 1.,  0.,  0.],
               [ 0., -1.,  0.],
               [ 0.,  1.,  0.],
               [ 0.,  0., -1.],
               [ 0.,  0.,  1.]])
               
    """
    H = np.zeros((2*nb_var, nb_var))
    for i in xrange(nb_var):
        H[2*i:2*i+2, i] = [-1, 1]
    return H