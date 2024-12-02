import matplotlib.pyplot as plt
from musmart.pt_midi_import import partitura_midi_import
from musmart.skyline import skyline
from musmart.pianoroll import pianoroll
from musmart import example

my_midi_file = example.fullpath("midi/chopin_prelude_7.mid")


print("------- input from partitura")
myscore = partitura_midi_import(my_midi_file, ptprint=False)
print("------- finished input from partitura")
myscore.show()

pianoroll(myscore)

print("------- Find skyline")
sl = skyline(myscore)

# print(sl)
sl.show()

pianoroll(sl)
plt.show() 



