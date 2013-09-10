import numpy as np

def lhs(n, x_min, x_max, samples=None, randomize=False):
    """
    Generate a latin-hypercube design
    
    Parameters
    ----------
    n : int
        The number of factors to generate samples for
    xmin : array
        The lower bounds to scale the samples to, one for each factor.
    xmax : array
        The upper bounds to scale the samples to, one for each factor.
    
    Optional
    --------
    samples : int
        The number of samples to generate for each factor (Default: n)
    randomize : bool
        If True, the samples will be slightly perturbed, such that the final
        set of samples are no longer equally spaced, but still evenly sampled.
        If False, the samples will be equally spaced as well.
    
    """
    
    assert x_min<x_max, 'x_min < x_max are required parameters'
    
    if samples is None:
        samples = n
    
    #if mixiter is None:
        #mixiter = 3*samples
    
    sequence = range(samples)
    #Aux = sequence
    #for i in xrange(int(np.ceil(samples/n))):
        #Aux += sequence
    
    #sequence = Aux[:samples]
    lhs_matrix = np.zeros((samples, n))
    for i in xrange(n):
        lhs_matrix[:, i] = sequence
    
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
                lhs_matrix[i, j] = lhs_matrix[i, j] + offset - 1
        
    for i in xrange(lhs_matrix.shape[1]):
        Min = np.min(lhs_matrix[:, i])
        Max = np.max(lhs_matrix[:, i])
        for j in xrange(lhs_matrix.shape[0]):
            lhs_matrix[j, i] = (lhs_matrix[j, i] - Min)/(Max - Min)
            lhs_matrix[j, i] = (x_max[i] - x_min[i])*lhs_matrix[j, i] + x_min[i]
    
    return lhs_matrix
