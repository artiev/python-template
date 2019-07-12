from unittest import TestCase
from random import choice
from shutil import get_terminal_size
from click.testing import CliRunner

from tools.pretty_console import build_text_in_hline
from tools.pretty_console import print_subtitle_hline, print_title_hline
from tools.pretty_console import LEFT, CENTER, RIGHT


class TestPrettyConsole( TestCase ):

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
        self.assertEqual( result.exit_code, 0 )
        self.assertEqual( len( result.output ), term_len + 1 )  # \n
        self.assertTrue( line_char_bold in result.output )

        result = runner.invoke( print_subtitle_hline, [string] )
        self.assertEqual( result.exit_code, 0 )
        self.assertEqual( len( result.output ), term_len + 1 )  # \n
        self.assertTrue( line_char_std in result.output )

    def test_various_hline_generations( self ):
        """
        This test verifies the logic behind integrating text in the hline
        using multiple standard configuration vectors.
        """

        position_vector = (LEFT, CENTER, RIGHT)
        string_vector = [
            'short title',
            'a somewhat long-ish title',
            'now this really is a title that noone wants embedded in a string',
        ]

        for string in string_vector:
            for position in position_vector:
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

                self.assertTrue( string in hline )
                self.assertTrue( line_char in hline )
                self.assertEqual( len( hline ), line_len )
