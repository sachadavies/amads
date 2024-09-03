# pcdist2_test.py - simple test of pcdist2()

import matplotlib.pyplot as plt
import numpy as np
from musmart import example
from musmart.pt_midi_import import partitura_midi_import
from musmart.pcdist2 import pcdist2

# "midi/tones.mid"
my_midi_file = example.fullpath("midi/twochan.mid")
# "midi/tempo.mid"

print("------- input from partitura")
myscore = partitura_midi_import(my_midi_file, ptprint=False)
print("------- finished input from partitura")

# myscore = myscore.flatten()

print("------- Calculate pitch-class distribution")
pcd = pcdist2(myscore, weighted=False)

print(pcd)

# Plot the pitch-class distribution as a heatmap
pcd_array = np.array(pcd)
plt.figure(figsize=(8, 6))
plt.imshow(pcd_array, cmap='hot', interpolation='nearest')
plt.colorbar(label='Probability')
plt.xlabel('Pitch Class (to)')
plt.ylabel('Pitch Class (from)')
plt.title('2nd Order Pitch-Class Distribution')

pitch_classes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#',
                 'B']
plt.xticks(range(12), pitch_classes)
plt.yticks(range(12), pitch_classes)

plt.show()
