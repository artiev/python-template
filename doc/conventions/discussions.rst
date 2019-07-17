Code Conventions
================
Go `back <../README.rst>`_ to the table of content.

I - the template's author - follow most of the PEP8 recommendations. But 
there are some rules which I consider diminishing read-ability of the code, and 
which are hence not enforced in the linter's configuration (see `.pylintrc`).

In particular, the following conventions are disables by default:

- `bad-whitespace`_
- `len-as-condition`_
- `no-name-in-module`_

bad-whitespace
--------------
One reason for me to disable the **bad-whitespace** warnings is the way I write functions definitions and calls, and mathematical formulae. I'd simply call it 'adding negative space' - the absence of code - to enhance readability. The **bad-whitespace** would trigger multiple warnings in the following code.

.. code-block:: python

    def add_and_multiply( a: float, b: float, c: float = 1 ) -> float:
        """
        Adds a to b, then multiplies the result by c
        """

        result = (a + b) * c
        message = '( {} + {} ) * {} = {}'.format( a, b, c, result )
        print( message )

        return result

But I find this much more readable than the following, despite is having the exact same functionality.

.. code-block:: python

    def add_and_multiply(a: float, b: float, c: float = 1) -> float:
        """ Adds a to b, then multiplies the result by c """
        result = (a + b) * c
        message = '( {} + {} ) * {} = {}'.format(a, b, c, result)
        print(message)
        return result

Granted, the code snippets differs in more ways between than just the introduction of that rule, but I will still prefer :

- ``print( message )`` over ``print(message)``
- ``add_and_multiply( a: float, b: float, c: float = 1 )`` over ``add_and_multiply(a: float, b: float, c: float = 1)``

len-as-condition
----------------

In the same vain as the **bad-whitespace** discussion, there is a few simplifications made in python which I consider hindering readability and clarity. Let's take the following example:

.. code-block:: python

    some_list = [1, 4, 6, 2, 1]

    if list:
        print( 'list is not empty' )

This makes my skin crawl, what is ``if list`` supposed to mean ? Now let's see the explicit equivalent, which would trigger the linter:

.. code-block:: python

    some_list = [1, 4, 6, 2, 1]

    if len(list) > 0:
        print( 'list is not empty' )

Now, whether one way is faster or more pythonic is not what I care about. Instead, I'll take readability over performance or philosophy most of the time. Because let's be honest, for real performance, write your libraries in C and compile them.

If you'd like to be thorough, then, I do agree that ``if len(some_list): pass`` is neither explicit, nor pythonic, and therefore should be avoided. It's not logical to extract a boolean value by camparing it to an integer which is computed from a list, but by deactivating **len-as-condition** entirely, you open the door to such slips. I guess it's up to you to decide if you can be diligent enough.

no-name-in-module
-----------------

Ok, I guess this is going to be the most controversial point, but I'm tired of the ``__init__.py`` files cluttering my directories. So I only use them sparsely since Python 3.3, but the linter does no always react in the best of ways (yet?) and throws me a bunch of **no-name-in-module** warnings.

Regular modules increase the risk of side effects you can purposely - or not - introduce in libraries. Now, not letting Python know what module is a module only works if your import scheme are consistent with an certain approach:

- Use absolute imports for all your custom libraries
- Only allow importing an entire module for the standard libraries
- Import only the resources you need from your app/libraries

This seems arbitrary, but in practice, there are quite a few things happening (and NOT happening). Let's have a look:

:Dependencies:
    You always highlight specific dependencies:

    .. code-block:: python

        from app.client import CREDENTIALS_ERROR

    Instead of:

    .. code-block:: python

        import app

    It has the added benefit to avoid executing code you don't know about, which brings me to the next point.

:Execution:
    Side effects are the bane of any collaborative software developer's existence. Now when importing a module with ``import app``, Python will implicitly execute the ``__init__.py`` file and a bunch more things.

    .. code-block:: python

        # module/__init__.py
        # [...]
        LOGGER = logging.getLogger('my_logger')
        HANDLER = RotatingFileHandler('my_log.log', maxBytes=2000, backupCount=10)
        LOGGER.addHandler(handler)
        # [...]

        # some other file
        import module

        # and boom, you've accessed the filesystem to create a log file.
        # Ok, granted, the 'module' was crap in the first place ^^

    Now, for most people, this being an empty file, it does not really matter. But I have seen (and on occasion even used) ``__init__.py`` files to restrict the import scopes of a module by manually overwriting the ``__all__`` attribute, in other words, redefining a module's exposed functions and objects.

    .. code-block:: python

        # __init__.py

        from .submodule import public_function
        from .defines import PUBLIC_SET
        from .lib.oop import PublicObject

        __all__ = ['public_function', 'PUBLIC_SET', 'PublicObject']

    You guess where I'm going with this ? Well, I'm being supplied a library and was told to only use the 'public' interface, I'm looking into the code, and find the perfect function, so I import my module, and call 'module.function' somewhere down, and... and nothing, it fails because ``__all__`` did not expose that particular function.

    Don't get me wrong, it's a very nice way to differentiate 'public' and 'private' functions or objects for third parties, but it contradicts my approach to software development: code should only do what it's supposed to do. And in Python, everything is public, so don't break expectations.

:Clutter:
    Last but not least, I do my best to divide my project's codes in small and contained libraries. You know, to keep things clean and modular. So I have many folders and files, and I'm working in the  console, so I call ``tree``:

    .. code-block:: text

        .
        ├── __init__.py
        ├── lib
        │   ├── bells
        │   │   └── __init__.py
        │   ├── colors
        │   │   └── __init__.py
        │   ├── console
        │   │   └── __init__.py
        │   └── __init__.py
        └── module
            ├── client
            │   └── __init__.py
            ├── core
            │   ├── defines
            │   │   └── __init__.py
            │   └── __init__.py
            └── __init__.py

    Well, I can't describe that feeling. But that's where Python 3.3+ came handy, by introducing the concept of ``namespace`` to complement the ``regular`` package definition, and suffice to say, it suits my needs. And also offer a few interesting options for the future.

And that's why most of my projects only have a limited amount of ``__init__.py`` files, simply because most of the time I treat folders as namespaces rather than entire modules.

.. pull-quote::

    A namespace package is a composite of various portions, where each portion contributes a subpackage to the parent package. Portions may reside in different locations on the file system. Portions may also be found in zip files, on the network, or anywhere else that Python searches during import. Namespace packages may or may not correspond directly to objects on the file system; they may be virtual modules that have no concrete representation.

    Namespace packages do not use an ordinary list for their __path__ attribute. They instead use a custom iterable type which will automatically perform a new search for package portions on the next import attempt within that package if the path of their parent package (or sys.path for a top level package) changes.

    With namespace packages, there is no parent/__init__.py file. In fact, there may be multiple parent directories found during import search, where each one is provided by a different portion. Thus parent/one may not be physically located next to parent/two. In this case, Python will create a namespace package for the top-level parent package whenever it or one of its subpackages is imported.

See https://www.python.org/dev/peps/pep-0420/ for more details.
