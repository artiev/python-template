Example of a flow diagram of the placefholder app
=================================================

Let's take an extremely simplified flow diagram of the template's main app,
which loops over an index `n` and compute the fibonacci value for that index.

.. graphviz:: assets/diagram-main-function.gv
    :align: center
    :caption: Example of a state machine



This graph is built automatically during the documentation generation using
an external dependency called `graphviz`. The graph image is generated based
on a graph description which defined in a separated text file.

.. literalinclude:: assets/diagram-main-function.gv
    :language: text
