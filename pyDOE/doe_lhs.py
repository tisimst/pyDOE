import numpy as np

def lhs(n, samples=None, randomize=False):
    """
    Generate a latin-hypercube design
    
    Parameters
    ----------
    n : int
        The number of factors to generate samples for
    
    Optional
    --------
    samples : int
        The number of samples to generate for each factor (Default: n)
    randomize : bool
        If True, the samples will be slightly perturbed within the respective
        intervals, such that the final set of samples are no longer equally spaced, but still uniformly sampled.
        If False, the samples will be equally spaced as well.
    
    Returns
    -------
    H : 2d-array
        An n-by-samples design matrix that has been normalized so factor values
        are uniformly spaced between zero and one.
    
    Example
    -------
    A 3-factor design (defaults to 3 samples)::
    
        >>> lhs(3)
        array([[ 0.16666667,  0.5       ,  0.83333333],
               [ 0.5       ,  0.83333333,  0.16666667],
               [ 0.83333333,  0.16666667,  0.5       ]])
    
    A 4-factor design with 6 samples::
    
        >>> lhs(4, samples=6)
        array([[ 0.08333333,  0.25      ,  0.75      ,  0.08333333],
               [ 0.25      ,  0.75      ,  0.08333333,  0.25      ],
               [ 0.91666667,  0.58333333,  0.25      ,  0.75      ],
               [ 0.58333333,  0.41666667,  0.91666667,  0.58333333],
               [ 0.75      ,  0.91666667,  0.41666667,  0.41666667],
               [ 0.41666667,  0.08333333,  0.58333333,  0.91666667]])
    
    A 2-factor design with 5 randomly perturbed samples::
    
        >>> lhs(2, samples=5, randomize=True)
        array([[ 0.82876253,  0.19000096],
               [ 0.39620898,  0.63175758],
               [ 0.01212062,  0.51822857],
               [ 0.69460061,  0.37600065],
               [ 0.47163116,  0.84052841]])
    
    """
    if samples is None:
        samples = n
    
    # generate the intervals
    sequence = np.arange(samples + 1)
    
    lhs_matrix = np.zeros((samples, n))
    for i in xrange(n):
        lhs_matrix[:, i] = sequence[:-1] + 0.5
    
    for i in xrange(samples):
        for j in xrange(n):
            Index1 = np.ceil(np.random.rand()*samples) - 1
            Index2 = np.ceil(np.random.rand()*samples) - 1
            Aux = lhs_matrix[Index1, j]
            lhs_matrix[Index1, j] = lhs_matrix[Index2, j]
            lhs_matrix[Index2, j] = Aux
    
    if randomize:
        for i in xrange(samples):
            for j in xrange(n):
                offset = np.random.rand() - 0.5
                lhs_matrix[i, j] = lhs_matrix[i, j] + offset
        
    return lhs_matrix/samples
