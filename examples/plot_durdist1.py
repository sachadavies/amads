"""
Duration distribution
===================
"""

# %%
#
# This example demonstrates how to calculate and visualize the duration distribution
# of notes in a MIDI file.

import matplotlib.pyplot as plt
from musmart import example
from musmart.pt_midi_import import partitura_midi_import
from musmart.durdist1 import durdist1

# Load example MIDI file
my_midi_file = example.fullpath("midi/sarabande.mid")

# Import MIDI using partitura
myscore = partitura_midi_import(my_midi_file, ptprint=False)
# myscore.show()

# Calculate duration distribution
dd = durdist1(myscore)

# Plot the duration distribution
bin_centers = [
    '1/4', 'sqrt(2)/4', '1/2', 'sqrt(2)/2', '1',
    'sqrt(2)', '2', '2*sqrt(2)', '4'
]
plt.bar(bin_centers, dd, color='skyblue')
plt.xlabel('Duration (in beats)')
plt.ylabel('Probability')
plt.title('Duration Distribution')
plt.show()

# %%
