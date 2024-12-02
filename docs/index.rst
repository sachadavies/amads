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

   user_guide/installation

.. toctree::
   :maxdepth: 2
   :caption: Developer notes:
   :hidden:

   developer_notes/building_docs
   developer_notes/design
   developer_notes/modules
   developer_notes/music21
   developer_notes/testing

.. toctree::
   :maxdepth: 2
   :caption: Examples:
   :hidden:

   auto_examples/index

Algorithms
----------

.. autosummary::
   :toctree: _autosummary
   :caption: Algorithms API:

   musmart.algorithm.entropy
   musmart.algorithm.pcdist1
   musmart.algorithm.pcdist2


Core
----

.. autosummary::
   :toctree: _autosummary 
   :caption: Core API:

   musmart.core.basics


IO
--

.. autosummary::
   :toctree: _autosummary
   :caption: IO API:

   musmart.io.pianoroll


Resources
---------

.. autosummary::
   :toctree: _autosummary
   :caption: Resources API:

   musmart.resources.key_profiles_literature
