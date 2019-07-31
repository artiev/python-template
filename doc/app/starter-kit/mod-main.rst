The main() function: an entry point
===================================

Most of the time, one function should be the entry point of your application. In
this instance, I use C as an inspiration for standardizing the use of the
:func:`main.main()` function. As python file names matter - in contrast to C -
the module holding the `main()` function is also called :mod:`main`.

.. graphviz::
    :align: center
    :caption: Entry points.


    digraph foo {
        rankdir = LR
        size = "8,5"
        overlap = False
        pad = 1

        "Project" -> "App"
        "App" -> "main()" [label = "execute"]
        "Project" -> "Tests"
        "Tests" -> "test/ folder" [label = "extend"]
        "Project" -> "Doc"
        "Doc" -> "doc/project/ folder" [label = "extend"]
    }

If you are calling the python interpreter directly on a file, then you'll need
to add a safeguard:

.. code-block:: python

    if __name__ == '__main__':
        main()

Otherwise, the function is usually given as a gateway, for example if using
gunicorn to start a server and deliver a flask application:

.. code-block:: shell

    $ gunicorn app.main:main

.. warning::

    The entire project is built using Python 3.7+, and in such an example,
    gunicorn or any other server needs to be carefully setup to use Python 3
    as - at the time of this writing - most operating systems and platforms
    still operate with Python 2.7 as a default.
