import numpy as np

__all__ = ['fold']

def fold(H, columns=None):
    """
    Fold a design to reduce confounding effects.
    
    Parameters
    ----------
    H : 2d-array
        The design matrix to be folded.
    columns : array
        Indices of of columns to fold (Default: None). If ``columns=None`` is
        used, then all columns will be folded.
    
    Returns
    -------
    Hf : 2d-array
        The folded design matrix.
    
    Examples
    --------
    ::
    
    """
    H = np.array(H)
    assert len(H.shape)==2, 'Input design matrix must be 2d.'
    
    if columns is None:
        columns = range(H.shape[1])
    
    Hf = H.copy()
    
    for col in columns:
        vals = np.unique(H[:, col])
        assert len(vals)==2, 'Input design matrix must be 2-level factors only.'
        
        for i in xrange(H.shape[0]):
            Hf[i, col] = vals[0] if H[i, col]==vals[1] else vals[1]
    
    Hf = np.vstack((H, Hf))
    
    return Hf
        
    