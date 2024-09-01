from matplotlib import pyplot as plt
from partitura_midi_import import partitura_midi_import
from pianoroll import pianoroll

my_midi_file = "../music/midi/sarabande.mid"
myscore = partitura_midi_import(my_midi_file, ptprint=False)

pr_fig = pianoroll(myscore)
plt.show() 