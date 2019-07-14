Python Project Template
=======================

:Brief:
    Functional set of tools and templates for starting a python project.
:CI Status:
    .. image:: https://travis-ci.org/artiev/python-template.svg?branch=master
        :target: https://travis-ci.org/artiev/python-template
    .. image:: https://codecov.io/gh/artiev/python-template/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/artiev/python-template
:Contributors:
    Arthur Van de Wiele
:Project Home:
    https://github.com/artiev/python-template


This small project aims at offering a personal take on formalizing python 
project structures, together with good development practices. The main point
here is setting up the most important tools a developer needs, and ensure
they function out of the box so starting any new project can be done in a
breeze.

Template's features
-------------------

:Code Syntax Check:
    Code quality is enforced using ``pylint``
:Unit Testing:
    A ``test/`` folder is colelction unit tests, and ``pytest`` in
    conjunction with ``unittest`` libraries can be used to write tests.
:Code Coverage:
    Coverage of the unit tests is automatically compiled.
:Dev Documentation:
    Developper's documenation can be extracted from the source code using
    ``sphinx`` and rendered in html format.
:Continuous Integration:
    All configuration files for using ``Travis`` and ``Codecov`` is already
    provided, and relies on the aforementioned unit tests and coverage.
:Custom Tools & Scripts:
    Some extra tools are provided for ease of life.

More documentation
------------------

:Code Conventions:
    | Explanations about used code conventions.
    | See `doc/conventions/ <doc/conventions/>`_

:Tools:
    | More information about the tools provided by the template.
    | See `doc/tools/ <doc/tools/>`_
