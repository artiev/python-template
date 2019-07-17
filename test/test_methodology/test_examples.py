"""
So, there is a few things you should consider when using this template, and
testing is one of them. Find below some quick example of how you can build a
smarter test suit. This examples are more about the process than about the
tests themselves, because I'm sure you can write a test already.
"""

from time import sleep

import pytest


class TestGeneralEnvironemnt():

    @pytest.mark.xfail( reason = 'Negative testing is always an option.' )
    def test_purposefully_failing( self ):
        """
        Believe it or not, expected fails are important, so this python project
        can handle XFAIL status.
        """

        assert False

    @pytest.mark.xfail( reason = 'Illustrates missing dependency.' )
    @pytest.mark.dependency()
    def test_crucial_dependency( self ):
        """
        Unfortunately, something went wrong with a dependency after I wrote and
        passed all my tests, so there is no reason to execute a bunch of failing
        tests that depend on this, instead, I have a 'guard' test, which if
        failed will force all dependent tests to be skipped.
        """

        assert False

    @pytest.mark.dependency( depends = ('test_crucial_dependency') )
    def test_only_if_dependency_is_ok( self ):
        """
        As expected, this test is going to be skipped, bacause I purposefully
        failed the dependency test.
        """

        assert False  # is not going to fail, just be skipped.

    def test_a_very_slow_process( self ):
        """
        This shows an example of reporting tests with highlighting some slow
        tests.
        """

        sleep( .1 )
