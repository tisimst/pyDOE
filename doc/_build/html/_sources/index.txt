.. meta::
   :description: Design of experiments for Python
   :keywords: DOE, design of experiments, experimental design,
        optimization, statistics

=====================================================
``pyDOE``: The experimental design package for python
=====================================================

The ``pyDOE`` package is designed to help the 
**scientist, engineer, statistician,** etc., to construct appropriate 
**experimental designs**.

Capabilities
============

The package currently includes functions for creating designs for any 
number of factors:

- *Factorial Designs*

  #. **General Full-Factorial** (``fullfact``)

  #. **2-level Full-Factorial** (``ff2n``)

  #. **2-level Fractional Factorial** (``fracfact``)

  #. **Plackett-Burman** (``pbdesign``)

- *Response-Surface Designs* 

  #. **Box-Behnken** (``bbdesign``)

  #. **Central-Composite** (``ccdesign``)

The following are *in the works* (probably), so stay tuned!
   
#. Split-plot designs

#. Incomplete block designs

#. D-Optimal designs

Requirements
============

- NumPy
- SciPy

.. index:: installation

.. _installing this package:

Installation and download
=========================

Important note
--------------

The installation commands below should be **run in a DOS or Unix
command shell** (*not* in a Python shell).

Under Windows (version 7 and earlier), a command shell can be obtained
by running ``cmd.exe`` (through the Run… menu item from the Start
menu). Under Unix (Linux, Mac OS X,…), a Unix shell is available when
opening a terminal (in Mac OS X, the Terminal program is found in the
Utilities folder, which can be accessed through the Go menu in the
Finder).

Automatic install or upgrade
----------------------------

One of the automatic installation or upgrade procedures below might work 
on your system, if you have a Python package installer or use certain 
Linux distributions.

Under Unix, it may be necessary to prefix the commands below with 
``sudo``, so that the installation program has **sufficient access 
rights to the system**.

If you have `pip <http://pip.openplans.org/>`_, you can try to install
the latest version with

.. code-block:: sh

   pip install --upgrade pyDOE

If you have setuptools_, you can try to automatically install or
upgrade this package with

.. code-block:: sh

   easy_install --upgrade pyDOE

Manual download and install
---------------------------

Alternatively, you can simply download_ the package archive from the
Python Package Index (PyPI) and unpack it.  The package can then be
installed by **going into the unpacked directory**
(:file:`pyDOE-...`), and running the provided :file:`setup.py`
program with

.. code-block:: sh

   python setup.py install

or, for an installation in the user Python library (no additional access
rights needed):

.. code-block:: sh

   python setup.py install --user

or, for an installation in a custom directory :file:`my_directory`:

.. code-block:: sh

   python setup.py install --install-lib my_directory

or, if additional access rights are needed (Unix):

.. code-block:: sh

   sudo python setup.py install

You can also simply **move** the :file:`pyDOE-py*` directory
that corresponds best to your version of Python to a location that
Python can import from (directory in which scripts using
:mod:`pyDOE` are run, etc.); the chosen
:file:`pyDOE-py*` directory should then be renamed
:file:`pyDOE`. Python 3 users should then run ``2to3 -w .``
from inside this directory so as to automatically adapt the code to
Python 3.

Source code
-----------

The latest, bleeding-edge but working `code
<https://github.com/tisimst/pyDOE/tree/master/pyDOE>`_
and `documentation source
<https://github.com/tisimst/pyDOE/tree/master/doc/>`_ are
available `on GitHub <https://github.com/tisimst/pyDOE/>`_.

.. index:: support

Contact
=======

Any feedback, questions, bug reports, or success stores should
be sent to the `author`_. I'd love to hear from you!

License
=======

This package is provided under two licenses:

1. The *BSD License*
2. Any other that the author approves (just ask!)

References
==========

- `Factorial designs`_
- `Plackett-Burman designs`_
- `Box-Behnken designs`_
- `Central composite designs`_

.. _author: mailto:tisimst@gmail.com
.. _Factorial designs: http://en.wikipedia.org/wiki/Factorial_experiment
.. _Box-Behnken designs: http://en.wikipedia.org/wiki/Box-Behnken_design
.. _Central composite designs: http://en.wikipedia.org/wiki/Central_composite_design
.. _Plackett-Burman designs: http://en.wikipedia.org/wiki/Plackett-Burman_design
.. _setuptools: http://pypi.python.org/pypi/setuptools
.. _download: http://pypi.python.org/pypi/pyDOE/#downloads

