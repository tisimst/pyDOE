import numpy as np

def union(H1, H2):
    """
    Join two matrices by stacking them on top of each other.
    
    Parameters
    ----------
    H1 : 2d-array
        The matrix that goes on top of the new matrix
    H2 : 2d-array
        The matrix that goes on bottom of the new matrix
    
    Returns
    -------
    mat : 2d-array
        The new matrix that contains the rows of ``H1`` on top of the rows of
        ``H2``.
    
    Example
    -------
    ::
    
        >>> union(np.eye(2), -np.eye(2))
        array([[ 1.,  0.],
               [ 0.,  1.],
               [-1.,  0.],
               [ 0., -1.]])
               
    """
    H = np.r_[H1, H2]
    return H