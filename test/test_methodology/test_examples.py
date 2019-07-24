"""
So, there is a few things you should consider when using this template, and
testing is one of them. Find below some quick example of how you can build a
smarter test suit. This examples are more about the process than about the
tests themselves, because I'm sure you can write a test already.

.. warning::
    It's crucial in test dependencies that ht e dependency be placed
    BEFORE the dependent. Otherwise, the dependent will always be skipped.
    See https://github.com/RKrahl/pytest-dependency/issues/20
"""

from time import sleep

import pytest


class TestGeneralEnvironment:

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

    @pytest.mark.dependency(
        depends = ['TestGeneralEnvironment::test_crucial_dependency'] )
    def test_only_if_dependency_is_ok( self ):
        """
        As expected, this test is going to be skipped, because I purposefully
        failed the dependency test.
        """

        pass

    def test_a_very_slow_process( self ):
        """
        This shows an example of reporting tests with highlighting some slow
        tests.
        """

        sleep( .1 )
