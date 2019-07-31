.. warning::

    Work in progress...

.. _section-travis-codecov-config:

Travis & Codecov configuration
==============================

As briefly discussed in the :ref:`section-coverage-in-general`
section, Travis is configured to
run the complete regression (all tests found in the `test/` folder) and
computed the coverage using the same tools as the local coverage computation.

The difference comes after the build on Travis is successful, and the
`codecov` module kicks in, uploading the coverage statistics to codecov.io.
This is achieved by a set of configuration files found at the root of the
project.

Linking Travis and Codecov
--------------------------

Computing code coverage locally is a nice tool, but most importantly, the
ability to follow the evolution of your coverage throughout the development
cycles of your application is a very effective metric to know how your
process is evolving, and whether or not your investment on testing in
increasing or decreasing.

This is achieved through a configuration file `.codecov.yml` located at the
root of the project directory:

.. literalinclude:: ../../../.codecov.yml
    :caption: .codecov.yml
    :language: yaml
    :emphasize-lines: 7,10,13

And a few special directives to the `.travis.yml`:

.. literalinclude:: ../../../.travis.yml
    :caption: .travis.yml
    :language: yaml
    :emphasize-lines: 13,19-20
