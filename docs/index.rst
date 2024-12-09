amads documentation
=====================

This package collects together a variety of algorithms for symbolic music analysis.

**The package is its very early stages. The API is subject to change, and many algorithms are not yet implemented, tested, or documented!**

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
   developer_notes/style

.. toctree::
   :maxdepth: 2
   :caption: Examples:
   :hidden:

   auto_examples/index



General algorithms
------------------

.. autosummary::
   :toctree: _autosummary
   :caption: General algorithms:

   amads.algorithm.boundary
   amads.algorithm.break_it_up
   amads.algorithm.durdist1
   amads.algorithm.durdist2
   amads.algorithm.entropy
   amads.algorithm.hz2midi
   amads.algorithm.ismonophonic
   amads.algorithm.ivdirdist1
   amads.algorithm.ivdist1
   amads.algorithm.ivdist2
   amads.algorithm.ivsizedist1
   amads.algorithm.nnotes
   amads.algorithm.pcdist1
   amads.algorithm.pcdist2
   amads.algorithm.pitch_mean
   amads.algorithm.scale
   amads.algorithm.segment_gestalt
   amads.algorithm.skyline

Harmony
-------

.. autosummary::
   :toctree: _autosummary
   :caption: Harmony:

   amads.harmony.root_finding.parncutt_1988

Pitch
-----

.. autosummary::
   :toctree: _autosummary
   :caption: Pitch:

   amads.pitch.transformations

Resources
---------

.. autosummary::
   :toctree: _autosummary
   :caption: Resources:

   amads.resources.key_profiles_literature

Core
----

.. autosummary::
   :toctree: _autosummary
   :caption: Core:

   amads.core.basics

IO
--

.. autosummary::
   :toctree: _autosummary
   :caption: IO:

   amads.io.pianoroll