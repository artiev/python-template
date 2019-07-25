Code Coverage based on Unit Tests
=================================

This template relies on the use of the `coverage` module in conjunction with
the `unittest` module to automatically compile code coverage report.

Underlined here is the importance of writing tests (prepared folder `test/`)
which not only maximize coverage, but also prevent breaking applications
later during refactoring and maintenance stages of a project's lifecycle.

.. warning::

    Code coverage alone is not a good indicator of project health.

The makefile offer the `test` and the `coverage` targets. The former collects
and run unit tests while gathering coverage statistics, then prints out stats
in the console only. The second target calls `test` then generates an html
report, located under `coverage/html/`.

For more info on code coverage in python, see
https://coverage.readthedocs.io/en/latest/#quick-start

.. note::

    Code coverage can be easily integrated with travis and codecov using
    the `codecov` module.

.. note::

    More coming soon!
