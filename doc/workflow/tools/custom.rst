This template is built upon as many standardized libraries and modules in order
to provide stability and state-of-the-art features relying on the great work of
other projects.

Unfortunately, sometimes a subset of features might be missing, or is not
user friendly enough, and investing some time into building the right tool
for the job is worth it. This is the case for the following scripts/tools,
which are not standard.

Python Project Cleaner
======================

Introduction
------------

As the name suggests, this collection of function and scripts helps you keep a
clean project tree. For me, this allows me to work in the console better, by
letting me clean all python cache files and folders in a single command, hence
keeping the directory tree pristine.

For example, see the file tree below. I could configure my system so that
folders starting with `__` would be hidden, but it makes no sense.

.. code-block::

    $ tree t*
    ├── test
    │   ├── pytest.ini
    │   ├── test_app
    │   │   ├── __pycache__
    │   │   │   └── test_main.cpython-37-pytest-5.0.1.pyc
    │   │   └── test_main.py
    │   ├── test_methodology
    │   │   ├── __pycache__
    │   │   │   └── test_examples.cpython-37-pytest-5.0.1.pyc
    │   │   └── test_examples.py
    │   └── test_tools
    │       ├── __pycache__
    │       │   ├── test_path_explorer.cpython-37-pytest-5.0.1.pyc
    │       │   └── test_pretty_console.cpython-37-pytest-5.0.1.pyc
    │       ├── test_path_explorer.py
    │       └── test_pretty_console.py
    └── tools
        ├── path_cleaner.py
        ├── path_explorer.py
        ├── pretty_console.py
        ├── __pycache__
        │   ├── path_explorer.cpython-37.pyc
        │   └── pretty_console.cpython-37.pyc
        └── pycharm_code_style.xml

That's where the cleaning routine helps. It navigates through the entire
project structure, and locates all the cache files and folders, then deletes
them all. So that navigating the project looks more like:

.. code-block::

    $ tree t*
    ├── test
    │   ├── pytest.ini
    │   ├── test_app
    │   │   └── test_main.py
    │   ├── test_methodology
    │   │   └── test_examples.py
    │   └── test_tools
    │       ├── test_path_explorer.py
    │       └── test_pretty_console.py
    └── tools
        ├── path_cleaner.py
        ├── path_explorer.py
        ├── pretty_console.py
        ├── __pycache__
        │   └── pretty_console.cpython-37.pyc
        └── pycharm_code_style.xml

.. note::

    As you might have noticed, currently executing pre-compiled files are not
    deleted, like it is the case for `pretty_console.cpython-37.pyc` being used
    by the makefile during the cleaning process.

How to clean the project tree
-----------------------------

Generally speaking, most of the template's tools are exposed through the
makefile. In this instance, simply run:

.. code-block::

    $ make clean

Now, this does a few things on top of cleaning up the cache, so you can always
call the script separately. The cleaner tool uses the `click` library to expose
a command line interface. For example, as called by the makefile's `clean`
target:


.. code-block::

    $ 	python -m tools.path_cleaner clear-all-cache <START_DIR>

You can always get an up-to-date feature description from calling:

.. code-block::

    $ python -m tools.path_cleaner --help
    Usage: path_cleaner.py [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      clear-all-cache               Entry point for cleaning files and then...
      clear-cache-files             Walk through the given path, looking for...
      clear-cache-folders-if-empty  Walk through the given path, looking for...

.. note::

    More about the `click` library at https://click.palletsprojects.com/en/

Developer's documentation
-------------------------

.. automodule:: path_cleaner
    :members:

.. autofunction:: path_cleaner.clear_all_cache
.. autofunction:: path_cleaner.clear_cache_files
.. autofunction:: path_cleaner.clear_cache_folders_if_empty

.. automodule:: path_explorer
    :members:
