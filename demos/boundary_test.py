import matplotlib.pyplot as plt
from musmart.pt_midi_import import partitura_midi_import
from musmart.boundary import boundary
from musmart.pianoroll import pianoroll
from musmart import example

my_midi_file = example.fullpath("midi/tempo.mid")


print("------- input from partitura")
myscore = partitura_midi_import(my_midi_file, ptprint=False)
print("------- finished input from partitura")

fig = pianoroll(myscore)

print("------- Executing boundary")
strength_list = boundary(myscore)
print(strength_list)
# I'm thinking of using a graph sharing the same time axis as
# our score plot so that the "soft" boundary strengths could be
# accentuated
# how do we visualize strength

plt.show()