"""
This is an empty file for the template.
"""


def fibonacci( index: int ) -> int:
    """
    Computes the Fibonacci number for a given index.
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
    This is where the magic happens.
    """

    print( 'Computing the first 10 digits of the Fibonacci sequence:' )

    for index in range( 0, 10 ):
        template = 'fibonacci({index}) = {result}'
        print( template.format( index = index, result = fibonacci( index ) ) )


if __name__ == '__main__':
    main()
