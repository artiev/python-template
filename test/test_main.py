"""
Test suite targeting the main calls.
"""

from unittest import TestCase

from app.main import main


class TestMainOperations( TestCase ):
    def setUp( self ):
        pass

    def test_main_returns_properly( self ):
        ret = main()
        self.assertTrue( ret )

    def tearDown( self ):
        pass
