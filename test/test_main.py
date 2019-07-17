"""
Test suite targeting the main calls.
"""
import pytest

from app.main import main


class TestMainOperations():

    def test_main_returns_properly( self ):
        ret = main()
        assert (ret)
