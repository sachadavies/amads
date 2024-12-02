musmart documentation
=====================


This package collects together a variety of algorithms for symbolic music analysis.
Here's an overview:

.. We add the :hidden: directive to each toctree so that the toctree is not displayed
.. in the main page itself, but only in the sidebar.

.. toctree::
   :maxdepth: 2
   :caption: User guide:
   :hidden:

   user_guide/installation.md

.. toctree::
   :maxdepth: 2
   :caption: Developer notes:
   :hidden:

   developer_notes/building_docs
   developer_notes/design.rst
   developer_notes/modules.rst
   developer_notes/music21.rst
   developer_notes/testing

Algorithms
----------

.. autosummary::
   :toctree: _autosummary
   :caption: Algorithms

   musmart.algorithm.entropy
   musmart.algorithm.pcdist1
   musmart.algorithm.pcdist2


Core
----

.. autosummary::
   :toctree: _autosummary 
   :caption: Core

   musmart.core.basics



IO
--

.. autosummary::
   :toctree: _autosummary
   :caption: IO

   musmart.io.pianoroll


Resources
---------

.. autosummary::
   :toctree: _autosummary
   :caption: Resources

   musmart.resources.key_profiles_literature
