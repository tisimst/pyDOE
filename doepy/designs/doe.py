"""
================================================================================
pyDOE: The experimental design package for python
================================================================================

Author: Abraham Lee
Copyright: 2013

"""

import numpy as np

__all__ = []  # add the functions as they are defined

################################################################################

def fullfact(levels):
    """
    Generate a full-factorial design of arbitrary numbers of levels.
    
    Parameters
    ----------
    levels : array-like
        An integer array that describes the number of desired factor levels for
        each factor.
    
    Returns
    -------
    design : 2d-array
        A 2-D array containing the coded levels of every possible combination 
        of factor levels, each column corresponding to a separate factor.
    
    Example
    -------
    Let's construct a design with three factors: a 2-level factor, a 4-level 
    factor, and a 3-level factor. This results in a design of 24 trial 
    conditions with three columns (2 levels in the first column, 4 levels in 
    the second column, and 3 levels in the third column)::
    
        >>> design = fullfact([2, 4, 3])
        >>> design
        array([[0, 0, 0],
               [1, 0, 0],
               [0, 1, 0],
               [1, 1, 0],
               [0, 2, 0],
               [1, 2, 0],
               [0, 3, 0],
               [1, 3, 0],
               [0, 0, 1],
               [1, 0, 1],
               [0, 1, 1],
               [1, 1, 1],
               [0, 2, 1],
               [1, 2, 1],
               [0, 3, 1],
               [1, 3, 1],
               [0, 0, 2],
               [1, 0, 2],
               [0, 1, 2],
               [1, 1, 2],
               [0, 2, 2],
               [1, 2, 2],
               [0, 3, 2],
               [1, 3, 2]])

   """
    try:
        len(levels)
    except TypeError:
        raise TypeError('Vector required as input')
        
    lvls = np.array(levels, dtype=np.float64)
    if len(lvls.shape)==1:
        n, m = 1, lvls.shape[0]
    else:
        m, n = lvls.shape[0], lvls.shape[1]
    
    if min([m, n])!=1:
        raise TypeError('Vector required as input')
    lvls = lvls.ravel()
    
    if np.any(np.floor(lvls)!=levels) or np.any(lvls<1):
        raise ValueError('Integers required in input vector')
    
    ntrials = np.prod(lvls)
    ncycles = np.prod(lvls)
    cols = max([m, n])
    
    design = np.zeros((ntrials, cols), dtype=int)
    
    for k in range(cols):
        # get the coded levels (e.g., [0, 1, 2] for 3-level factor)
        coded_levels = range(int(lvls[k]))
        # how many times to repeat each level
        nreps = ntrials/ncycles
        # how many times to repeat each set of repeated levels
        ncycles = ncycles/lvls[k]
        # make a set of repeated levels
        reps = list(np.array([[v]*nreps for v in coded_levels]).ravel())
        # repeat the set of repeated levels
        cycles = reps*ncycles
        # assign the values to the appropriate column
        design[:, k] = cycles[:]
    
    return design

__all__.append('fullfact')

################################################################################

def ff2n(n):
    """
    Generate a strictly two-level full-factorial design.
    
    Parameters
    ----------
    n : int
        The number of factors in the design.
    
    Returns
    -------
    design : 2d-array
        A 2-D array containing the coded levels of every possible combination
        of factor levels, each column corresponding to a separate factor.
    
    Example
    -------
    Let's construct a design with three factors. This results in a design 
    of 8 trial conditions with 3 columns and 2 levels in each column::
    
        >>> design = ff2n(3)
        >>> design
        array([[0, 0, 0],
               [1, 0, 0],
               [0, 1, 0],
               [1, 1, 0],
               [0, 0, 1],
               [1, 0, 1],
               [0, 1, 1],
               [1, 1, 1]])
       
    """
    return fullfact([2]*int(n))
    
__all__.append('ff2n')

################################################################################

