Testing
=======

This project uses pytest for testing. To run the tests, follow these steps:

Prerequisites
------------

Make sure you have the development dependencies installed:

    pip install -e ".[dev]"

Running all tests
---------------

From the root directory of the project, run:

    pytest

Running specific tests
--------------------

To run tests in a specific file:

    pytest tests/test_pitch_list_transformations.py

To run a specific test function:

    pytest tests/test_pitch_list_transformations.py::test_function_name

Writing tests
-----------

Tests are located in the ``tests/`` directory. Each test file should start with ``test_`` and each test function should also start with ``test_``.

Example test:

    def test_my_function():
        result = my_function()
        assert result == expected_value 

Continuous Integration
--------------------

Tests are automatically run via GitHub Actions CI on pushes to main and pull requests. The CI runs tests against Python versions 3.9, 3.10, and 3.11 on Ubuntu.

You can view the CI configuration in `.github/workflows/tests.yml` and check test results in the "Actions" tab of the GitHub repository.
