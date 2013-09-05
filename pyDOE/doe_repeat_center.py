import numpy as np

def repeat_center(n, repeat):
    """
    Create the center-point portion of a design matrix
    
    Parameters
    ----------
    n : int
        The number of factors in the original design
    repeat : int
        The number of center points to repeat
    
    Returns
    -------
    mat : 2d-array
        The center-point portion of a design matrix (elements all zero).
    
    Example
    -------
    ::
    
        >>> repeat_center(3, 2)
        array([[ 0.,  0.,  0.],
               [ 0.,  0.,  0.]])
       
    """
    return np.zeros((repeat, n))