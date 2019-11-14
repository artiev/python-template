.. _chapter-standard-tools:

Standard Tools
==============

This projects uses the `pylint` and `coverage` modules to ensure a decent level
of code quality. Both module are configured through their rc files at the root
of the project folder. The test coverage is itself dependent on the `pytest`
module. Continuous integration through https://travis-ci.org and
https://codecov.io is also pre-configured and discussed in another chapter
(:ref:`section-travis-codecov-config`). The documentation itself is built using
`sphinx` with the `autodoc` extension. A direct connection to
https://readthedocs.io is ready to be established.

.. toctree::
    :maxdepth: 4

    coverage.rst
    linter.rst
    unittest.rst
    documentation.rst

.. _chapter-custom-tools:

Custom Tools
============

Unfortunately, sometimes the standard way is not always the most
user-friendly, or the optimal process. So despite generally advising against
it, I've collected a few tools of my own design to help work out some
specific problems I could not solve otherwise.

.. toctree::
    :maxdepth: 4

    custom.rst
