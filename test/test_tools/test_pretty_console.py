import pytest
from random import choice
from shutil import get_terminal_size
from click.testing import CliRunner

from tools.pretty_console import build_text_in_hline
from tools.pretty_console import print_subtitle_hline, print_title_hline
from tools.pretty_console import LEFT, CENTER, RIGHT

POSITION_TEST_DATA = (LEFT, CENTER, RIGHT)
STRING_TEST_DATA = [
    'short title',
    'a somewhat long-ish title',
    'now this really is a title that noone wants embedded in a string',
]


class TestPrettyConsole():
    test_vector = [(string, pos)
                   for string in STRING_TEST_DATA
                   for pos in POSITION_TEST_DATA]

    def test_command_hline_interface( self ):
        """
        The pretty_console lib is dedicated to printing nicer console messages.
        This test ensures the two critical hline functions are exposed properly
        """

        string = 'a somewhat long-ish title'

        runner = CliRunner()

        term_len, _ = get_terminal_size()
        line_char_std = '\u2500'
        line_char_bold = '\u2501'

        result = runner.invoke( print_title_hline, [string] )
        assert (result.exit_code == 0)
        assert (len( result.output ) == term_len + 1)  # \n
        assert (line_char_bold in result.output)

        result = runner.invoke( print_subtitle_hline, [string] )
        assert (result.exit_code == 0)
        assert (len( result.output ) == term_len + 1)  # \n
        assert (line_char_std in result.output)

    @pytest.mark.parametrize( 'string, position', test_vector )
    def test_various_hline_generations( self, string, position ):
        """
        This test verifies the logic behind integrating text in the hline
        using multiple standard configuration vectors.
        """

        is_bold = choice( (True, False) )
        is_using_terminal_width = choice( (True, False) )

        hline = build_text_in_hline(
            string,
            position = position,
            bold = is_bold,
            justify = is_using_terminal_width
        )

        term_len, _ = get_terminal_size()
        line_len = 80 if not is_using_terminal_width else term_len
        line_char = '\u2501' if is_bold else '\u2500'

        assert (string in hline)
        assert (line_char in hline)
        assert (len( hline ) == line_len)

    @pytest.mark.xfail( reason = 'Not intended to be used that way.' )
    def test_hline_generation_with_wrong_arguments( self ):
        """
        The HLine methods are not designed to handle wrong arguments gracefully,
        instead, they will raise errors.
        """

        hline = build_text_in_hline(
            'some text',
            position = 99,  # 0,1,2 are LEFT, CENTER, RIGHT
            bold = True,
            justify = False
        )

        assert isinstance( hline, str )
