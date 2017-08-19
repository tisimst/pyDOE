.. _factorial:

================================================================================
Factorial Designs
================================================================================

In this section, the following kinds of *factorial designs* will be described:

- :ref:`General Full-Factorial <general_full_factorial>`
- :ref:`2-Level Full-Factorial <2_level_full_factorial>`
- :ref:`2-Level Fractional-Factorial <fractional_factorial>`
- :ref:`Plackett-Burman <plackett_burman>`

.. hint::
   All available designs can be accessed after a simple import statement::

    >>> from pyDOE import *


.. index:: General Full-Factorial

.. _general_full_factorial:

General Full-Factorial (``fullfact``)
=====================================

This kind of design offers full flexibility as to the number of discrete
levels for each factor in the design. Its usage is simple::

    >>> fullfact(levels)

where ``levels`` is an array of integers, like::

    >>> fullfact([2, 3])
    array([[ 0.,  0.],
           [ 1.,  0.],
           [ 0.,  1.],
           [ 1.,  1.],
           [ 0.,  2.],
           [ 1.,  2.]])

As can be seen in the output, the design matrix has as many columns as
items in the input array.

.. index:: 2-Level Full Factorial

.. _2_level_full_factorial:

2-Level Full-Factorial (``ff2n``)
=================================

This function is a convenience wrapper to ``fullfact`` that forces all the
factors to have two levels each, you simple tell it how many factors to
create a design for::

    >>> ff2n(3)
    array([[-1., -1., -1.],
           [ 1., -1., -1.],
           [-1.,  1., -1.],
           [ 1.,  1., -1.],
           [-1., -1.,  1.],
           [ 1., -1.,  1.],
           [-1.,  1.,  1.],
           [ 1.,  1.,  1.]])

.. index:: 2-Level Fractional Factorial

.. _fractional_factorial:

2-Level Fractional-Factorial (``fracfact``)
===========================================

