"""
Test suite targeting the main calls and primary dependencies.
"""

import pytest

from app.main import main
from app.main import fibonacci


class TestMainOperations:

    @pytest.mark.dependency()
    def test_fibonacci_generator( self ):
        """
        The fibonacci generator should return the right fibonacci number
        for a specific index. Index must me a positive integer.
        """

        assert fibonacci( -99 ) is None
        assert fibonacci( 0 ) == 0
        assert fibonacci( 1 ) == 1
        assert fibonacci( 2 ) == 1
        assert fibonacci( 9 ) == 34

    @pytest.mark.dependency(
        depends = ['TestMainOperations::test_fibonacci_generator'] )
    def test_main_executes_properly( self ):
        """
        During normal execution, the main function returns nothing, but
        prints out a bunch of stuff. This test ensure that main runs without
        throwing in exception.
        """

        assert main() is None
