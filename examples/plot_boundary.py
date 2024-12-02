"""
Boundary detection
==================
"""

# %%
#
# This example demonstrates how to detect boundaries in a MIDI file using the
# boundary detection algorithm.

import matplotlib.pyplot as plt
from musmart.pt_midi_import import partitura_midi_import
from musmart.boundary import boundary
from musmart.pianoroll import pianoroll
from musmart import example

# Load example MIDI file
my_midi_file = example.fullpath("midi/tempo.mid")

# Import MIDI using partitura
myscore = partitura_midi_import(my_midi_file, ptprint=False)

# Create piano roll visualization
fig = pianoroll(myscore)

# Detect boundaries and get strength values
strength_list = boundary(myscore)
print(strength_list)

# TODO: consider a graph sharing the same time axis as
# our score plot so that the "soft" boundary strengths could be
# accentuated. How do we visualize strength?

plt.show()
