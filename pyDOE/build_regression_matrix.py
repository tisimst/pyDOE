import numpy as np

def grep(haystack, needle):
    start = 0
    while True:
        start = haystack.find(needle, start)
        if start==-1:
            return
        yield start
        start += len(needle)

def build_regression_matrix(H, model, build=None):
    """
    Build a regression matrix using a DOE matrix and a list of monomials.
    
    Parameters
    ----------
    H : 2d-array
    model : str
    build : bool-array
    
    Returns
    -------
    R : 2d-array
    
    """
    ListOfTokens = model.split(' ')
    if H.shape[1]==1:
        size_index = len(str(H.shape[0]))
    else:
        size_index = len(str(H.shape[1]))
    
    if build is None:
        build = [True]*len(ListOfTokens)
    
    # Test if the vector has the wrong direction (lines instead of columns)
    if H.shape[0]==1:
        H = H.T
    
    # Collect the list of monomials
    Monom_Index = []
    for i in xrange(len(ListOfTokens)):
        if build[i]:
            Monom_Index += [grep(ListOfTokens, 'x' + str(0)*(size_index - \
            len(str(i))) + str(i))]
    
    Monom_Index = -np.sort(-Monom_Index)
    Monom_Index = np.unique(Monom_Index)
    
    if H.shape[1]==1:
        nb_var = H.shape[0]  # vector "mode": the number of vars is equal to the number of lines of H
        VectorMode = True
        
        for i in xrange(nb_var):
            for j in xrange(ListOfTokens.shape[0]):
                ListOfTokens[j] = ListOfTokens[j].replace(
                    'x' + str(0)*(size_index - len(str(i))) + str(i),
                    'H(' + str(i) + ')')
    else:
        nb_var = H.shape[0]  # matrix "mode": the number of vars is equal to the number of columns of H
        VectorMode = False
        
        for i in xrange(nb_var):
            for j in xrange(ListOfTokens.shape[0]):
                ListOfTokens[j] = ListOfTokens[j].replace(
                    'x' + str(0)*(size_index - len(str(i))) + str(i),
                    'H[i,' + str(i) + ')')
    
    # Now build the regression matrix
    if VectorMode:
        R = np.zeros((len(ListOfTokens), 1))
        for j in xrange(len(ListOfTokens)):
            R[j, 0] = eval(ListOfTokens[j])
    else:
        R = np.zeros((H.shape[0], len(ListOfTokens)))
        for i in xrange(H.shape[0]):
            for j in xrange(len(ListOfTokens)):
                R[i, j] = eval(ListOfTokens[j])
    
    return R
    
    