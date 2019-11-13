Flow diagrams
=============

Taking the habit of documenting your application's flow control with proper
diagrams will allow new-comers to your code find their way through the code
base much faster.  Let's take an extremely simplified flow diagram of the
template's main app, which loops over an index `n` and compute the fibonacci
value for that index.

.. graphviz:: assets/diagram-main-function.gv
    :align: center
    :caption: Example of a state machine



This graph is built automatically during the documentation generation using
an external dependency called `graphviz`. The graph image is generated based
on a graph description which defined in a separated text file.

The beauty of it, is that you can maintain the graphs as easily as you maintain
your code, without the need for any external tools. And the same holds true for
automatically generated documentation (see :ref:`section-sphinx-doc`)

.. literalinclude:: assets/diagram-main-function.gv
    :language: text
