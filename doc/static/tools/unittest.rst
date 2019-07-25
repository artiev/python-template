Unit Tests
==========

The unit testing scheme of this template is designed to offer the user the
possibility to not only create unit tests within the `test/` folder, but also
the option to separate unit tests in what I will call `collections`.

The reasoning behind it is that not 100% of the project needs to be tested
during coding sessions, as opposed to continuous integration regressions, hence
the ability for any contributor to design their own test collections.

.. code-block::

    test
    ├── collection_full.py
    ├── test_main.py
    └── test_tools.py

When computing code-coverage, the entry point of is always the complete
collection of tests located in the `test/` folder. Adding new tests to the
collection is as simple as creating a new file within that directory structure.

.. code-block:: python

    from test.test_main import TestMainOperations

For more info on unittesting in python, see
https://docs.python.org/3/library/unittest.html.

.. note::

    More coming soon!
