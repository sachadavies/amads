# partitura_midi_test.py - some tests for partitura_midi_import.py

from partitura_midi_import import partitura_midi_import
from pitch_mean import pitch_mean

# my_midi_file = "../music/midi/tones.mid"
my_midi_file = "../music/midi/twochan.mid"
# my_midi_file = "../music/midi/tempo.mid"

print("------- input from partitura")
myscore = partitura_midi_import(my_midi_file, ptprint=True)
myscore.show()


print("------- result of score copy")
scorecopy = myscore.deep_copy()
scorecopy.show()


print("------- result from strip_chords")
nochords = scorecopy.strip_chords()
nochords.show()

print("------- result from strip_ties")
noties = scorecopy.strip_ties()
noties.show()

print("------- result from flatten")
flatscore = scorecopy.flatten()
flatscore.show()

print("------- result from keynum_list")
print(myscore.collapse_parts().content[0].content)

print("------- result from keynum_list(part=(0))")
print(myscore.collapse_parts(part=[0]).content[0].content)

print("------- result from pitch_mean(myscore)")
print(pitch_mean(myscore))

print("------- result from pitch_mean(myscore, weighted=True)")
print(pitch_mean(myscore, weighted=True))

