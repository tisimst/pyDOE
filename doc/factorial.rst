================================================================================
Factorial Designs
================================================================================

In this section, the following kinds of *factorial designs* will be described:

- General Full-Factorial
- 2-Level Full-Factorial
- 2-Level Fractional-Factorial
- Plackett-Burman

General Full-Factorial (``fullfact``)
=====================================

This kind of design offers full flexibility as to the number of discrete 
levels for each factor in the design. Its usage is simple::

    >>> fullfact(levels)

where ``levels`` is an array of integers, like::

    >>> fullfact([2, 3])
    array([[ 0.,  0.],
           [ 0.,  1.],
           [ 0.,  2.],
           [ 1.,  0.],
           [ 1.,  1.],
           [ 1.,  2.]])

As can be seen in the output, the design matrix has as many columns as 
items in the input array.

2-Level Full-Factorial (``ff2n``)
=================================

This function is a convenience wrapper to ``fullfact`` that forces all the
factors to have two levels each, you simple tell it how many factors to
create a design for::

    >>> ff2n(3)
    array([[ 0.,  0.,  0.],
           [ 0.,  0.,  1.],
           [ 0.,  1.,  0.],
           [ 0.,  1.,  1.],
           [ 1.,  0.,  0.],
           [ 1.,  0.,  1.],
           [ 1.,  1.,  0.],
           [ 1.,  1.,  1.]])

2-Level Fractional-Factorial (``fracfact``)
===========================================

This function requires a little more knowledge of how the *confounding*
will be allowed (this means that some factor effects get muddled with
other interaction effects, so it's harder to distinguish between them).

The input to ``fracfact`` is a generator string of symbolic characters
(lowercase or uppercase, but not both) separated by spaces, like::

    >>> gen = 'a b ab' 

This design would result in a 3-column matrix, where the confounding effect is 
implicitly defined as ``"c = ab"``. This means that the factor in the third 
column is confounded with the interaction of the factors in the first two 
columns. The design ends up looking like this::

    >>> fracfact('a b ab')
    array([[ 0.,  0.,  1.],
           [ 0.,  1.,  0.],
           [ 1.,  0.,  0.],
           [ 1.,  1.,  1.]])

Fractional factorial designs are usually specified using the notation 
:math:`2^{k-p}`, where k is the number of columns and p is the number 
of effects that are confounded. This is also known as a 
*Resolution (k-p+1)* design. In terms of *resolution* level, higher is
"better". The above design would be considered a :math:`2^{3-1}` 
fractional factorial design, a 1/2-fraction design, or a *Resolution III*
design. Another common design is a Resolution III, :math:`2^{7-4}` 
fractional factorial and would be created using the following string 
generator::

    >>> fracfact('a b c ab ac bc abc')
    array([[ 0.,  0.,  0.,  1.,  1.,  1.,  0.],
           [ 0.,  0.,  1.,  1.,  0.,  0.,  1.],
           [ 0.,  1.,  0.,  0.,  1.,  0.,  1.],
           [ 0.,  1.,  1.,  0.,  0.,  1.,  0.],
           [ 1.,  0.,  0.,  0.,  0.,  1.,  1.],
           [ 1.,  0.,  1.,  0.,  1.,  0.,  0.],
           [ 1.,  1.,  0.,  1.,  0.,  0.,  0.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.]])
       
More sophisticated generator strings can be created using the "+" and 
"-" operators. The "-" operator swaps the levels of that column like 
this::

    >>> fracfact('a b -ab')
    array([[ 0.,  0.,  0.],
           [ 0.,  1.,  1.],
           [ 1.,  0.,  1.],
           [ 1.,  1.,  0.]]) 

In order to reduce confounding, we can utilize the ``fold`` function::

    >>> m = fracfact('a b ab')
    >>> fold(m)
    array([[ 0.,  0.,  1.],
           [ 0.,  1.,  0.],
           [ 1.,  0.,  0.],
           [ 1.,  1.,  1.],
           [ 1.,  1.,  0.],
           [ 1.,  0.,  1.],
           [ 0.,  1.,  1.],
           [ 0.,  0.,  0.]])

Applying the fold to all columns in the design breaks the alias chains
between every *main factor and two-factor interactions*. This means that
we can then estimate *all the main effects clear of any two-factor 
interactions*. Typically, when all columns are folded, this "upgrades"
the resolution of the design.

By default, ``fold`` applies the level swapping to all 
columns, but we can fold specific columns, if desired, by supplying an 
array to the keyword ``columns``::

    >>> fold(m, columns=[2])
    array([[ 0.,  0.,  1.],
           [ 0.,  1.,  0.],
           [ 1.,  0.,  0.],
           [ 1.,  1.,  1.],
           [ 0.,  0.,  0.],
           [ 0.,  1.,  1.],
           [ 1.,  0.,  1.],
           [ 1.,  1.,  0.]])

.. note::
   Care should be taken to decide the appropriate alias structure for 
   your design and the effects that folding has on it.

Plackett-Burman (``pbdesign``)
==============================

Another way to generate fractional-factorial designs is through the use
of **Plackett-Burman** designs. These designs are unique in that the 
number of trial conditions (rows) expands by multiples of four (e.g. 4,
8, 12, etc.). The max number of columns allowed before a design increases
the number of rows is always one less than the multiple of four.

For example, I can use up to 3 factors in a design with 4 columns::

    >>> pbdesign(4)
    array([[ 0.,  0.,  1.],
           [ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 1.,  1.,  1.]])

But if I want to do four factors, the design needs to increase the number
of rows up to the next multiple of four (8 in this case)::

    >>> pbdesign(8)
    array([[ 0.,  0.,  1.,  0.,  1.,  1.,  0.],
           [ 1.,  0.,  0.,  0.,  0.,  1.,  1.],
           [ 0.,  1.,  0.,  0.,  1.,  0.,  1.],
           [ 1.,  1.,  1.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  1.,  1.,  0.,  0.,  1.],
           [ 1.,  0.,  0.,  1.,  1.,  0.,  0.],
           [ 0.,  1.,  0.,  1.,  0.,  1.,  0.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.]])

So, an 8-run Plackett-Burman design can handle up to (8 - 1) or 7 factors.

More Information
================

If the user needs more information about appropriate designs, please 
consult the following articles on Wikipedia:

- `Factorial designs`_
- `Plackett-Burman designs`_

There is also a wealth of information on the `NIST`_ website about the
various design matrices that can be created.

Any questions, comments, bug-fixes, etc. can be forwarded to the `author`_.

.. _author: mailto:tisimst@gmail.com
.. _Factorial designs: http://en.wikipedia.org/wiki/Factorial_experiment
.. _Plackett-Burman designs: http://en.wikipedia.org/wiki/Plackett-Burman_design
.. _NIST: http://www.itl.nist.gov/div898/handbook/pri/pri.htm