.. _chapter-tools:

Tools and Libraries
===================

This projects uses the `pylint` and `coverage` modules to ensure a decent level
of code quality. Both module are configured through their rc files at the root
of the project folder. The test coverage is itself dependent on the `pytest`
module. Continuous integration through https://travis-ci.org and https://codecov.io
is also pre-configured and discussed in another chapter
(:ref:`section-travis-codecov-config`). The documentation itself is built using
`sphinx` with the `autodoc` extension. A direct connection to
https://readthedocs.io is ready to be established.


.. toctree::
    :maxdepth: 2
    :caption: Table of Content:

    coverage.rst
    linter.rst
    unittest.rst
    documentation.rst
    custom.rst
