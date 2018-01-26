pyDOE2: An experimental design package for python
=====================================================

`pyDOE2` is a fork of the [`pyDOE`](https://github.com/tisimst/pyDOE) package 
that is designed to help the scientist, engineer, statistician, etc., to 
construct appropriate experimental designs.

This fork came to life to solve bugs and issues that remained unsolved in the
original package.

Capabilities
------------

The package currently includes functions for creating designs for any 
number of factors:

- Factorial Designs
    - General Full-Factorial (``fullfact``)
    - 2-level Full-Factorial (``ff2n``)
    - 2-level Fractional Factorial (``fracfact``)
    - Plackett-Burman (``pbdesign``)
- Response-Surface Designs 
    - Box-Behnken (``bbdesign``)
    - Central-Composite (``ccdesign``)
- Randomized Designs
    - Latin-Hypercube (``lhs``)
  
See the original [package homepage](http://pythonhosted.org/pyDOE) for details 
on usage and other notes.

Requirements
------------

- NumPy
- SciPy

Installation and download
-------------------------

Through pip:

```
pip install pyDOE2
```


Credits
-------

`pyDOE` was originally published by the following individuals for use with
Scilab:
    
- Copyright (C) 2012 - 2013 - Michael Baudin
- Copyright (C) 2012 - Maria Christopoulou
- Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
- Copyright (C) 2009 - Yann Collette
- Copyright (C) 2009 - CEA - Jean-Marc Martinez

- Website: forge.scilab.org/index.php/p/scidoe/sourcetree/master/macros

Much thanks goes to these individuals.

And thanks goes out to the following for finding and offering solutions for
bugs:

- Ashmeet Singh

And thanks to the following individuals for forking and working with `pyDOE2`:

- Copyright (C) 2018 - Rickard Sjögren and Daniel Svensson


License
-------

This package is provided under two licenses:

1. The *BSD License* (3-clause)
2. Any other that the author approves (just ask!)

References
----------

- [Factorial designs](http://en.wikipedia.org/wiki/Factorial_experiment)
- [Plackett-Burman designs](http://en.wikipedia.org/wiki/Plackett-Burman_design)
- [Box-Behnken designs](http://en.wikipedia.org/wiki/Box-Behnken_design)
- [Central composite designs](http://en.wikipedia.org/wiki/Central_composite_design)
- [Latin-Hypercube designs](http://en.wikipedia.org/wiki/Latin_hypercube_sampling)
