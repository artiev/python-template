"""
The main.py file is currently used for demonstration only within this project,
in order to offer a standard entry point to the whole template.

The structure of the app itself is not predefined, and different apps will
present different structures, hence the freedom.

In this example, the main file is supposed to be called directly from an
interpreter which will call the main() function.

.. code-block:: python

    if __name__ == '__main__':
        main()

"""


def fibonacci( index: int ) -> int:
    """
    Computes the Fibonacci number for a given index through recursion.
    """

    result = None

    if index == 0:
        result = 0
    elif index == 1:
        result = 1
    elif index > 1:
        result = fibonacci( index - 1 ) + fibonacci( index - 2 )

    return result


def main() -> None:
    """
    The main function within this example simply computes the first ten digits
    of the Fibonacci sequence.

    .. warning::
        Using a recursive function in this instance is a waste of resources,
        but this is just an example.

    The Fibonacci number have an interesting mathematical significance, and
    have many applications.

    .. note::
        See https://en.wikipedia.org/wiki/Fibonacci_number for more on
        the Fibonacci numbers.

    """

    print( 'Computing the first 10 digits of the Fibonacci sequence:' )

    for index in range( 0, 10 ):
        template = 'fibonacci({index}) = {result}'
        print( template.format( index = index, result = fibonacci( index ) ) )


if __name__ == '__main__':
    main()
