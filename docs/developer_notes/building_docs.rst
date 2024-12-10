Building documentation
======================

This guide explains how to build and maintain the project's documentation using Sphinx.

Prerequisites
-------------

Before building the documentation, ensure you have the dev dependencies installed:

.. code-block:: bash

    pip install -e ".[dev]"

Building documentation
----------------------

The documentation can be built in two ways:

1. One-time build
~~~~~~~~~~~~~~~~~

To build the documentation once, navigate to the ``docs`` directory and run:

.. code-block:: bash

    # On Unix/macOS
    make html

    # On Windows
    make.bat html

The built documentation will be available in ``docs/_build/html/index.html``.

2. Auto-building (development)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For development, you can use ``sphinx-autobuild`` which automatically rebuilds the
documentation when changes are detected.

The first time you run this, you will need to install the ``sphinx-autobuild`` package:

.. code-block:: bash

    pip install sphinx-autobuild

Then run the following command to start the auto-building server:

.. code-block:: bash

    sphinx-autobuild docs docs/_build/html --open-browser

Writing documentation
---------------------

Documentation files are written in reStructuredText (RST) format. Here are some key points:

- Use ``.rst`` extension for documentation files
- Follow the numpydoc style for docstrings
- Include code examples using ``.. code-block:: python`` blocks
- Cross-reference other pages using ``:ref:`` roles
- Add new pages to the appropriate toctree in ``index.rst``

For example:

.. code-block:: rst

    .. code-block:: python

        def example_function():
            """
            This is a docstring example.

            Parameters
            ----------
            None

            Returns
            -------
            None
            """
            pass

You can also write markdown files, which will be rendered using the ``myst_parser`` extension.

Adding new documentation files
------------------------------

To add a new documentation file:

1. Create a new ``.rst`` file in the appropriate directory:

   .. code-block:: bash

       touch docs/user_guide/new_feature.rst

2. Add content to your RST file using reStructuredText syntax:

   .. code-block:: rst

       New feature guide
       =================

       This is a guide for the new feature.

       Section title
       -------------

       Content goes here.

3. Add the file to the toctree in ``index.rst`` or another parent document:

   .. code-block:: rst

       .. toctree::
          :maxdepth: 2
          :caption: Contents:

          user_guide/existing_page
          user_guide/new_feature   # Add your new file here

The file will now appear in the documentation navigation. Make sure to:

- Use descriptive filenames that reflect the content
- Place files in appropriate subdirectories (user_guide, developer_notes, etc.)
- Keep the toctree organized and logical
- Build and check that the new page appears correctly


Troubleshooting
---------------

Common issues and solutions:

1. **Missing modules**: If you see warnings about missing modules, ensure all development
   dependencies are installed:

   .. code-block:: bash

       pip install -e .[docs]

2. **Build errors**: Clear the build directory and rebuild:

   .. code-block:: bash

       rm -rf docs/_build/*  # Unix/macOS
       # or
       rmdir /s /q docs\_build  # Windows
       make html
