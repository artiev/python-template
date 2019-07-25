.. warning::

    Work in progress...

.. _section-unit-test:

Unit Tests
==========

The unit testing scheme of this template is designed to offer the user the
possibility to not only create unit tests within the `test/` folder, but also
the option to separate unit tests in what I will call `collections`.

The reasoning behind it is that not 100% of the project needs to be tested
during coding sessions, as opposed to continuous integration regressions, hence
the ability for any contributor to design their own test collections.

When computing code-coverage, the entry point of is always the complete
collection of tests located in the `test/` folder. Adding new tests to the
collection is as simple as creating a new file within that directory structure.

.. note::

    For more info on unittesting in python, see
    https://docs.python.org/3/library/unittest.html


Deep dive on the test results
-----------------------------

As mentioned previously, usual coverage of your tests should be around 100%,
which has a lot to do with approaches such as Test Driven Development - which is
a good thing - but in my opinion, passing tests is not the only tool in your
arsenal. In fact, a test can have quite a few different outcomes, which all have
various degrees of severity, but let's focus on these for now:

- passed
- failed
- skipped
- expected failed
- error

Now you're obviously familiar with the first two, but let's talk about the other
three, and why these can be very important.

Skipped
*******

There are a few reasons a test might or should be skipped, some at the tester's
discretion and some others due to the level of automation the project relies on.
To cite only a few:

- Using **parametrized regressions** can help to reduce test time to use the
  same test suite for different level of regressions, one common approach to
  this is skipping some tests.
- If a dependency fails during the current test sequence, and you have
  specified these dependencies within your tests, then for the sake of clarity,
  you should skip some tests automatically. More about this in the chapter on
  unit testing.
- Sometimes, introducing tests long before a modules is ready is the best way
  to define an API, but it can be hard to maintain a quality gate with these
  tests if not for purposefully skipping them until the modules are ready.


Expected Fails
**************

Sometimes, having all your tests passing is not the best way to prove a
library's proper behaviour. Let's take a few concrete examples:

- Writing tests is often a great source of **documentation** for the next
  developer. To that end, writing failing test can be an effective way of
  signaling how not to do something.
- Randomizing **test vectors** to maximize the impact of a single test - running
  one sequence of tests with an arrays of possible inputs - if a fantastic way
  to attack stress a module, but sometimes, not all input combinations is
  supposed to work, and for these combination, specifying an expected fail
  flag is mandatory.

Errors
******

As briefly mentioned while talking about coverage targets, your tools and
development environment is as susceptible to breakage as your application. This
is what differentiate an error from a fail: the error seem to happen within your
test framework / environment rather than while executing a specific test. Now -
granted - there is a fine line between and error and a fail, and sometimes one
can be mistakenly confused with the other, but the difference still exists.
