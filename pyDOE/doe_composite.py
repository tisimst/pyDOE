import numpy as np
from doe_factorial import ff2n
from doe_star import star
from doe_union import union
from doe_repeat_center import repeat_center

def ccdesign(n, center=1, face='circumscribed'):
    """
    Central composite design
    
    Parameters
    ----------
    n : int
        The number of factors in the design.
    
    Optional
    --------
    center : int
        The number of center points (default: 0)
    face : str
        The relation between the start points and the corner (factorial) points.
        There are three options for this input:
        
        1. 'circumscribed' or 'ccc': This is the original form of the central
           composite design. The star points are at some distance ``alpha``
           from the center, based on the properties desired for the design.
           The start points establish new extremes for the low and high
           settings for all factors. These designs have circular, spherical,
           or hyperspherical symmetry and require 5 levels for each factor.
           Augmenting an existing factorial or resolution V fractional 
           factorial design with star points can produce this design.
        
        2. 'inscribed' or 'cci': For those situations in which the limits
           specified for factor settings are truly limits, the CCI design
           uses the factors settings as the star points and creates a factorial
           or fractional factorial design within those limits (in other words,
           a CCI design is a scaled down CCC design with each factor level of
           the CCC design divided by ``alpha`` to generate the CCI design).
           This design also requires 5 levels of each factor.
        
        3. 'faced' or 'ccf': In this design, the star points are at the center
           of each face of the factorial space, so ``alpha`` = +/-1. This 
           variety requires 3 levels of each factor. Augmenting an existing 
           factorial or resolution V design with appropriate star points can 
           also produce this design.
    
        Note 1: The value for ``alpha`` is automatically calculated to maintain 
        rotatability.
        
        Note 2: Fractional factorial designs are not (yet) available here.
        
    Returns
    -------
    mat : 2d-array
        The design matrix with coded levels -1 and 1
    
    Example
    -------
    ::
    
        >>> ccdesign(3)
        array([[-1.        , -1.        , -1.        ],
               [ 1.        , -1.        , -1.        ],
               [-1.        ,  1.        , -1.        ],
               [ 1.        ,  1.        , -1.        ],
               [-1.        , -1.        ,  1.        ],
               [ 1.        , -1.        ,  1.        ],
               [-1.        ,  1.        ,  1.        ],
               [ 1.        ,  1.        ,  1.        ],
               [-1.68179283,  0.        ,  0.        ],
               [ 1.68179283,  0.        ,  0.        ],
               [ 0.        , -1.68179283,  0.        ],
               [ 0.        ,  1.68179283,  0.        ],
               [ 0.        ,  0.        , -1.68179283],
               [ 0.        ,  0.        ,  1.68179283],
               [ 0.        ,  0.        ,  0.        ]])
       
    """
    H1 = ff2n(n)
    H2 = star(n)
    
    if face.lower() in ('circumscribed', 'ccc'):
        alpha = (H1.shape[0])**0.25
    elif face.lower() in ('inscribed', 'cci'):
        alpha = 1
        H1 /= (H1.shape[0])**0.25
    elif face.lower() in ('faced', 'ccf'):
        alpha = 1
    else:
        raise Exception, 'Invalid input for "face": {:}'.format(face)
        
    H = union(H1, alpha*H2)
    H = np.c_[H.T, repeat_center(nb_var, center).T].T
    return H