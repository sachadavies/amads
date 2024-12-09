import matplotlib.pyplot as plt
import numpy as np
from amads.pt_midi_import import partitura_midi_import
from amads.durdist2 import durdist2
from amads import example

my_midi_file = example.fullpath("midi/sarabande.mid")

print("------- input from partitura")
myscore = partitura_midi_import(my_midi_file, ptprint=False)
print("------- finished input from partitura")
myscore.show()


print("------- Calculate 2nd order duration distribution")
dd = durdist2(myscore)

print(dd)

# Plot the 2nd order duration distribution as a heatmap
dd_array = np.array(dd)
plt.figure(figsize=(8, 6))
plt.imshow(dd_array, cmap='gray_r', interpolation='nearest')
plt.colorbar(label='Probability')
plt.xlabel('Duration (to)')
plt.ylabel('Duration (from)')
plt.title('2nd Order Duration Distribution')

bin_centers = [
    '1/4', 'sqrt(2)/4', '1/2', 'sqrt(2)/2', '1',
    'sqrt(2)', '2', '2*sqrt(2)', '4'
]
plt.xticks(range(len(bin_centers)), bin_centers)
plt.yticks(range(len(bin_centers)), bin_centers)

plt.gca().invert_yaxis()

plt.show()
