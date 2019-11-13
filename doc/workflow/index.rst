.. _chapter-workflow:

Workflow
========

Having a sold and documented workflow is paramount to maintaining a clean
codebase when multiple contributors are involved. In this chapter, I'm
highlighting some of the conventions I adopted, while also trying to discuss
the reasons leading me to these choices.

.. toctree::
    :maxdepth: 4

    ci/index.rst
    conventions/index.rst
    structure/index.rst

.. _chapter-standard-tools:

Standard Tools
==============

This projects uses the `pylint` and `coverage` modules to ensure a decent level
of code quality. Both module are configured through their rc files at the root
of the project folder. The test coverage is itself dependent on the `pytest`
module. Continuous integration through https://travis-ci.org and https://codecov.io
is also pre-configured and discussed in another chapter
(:ref:`section-travis-codecov-config`). The documentation itself is built using
`sphinx` with the `autodoc` extension. A direct connection to
https://readthedocs.io is ready to be established.

.. toctree::
    :maxdepth: 4

    tools/coverage.rst
    tools/linter.rst
    tools/unittest.rst
    tools/documentation.rst

.. _chapter-custom-tools:

Custom Tools
============

Unfortunately, sometimes the standard way is not always the most
user-friendly, or the optimal process. So despite generally advising against
it, I've collected a few tools of my own design to help work out some
specific problems I could not solve otherwise.

.. toctree::
    :maxdepth: 4

    tools/custom.rst
