=====================================================
``pyDOE``: The experimental design package for python
=====================================================

The ``pyDOE`` package is designed to help the 
**scientist, engineer, statistician,** etc., to construct appropriate 
**experimental designs**.

Capabilities
------------

The package currently includes functions for creating designs for any number of
factors:

1. **2-level full-factorial**
2. **Generic full-factorial**
3. **Box-Behnken**
4. **Central-Composite**

The following are *in the works* (probably), so stay tuned!
   
1. Plackett-Burman designs
2. Fractional-factorial designs
3. Split-plot designs
4. Incomplete block designs
5. D-Optimal designs

Requirements
------------

- NumPy

Basic Examples
--------------

The main import::

    >>> from pyDOE import *
    
2-Level full-factorial designs (``ff2n``) only require the **number of factors**::

    >>> ff2n(3)
    array([[-1., -1., -1.],
           [ 1., -1., -1.],
           [-1.,  1., -1.],
           [ 1.,  1., -1.],
           [-1., -1.,  1.],
           [ 1., -1.,  1.],
           [-1.,  1.,  1.],
           [ 1.,  1.,  1.]])
    
General full-factorial designs (``fullfact``) require an **array of integers**, one 
integer for each factor, where the integer value is the number of levels 
for that factor::

    >>> fullfact([2, 4, 3])
    array([[ 0.,  0.,  0.],
           [ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 1.,  1.,  0.],
           [ 0.,  2.,  0.],
           [ 1.,  2.,  0.],
           [ 0.,  3.,  0.],
           [ 1.,  3.,  0.],
           [ 0.,  0.,  1.],
           [ 1.,  0.,  1.],
           [ 0.,  1.,  1.],
           [ 1.,  1.,  1.],
           [ 0.,  2.,  1.],
           [ 1.,  2.,  1.],
           [ 0.,  3.,  1.],
           [ 1.,  3.,  1.],
           [ 0.,  0.,  2.],
           [ 1.,  0.,  2.],
           [ 0.,  1.,  2.],
           [ 1.,  1.,  2.],
           [ 0.,  2.,  2.],
           [ 1.,  2.,  2.],
           [ 0.,  3.,  2.],
           [ 1.,  3.,  2.]])
       
Box-Behnken designs (``bbdesign``) require the **number of factors** and 
**optional number of center points** 
(*NOTE: the number of center points is not automatically calculated!*
*It needs to be given explicitly*, default = 1)::

    >>> bbdesign(3, center=5)
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
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])
    
Central-Composite designs (``ccdesign``) require the **number of factors**, an optional
**number of center points**, and an optional **type description** (i.e.
``face=...`` which can be one of:

1. "circumscribed" or "ccc" (default)
2. "faced" or "ccf"
3. "inscribed" or "cci" 

(*Note: the alpha value for the star points is automatically calculated*)::

    >>> ccdesign(3, face='ccc', center=4)
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
           [ 0.        ,  0.        ,  0.        ],
           [ 0.        ,  0.        ,  0.        ],
           [ 0.        ,  0.        ,  0.        ],
           [ 0.        ,  0.        ,  0.        ]])

Contact
-------

Any feedback, questions, bug reports, or words of encouragement can
be sent to the `author`_.

License
-------

This package is provided under two licenses:

1. The *BSD License*
2. Any other that the author approves (just ask!)

References
----------

- `Factorial designs`_
- `Box-Behnken designs`_
- `Central composite designs`_


.. _author: mailto:tisimst@gmail.com
.. _Factorial designs: http://en.wikipedia.org/wiki/Factorial_experiment
.. _Box-Behnken designs: http://en.wikipedia.org/wiki/Box-Behnken_design
.. _Central composite designs: http://en.wikipedia.org/wiki/Central_composite_design