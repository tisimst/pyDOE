=====================================================
``pyDOE``: The experimental design package for python
=====================================================

The ``pyDOE`` package is designed to help the 
**scientist, engineer, statistician,** etc., to construct appropriate 
**experimental designs**.

Capabilities
------------

The package currently includes functions for creating designs for any 
number* of factors:

- *Factorial Designs*
  #. **2-level Full-Factorial** (``ff2n``)
  #. **Generic Full-Factorial** (``fullfact``)
  #. **2-level Fractional Factorial** (``fracfact``)
  #. **Plackett-Burman** (``pbdesign``)
- *Response-Surface Designs* 
  #. **Box-Behnken** (``bbdesign``)
  #. **Central-Composite** (``ccdesign``)

(* Plackett-Burman designs require the number of factors to be a multiple
of 4.)

The following are *in the works* (probably), so stay tuned!
   
#. Split-plot designs
#. Incomplete block designs
#. D-Optimal designs

Requirements
------------

- NumPy
- SciPy

Contact
-------

Any feedback, questions, bug reports, or success stores should
be sent to the `author`_. I'd love to hear from you!

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
- `Plackett-Burman designs`_

.. _author: mailto:tisimst@gmail.com
.. _Factorial designs: http://en.wikipedia.org/wiki/Factorial_experiment
.. _Box-Behnken designs: http://en.wikipedia.org/wiki/Box-Behnken_design
.. _Central composite designs: http://en.wikipedia.org/wiki/Central_composite_design
.. _Plackett-Burman designs: http://en.wikipedia.org/wiki/Plackett-Burman_design

