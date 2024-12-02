import matplotlib.pyplot as plt
from musmart.pt_midi_import import partitura_midi_import
from musmart.pcdist1 import pcdist1
from musmart.plotdist import plotdist
from musmart import example

my_midi_file = example.fullpath("midi/sarabande.mid")

myscore = partitura_midi_import(my_midi_file)

pcd = pcdist1(myscore)
fig = plotdist(pcd)

plt.show()