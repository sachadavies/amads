# partitura_midi_test.py - some tests for partitura_midi_import.py

from partitura_midi_import import partitura_midi_import

from scale import scale

# my_midi_file = "../music/midi/tones.mid"
my_midi_file = "../music/midi/twochan.mid"
# my_midi_file = "../music/midi/tempo.mid"

print("------- input from partitura")
myscore = partitura_midi_import(my_midi_file, ptprint=False)
print("------- finished input from partitura")

print("------- scaling dur by 2")
scaled_score = scale(myscore.deep_copy(),2,'dur')

print("------- scaled score")
scaled_score.show()

print("------- scaling offset by 2")
scaled_score = scale(myscore.deep_copy(),2,'offset')

print("------- scaled score")
scaled_score.show()

print("------- scaling everything (dur and offset) by 2")
scaled_score = scale(myscore.deep_copy(),2,'all')

print("------- scaled score")
scaled_score.show()