def boxbehnken(nfactors, center=None, blocksize=None):
    """
    Generates a Box-Behnken design.
    
    Parameters
    ----------
    nfactors : int
        The number of factors in the design (must be 3 or larger).
    
    Optional
    --------
    center : int
        The number of center points to include (a default is generated if not
        specified).
    blocksize : int
        The maximum number of points allowed in a block.
    
    Returns
    -------
    design : 2d-array
        A N-by-nfactors matrix, where N is the number of trial conditions in the
        design. Each row is scaled between -1 and 1.
    blk : 1d-array
        The vector of block numbers.
        
    See Also
    --------
    ccd
    
    Example
    -------
    
    """
    # Let's define some utility functions here #################################
    def getncenter(k):
        """
        Get default number of center points for Box-Behnken design.
        """
        v = [np.nan, np.nan, 3, 3, 6, 6, 6, 8, 10, 10, 12, 12, 12, 12, 12, 12]
        return v[min([k,len(v)])]

    def getbibd(k):
        """
        Get the balanced or partially balanced incomplete block design required
        to generate a Box-Behnken design, plus a set of block assignments if
        the design can be blocked based on the BIBD component.
        """
        Bb = []
        if k==3:
            B = [[1, 2], [1, 3], [2, 3]]
        elif k==4:
            B = [[1, 2], [3, 4], [1, 4], [2, 3], [1, 3], [2, 4]]
            Bb = [1, 1, 2, 2, 3, 3]
        elif k==5:
            B = [[1, 2], [3, 4], [2, 5], [1, 3], [4, 5], [2, 3], [1, 4],  
                [3, 5], [1, 5], [2, 4]]
            Bb = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        elif k==6:
            B = [[1, 2, 4], [2, 3, 5], [3, 4, 6], [1, 4, 5], [2, 5, 6], 
                [1, 3, 6]]
        elif k==7:
            B = [[4, 5, 6], [1, 6 ,7], [2, 5, 7], [1, 2, 4], [3, 4, 7], 
                [1, 3, 5], [2, 3, 6]]
        elif k==9:
            B = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], 
                [7, 8, 9], [1, 5, 9], [3, 4, 8], [2, 6, 7], [1, 6, 8], 
                [2, 4, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
            Bb = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
        elif k==10:
            B = [[2, 6, 7, 10], [1, 2, 5, 10], [2, 3, 7, 8], [2, 4, 6, 9], 
                [1, 8, 9, 10], [3, 4, 5, 10], [1, 4, 7, 8], [3, 5, 7, 9], 
                [1, 3, 6, 9], [4, 5, 6, 8]]
        elif k==11:
            B = [[3, 7, 8, 9, 11], [1, 4, 8, 9, 10], [2, 5, 9, 10, 11], 
                [1, 3, 6, 10, 11], [1, 2, 4, 7, 11], [1, 2, 3, 5, 8], 
                [2, 3, 4, 6, 9], [3, 4, 5, 7, 10], [4, 5, 6, 8, 11], 
                [1, 5, 6, 7, 9], [2, 6, 7, 8, 10]]
        elif k==12:
            B = [[1, 2, 5, 7], [2, 3, 6, 8], [3, 4, 7, 9], [4, 5, 8, 10], 
                [5, 6, 9, 11], [6, 7, 10, 12], [1, 7, 8, 11], [2, 8, 9, 12], 
                [1, 3, 9, 10], [2, 4, 10, 11], [3, 5, 11, 12], [1, 4, 6, 12]]
        elif k==16:
            B = [[1, 2, 6, 9], [3, 4, 8, 11], [5, 10, 13, 14], [7, 12, 15, 16],
                [2, 3, 7, 10], [1, 4, 5, 12], [6, 11, 14, 15], [8, 9, 13, 16],
                [2, 5, 6, 13], [4, 7, 8, 15], [1, 9, 10, 14], [3, 11, 12, 16],
                [3, 6, 7, 14], [1, 5, 8, 16], [2, 10, 11, 15], [4, 9, 12, 13],
                [1, 3, 13, 15], [2, 4, 14, 16], [5, 7, 9, 11], [6, 8, 10, 12],
                [4, 6, 10, 16], [3, 5, 9, 15], [1, 7, 11, 13], [2, 8, 12, 14]]
            Bb = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 
                6, 6, 6, 6]
        else:
            p = range(1, k)[::-1]
            I = np.zeros(k*(k-1)/2)
            I[np.cumsum(np.r_[1, p])] = 1
            I = np.cumsum(I)
            J = np.ones(k*(k-1)/2)
            J[np.cumsum(p)+1] = 2-p
            J[0] = 2
            J = np.cumsum(J)
            B = np.r_[I, J]
        
        return np.array(B), np.atleast_2d(Bb).T
   
    ############################################################################
    # Check the factor count
    assert nfactors>=3 and nfactors==np.floor(nfactors), \
        'Number of factors must be three or more.'
    
    # Check center points, generate if necessary
    if ncenter is None:
        ncenter = getncenter(nfactors)
    assert ncenter>0 and ncenter==np.floor(ncenter), \
        'Invalid center points (must be a positive integer).'
    
    # Check block size
    if blocksize is not None:
        assert blocksize>0 and blocksize==np.floor(blocksize), \
            'Invalid block size (must be a positive integer).'
    
    B, Bb = getbibd(nfactors)
    F, Fb = getfactorial(nfactors)
    
    d = mergeBF(B, F, ncenter, nfactors)
    
__all__.append('boxbehnken')

################################################################################

if __name__=='__main__':
    levels = [2, 4, 3]
    n = len(levels)
    design = fullfact(levels)
    print '{:}-Factor design with levels {:}:'.format(n, levels)
    print design
    
    design = ff2n(n)
    print '{:}-Factor, 2-level design:'.format(n)
    print design