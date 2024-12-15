import matplotlib.pyplot as plt

from amads.all import partitura_midi_import, pianoroll, segment_gestalt
from amads.music import example

my_midi_file = example.fullpath("midi/sarabande.mid")


print("------- input from partitura")
myscore = partitura_midi_import(my_midi_file, ptprint=False)
print("------- finished input from partitura")

fig = pianoroll(myscore)

print("------- Executing segmentgestalt")
clang_qstarts, segment_qstarts = segment_gestalt(myscore)
print(clang_qstarts)
print(segment_qstarts)
xmin, xmax, ymin, ymax = plt.axis()

plt.vlines(clang_qstarts, ymin, ymax, colors="purple", label="clang boundary qstarts")
plt.vlines(
    segment_qstarts, ymin, ymax, colors="green", label="segment boundary qstarts"
)
plt.legend(loc="best")

plt.show()
