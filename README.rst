Python Project Template
=======================

This project documentation is automatically built using Sphinx, and published
on https://readthedocs.io, see links below.

:CI Status:
    .. image:: https://travis-ci.org/artiev/python-template.svg?branch=master
        :target: https://travis-ci.org/artiev/python-template
        :alt: Continuous Integration Status
    .. image:: https://codecov.io/gh/artiev/python-template/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/artiev/python-template
        :alt: Code Coverage Status
    .. image:: https://readthedocs.org/projects/py-template/badge/?version=latest
        :target: https://py-template.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
:Contributors:
    Arthur Van de Wiele
:Project Links:
    | **Home**: https://github.com/artiev/python-template
    | **Doc**: https://py-template.readthedocs.io


Template's features
-------------------

This template offers a concise but extensive set of tools to ease your
development cycles and let you focus on what matters.

:Code Syntax Check:
    Code quality is enforced using ``pylint``
:Unit Testing:
    A ``test/`` folder collects unit tests, and ``pytest`` in
    conjunction with ``unittest`` libraries can be used to write and
    execute these tests.
:Code Coverage:
    Coverage based on the unit tests is automatically compiled, and linked to
    http://codecov.io
:Dev Documentation:
    Developer's documentation can be extracted from the source code using
    ``sphinx`` and rendered in html format, and is integrated with
    https://readthedocs.io for automated doc builds.
:Continuous Integration:
    All configuration files for using ``Travis`` and ``Codecov`` is already
    provided, and relies on the aforementioned unit tests and coverage.
:Custom Tools & Scripts:
    Some extra tools are provided for ease of life.
