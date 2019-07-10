# Tools

This projects uses `pylint` and `coverage` modules to ensure a decent level of 
code quality. Both module are configured through their rc files at the root of 
the project folder.

## Code Coverage

This template relies on the use of the `coverage` module in conjunction with
the `unittest` module to automatically compile code coverage report.

Underlined here is the importance of writing tests (prepared folder `test/`) 
which not only maximize coverage, but also prevent breaking applications
later during refactoring and maintenance stages of a project's lifecycle. 

> Code coverage alone is not a good indicator of project health.

The makefile offer the `test` and the `coverage` targets. The former collects 
and run unit tests while gathering coverage statistics, then prints out stats
in the console only. The second target calls `test` then generates an html 
report, located under `coverage/html/`.

For more info on code coverage in python, 
[read the doc](https://coverage.readthedocs.io/en/latest/#quick-start).

> Note: code coverage can be easily integrated with travis and codecov using 
the `codecov` module.

## Unit Testing

The unit testing scheme of this template is designed to offer the user the 
possibility to not only create unit tests within the `test/` folder, but also 
the option to separate unit tests in what I will call `collections`.

The reasoning behind it is that not 100% of the project needs to be tested 
during coding sessions, as opposed to continuous integration regressions, hence
the ability for any contributor to design their own test collections.

```
test
├── collection_full.py
├── test_main.py
└── test_tools.py
```

When computing code-coverage, the entry point of is always the 
`collection_full.py` file. Adding new tests to the collection is easily done
by importing new TestCase classes from any other files file.

```python3
from test.test_main import TestMainOperations
```

For more info on unittesting in python, 
[read the doc](https://docs.python.org/3/library/unittest.html).

## Linting

The linting process checks all *imported* code from a given starting point 
(entry file) for common PEP8 rules (not all, see `doc/conventions/`). In the 
current configuration, the linting process also applies grammar check to all 
comments on top of the normal code.

For more info on linting in python, 
[read the doc](https://pylint.readthedocs.io/en/latest/tutorial.html).