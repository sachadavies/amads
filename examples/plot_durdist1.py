"""
Plot the duration distribution of notes in a MIDI file.

This example demonstrates how to calculate and visualize the duration distribution
of notes in a MIDI file.
"""

from amads import example
from amads.pt_midi_import import partitura_midi_import
from amads.durdist1 import duration_distribution_1

# Load example MIDI file
my_midi_file = example.fullpath("midi/sarabande.mid")

# Import MIDI using partitura
myscore = partitura_midi_import(my_midi_file, ptprint=False)
# myscore.show()

# Calculate duration distribution
dd = duration_distribution_1(myscore)
plt, fig = dd.plot()

print("Duration distribution:", dd.data, dd.x_categories)
plt.show()

# %%