This function requires a little more knowledge of how the *confounding*
will be allowed (this means that some factor effects get muddled with
other interaction effects, so it's harder to distinguish between them).

Let's assume that we just can't afford (for whatever reason) the number
of runs in a *full-factorial* design. We can systematically decide on a
*fraction of the full-factorial* by allowing some of the factor *main
effects* to be confounded with other factor *interaction effects*. This
is done by defining an *alias* structure that defines, symbolically,
these interactions. These alias structures are written like "C = AB" or
"I = ABC", or "AB = CD", etc. These define how one column is related to
the others.

For example, the alias "C = AB" or "I = ABC" indicate that there are
three factors (A, B, and C) and that the main effect of factor
C is confounded with the interaction effect of the product AB, and by
extension, A is confounded with BC and B is confounded with AC. A full-
factorial design with these three factors results in a design matrix with
8 runs, but we will assume that we can only afford 4 of those runs. To
create this *fractional* design, we need a matrix with three columns, one
for A, B, and C, only now where the levels in the C column is created by
the product of the A and B columns.

The input to ``fracfact`` is a generator string of symbolic characters
(lowercase or uppercase, but not both) separated by spaces, like::

    >>> gen = 'a b ab'

This design would result in a 3-column matrix, where the third column is
implicitly defined as ``"c = ab"``. This means that the factor in the third
column is confounded with the interaction of the factors in the first two
columns. The design ends up looking like this::

    >>> fracfact('a b ab')
    array([[-1., -1.,  1.],
           [ 1., -1., -1.],
           [-1.,  1., -1.],
           [ 1.,  1.,  1.]])

Fractional factorial designs are usually specified using the notation
2^(k-p), where k is the number of columns and p is the number
of effects that are confounded. In terms of *resolution* level, higher is
"better". The above design would be considered a 2^(3-1)
fractional factorial design, a 1/2-fraction design, or a *Resolution III*
design (since the smallest alias "I=ABC" has three terms on the right-hand
side). Another common design is a Resolution III, 2^(7-4)
fractional factorial and would be created using the following string
generator::

    >>> fracfact('a b ab c ac bc abc')
    array([[-1., -1.,  1., -1.,  1.,  1., -1.],
           [ 1., -1., -1., -1., -1.,  1.,  1.],
           [-1.,  1., -1., -1.,  1., -1.,  1.],
           [ 1.,  1.,  1., -1., -1., -1., -1.],
           [-1., -1.,  1.,  1., -1., -1.,  1.],
           [ 1., -1., -1.,  1.,  1., -1., -1.],
           [-1.,  1., -1.,  1., -1.,  1., -1.],
           [ 1.,  1.,  1.,  1.,  1.,  1.,  1.]])

More sophisticated generator strings can be created using the "+" and
"-" operators. The "-" operator swaps the levels of that column like
this::

    >>> fracfact('a b -ab')
    array([[-1., -1., -1.],
           [ 1., -1.,  1.],
           [-1.,  1.,  1.],
           [ 1.,  1., -1.]])

In order to reduce confounding, we can utilize the ``fold`` function::

    >>> m = fracfact('a b ab')
    >>> fold(m)
    array([[-1., -1.,  1.],
           [ 1., -1., -1.],
           [-1.,  1., -1.],
           [ 1.,  1.,  1.],
           [ 1.,  1., -1.],
           [-1.,  1.,  1.],
           [ 1., -1.,  1.],
           [-1., -1., -1.]])

Applying the fold to all columns in the design breaks the alias chains
between every *main factor and two-factor interactions*. This means that
we can then estimate *all the main effects clear of any two-factor
interactions*. Typically, when all columns are folded, this "upgrades"
the resolution of the design.

By default, ``fold`` applies the level swapping to all columns, but we can
fold specific columns (first column = 0), if desired, by supplying an array
to the keyword ``columns``::

    >>> fold(m, columns=[2])
    array([[-1., -1.,  1.],
           [ 1., -1., -1.],
           [-1.,  1., -1.],
           [ 1.,  1.,  1.],
           [-1., -1., -1.],
           [ 1., -1.,  1.],
           [-1.,  1.,  1.],
           [ 1.,  1., -1.]])

Another way to reduce confounding it to scan several (or all) available
fractional designs and pick the one that has less confounding. The function
``fracfact_opt`` performs just that. For a 2^k-p fractional factorial the
function scans all generators that create at most 2^k-p experiments, and pick
the one that has confounding on interactions of order as high as possible:

    >>> design, alias_map, alias_cost = fracfact_opt(6, 2)
    >>> design
    'a b c d bcd acd'
    >>> print('\n'.join(alias_map))
    a = bef = cdf = abcde
    b = aef = cde = abcdf
    c = adf = bde = abcef
    d = acf = bce = abdef
    e = abf = bcd = acdef
    f = abe = acd = bcdef
    af = be = cd = abcdef
    ab = ef = acde = bcdf
    ac = df = abde = bcef
    ad = cf = abce = bdef
    ae = bf = abcd = cdef
    bc = de = abdf = acef
    bd = ce = abcf = adef
    abc = ade = bdf = cef
    abd = ace = bcf = def
    abef = acdf = bcde

You can generate the human-readable alias_map of any design with the function
`fracfact_aliasing`:

    >>> print('\n'.join(fracfact_aliasing(fracfact('a b ab'))[0]))
    a = bc
    b = ac
    c = ab
    abc

.. note::
   Care should be taken to decide the appropriate alias structure for
   your design and the effects that folding has on it.

.. index:: Plackett-Burman

.. _plackett_burman:

Plackett-Burman (``pbdesign``)
==============================

Another way to generate fractional-factorial designs is through the use
of **Plackett-Burman** designs. These designs are unique in that the
number of trial conditions (rows) expands by multiples of four (e.g. 4,
8, 12, etc.). The max number of columns allowed before a design increases
the number of rows is always one less than the next higher multiple of four.

For example, I can use up to 3 factors in a design with 4 rows::

    >>> pbdesign(3)
    array([[-1., -1.,  1.],
           [ 1., -1., -1.],
           [-1.,  1., -1.],
           [ 1.,  1.,  1.]])

But if I want to do 4 factors, the design needs to increase the number
of rows up to the next multiple of four (8 in this case)::

    >>> pbdesign(4)
    array([[-1., -1.,  1., -1.],
           [ 1., -1., -1., -1.],
           [-1.,  1., -1., -1.],
           [ 1.,  1.,  1., -1.],
           [-1., -1.,  1.,  1.],
           [ 1., -1., -1.,  1.],
           [-1.,  1., -1.,  1.],
           [ 1.,  1.,  1.,  1.]])

Thus, an 8-run Plackett-Burman design can handle up to (8 - 1) = 7 factors.

As a side note, It just so happens that the Plackett-Burman and 2^(7-4)
fractional factorial design are identical::

    >>> np.all(pbdesign(7)==fracfact('a b ab c ac bc abc'))
    True

.. index:: Factorial Designs Support

More Information
================

If the user needs more information about appropriate designs, please
consult the following articles on Wikipedia:

- `Factorial designs`_
- `Plackett-Burman designs`_

There is also a wealth of information on the `NIST`_ website about the
various design matrices that can be created as well as detailed information
about designing/setting-up/running experiments in general.

Any questions, comments, bug-fixes, etc. can be forwarded to the `author`_.

.. _author: mailto:tisimst@gmail.com
.. _Factorial designs: http://en.wikipedia.org/wiki/Factorial_experiment
.. _Plackett-Burman designs: http://en.wikipedia.org/wiki/Plackett-Burman_design
.. _NIST: http://www.itl.nist.gov/div898/handbook/pri/pri.htm