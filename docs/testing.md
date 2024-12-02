Running tests
============

This project uses pytest for testing, including doctests. To run the tests, follow these steps:

Prerequisites
------------

Make sure you have the development dependencies installed::

    pip install -e ".[dev]"

Running all tests
---------------

From the root directory of the project, run::

    pytest

This will run both regular tests and doctests.

Running specific tests
--------------------

To run tests in a specific file:

    pytest tests/test_pitch_list_transformations.py

To run a specific test function::

    pytest tests/test_pitch_list_transformations.py::test_function_name

Writing tests
-----------

There are two main ways to write tests in this project:

1. Regular pytest tests

----------------------

Tests are located in the ``tests/`` directory. Each test file should start with ``test_`` and each test function should also start with ``test_``.

Example test::

    def test_my_function():
        result = my_function()
        assert result == expected_value

2. Doctests
----------

You can write tests directly in the docstring of a function using doctests. These are particularly useful for showing example usage. The doctest should show both the input and expected output using Python's interactive prompt syntax (>>>).

Example doctest::

    def my_function(x):
        """Calculate something.
        
        Parameters
        ----------
        x : float
            Input value
            
        Returns
        -------
        float
            Calculated result
            
        Examples
        --------
        >>> round(my_function(0.5), 6)
        1.0
        """
        # function implementation...

The doctest above shows:

1. The exact input to test (`my_function(0.5)`)
2. Any necessary formatting (`round(..., 6)` for floating point precision)
3. The expected output (`1.0`)

Running doctests specifically::

    pytest --doctest-modules
