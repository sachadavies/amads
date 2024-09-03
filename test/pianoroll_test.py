from matplotlib import pyplot as plt
from partitura_midi_import import partitura_midi_import
from musmart.pianoroll import pianoroll
from musmart import example

my_midi_file = example.fullpath("midi/sarabande.mid")
myscore = partitura_midi_import(my_midi_file, ptprint=False)

pr_fig = pianoroll(myscore)
plt.show() 
