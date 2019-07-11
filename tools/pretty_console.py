import click
import shutil

LEFT, CENTER, RIGHT = range( 3 )


@click.group()
def cli(): pass


@cli.command()
@click.argument( 'title' )
def print_title_hline( title: str ) -> None:
    """
    Print out a 80char long string with a bold horizontal line, embedding text
    on the right hand side.
    """

    print_text_in_hline(
        title.upper(),
        bold = True,
        justify = True,
        position = CENTER
    )


@cli.command()
@click.argument( 'subtitle' )
def print_subtitle_hline( subtitle: str ) -> None:
    """
    Print out a 80char long string with a horizontal line, embedding text
    in the center of the line.
    """

    print_text_in_hline(
        subtitle,
        justify = True,
        position = CENTER
    )


def print_text_in_hline( title: str,
                         bold = False,
                         position: int = LEFT,
                         terminal_length = 80,
                         justify = False ) -> None:
    """
    Multipurpose function printing horizontal line while embedding some text
    in the resulting string. The line can be bold, and the text can be placed
    in different positions (left, center, right).
    """

    line_char = '\u2501' if bold else '\u2500'
    actual_terminal_length, _ = shutil.get_terminal_size()
    terminal_length = terminal_length if not justify else actual_terminal_length
    line = line_char * terminal_length

    left_index, right_index = compute_title_placement_indices(
        position,
        len( title ),
        terminal_length )

    output = line[:left_index] + ' ' + title + ' ' + line[right_index:]
    print( output )


def compute_title_placement_indices( position: int,
                                     title_length: int,
                                     output_length: int ) -> (int, int):
    """
    Given a placement/position for the the text, this method computes the left
    and right indices at which the text must be inserted.
    """

    if position is LEFT:
        left_index = 1
    elif position is CENTER:
        left_index = int( (output_length - (title_length + 2)) / 2.0 )
    elif position is RIGHT:
        left_index = output_length - (title_length + 2 + 1)

    right_index = left_index + title_length + 2

    return left_index, right_index


if __name__ == '__main__':
    cli()
