import matplotlib.pyplot as plt
from partitura_midi_import import partitura_midi_import
from durdist1 import durdist1

my_midi_file = "../music/midi/sarabande.mid"

print("------- input from partitura")
myscore = partitura_midi_import(my_midi_file, ptprint=False)
print("------- finished input from partitura")
myscore.show()

print("------- Calculate duration distribution")
dd = durdist1(myscore)

print(dd)

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