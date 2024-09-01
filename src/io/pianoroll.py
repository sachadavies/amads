"""
Ports `pianoroll` Function

Original Doc: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6e06906ca1ba0bf0ac8f2cb1a929f3be95eeadfa#page=82
"""

from basics import Score, Note
import matplotlib.figure as figure, matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def midi_num_to_name(midi_num: int, accidental) -> str:
    """
    Converts midi numbers to note names

    Helper function for pianoroll

    Args:
        midi_num (int): The midi number to be converted
        accidental (str): If the note has an accidental, 
                    determines if it is a sharp or a flat.
                        Defaults to 'sharp', raises exception for
                        inputs that's not either 'sharp' or 'flat'
        
    """

    octave = str(int((midi_num / 12) - 1))
    
    match accidental:
        case 'sharp':
            base = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'][midi_num % 12]
        case 'flat':
            base = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'][midi_num % 12]

    return base + octave


def pianoroll(score: Score, y_label='name', x_label='beat',
              color='skyblue', accidental='sharp') -> figure.Figure:
    """
    Returns a matplotlib.figure.Figure which displays a piano roll of a musical score.

    Args:
        score (Score): The musical score to display
        y_label (str, optional): Determines whether the y-axis is 
                                 labeled with note names or MIDI numbers
                                    Raises exception on inputs that's not
                                    'name' or 'num'.
        x_label (str, optional): Determines whether the x-axis is labeled 
                                 with beats or seconds.
                                    Raises exception on inputs that's not
                                    'beat' or 'sec'.
        accidental (str, optional): Determines whether the y-axis is labeled 
                                    with sharps or flats. Only useful if argument
                                    y_label is 'name'
                                        Raises exception on inputs that's not
                                        'sharp' or 'flat'.
    """

    # Stores properties of all notes in numpy array
    note_list = score.find_all(Note)
    note_info = np.array([[note.qstart(), note.dur, note.pitch.keynum] for note in note_list])

    midi_numbers = list(range(int(np.min(note_info[:, 2]) - 1), int(np.max(note_info[:, 2]) + 1)))
    
    match y_label:
        case 'num':
            notes = midi_numbers
        case 'name':
            notes = [midi_num_to_name(mn, accidental) for mn in midi_numbers]
        case _:
            Exception(
                "Invalid y_label type"
            )

    if x_label == 'sec':
        vectorized_beat_to_time = np.vectorize(score.timemap.beat_to_time)
        
        note_info[:, 0] = vectorized_beat_to_time(note_info[:, 0])
        note_info[:, 1] = vectorized_beat_to_time(note_info[:, 1])
    elif x_label != 'beat':
        Exception(
            "Invalid x_label type"
        )

    fig, ax = plt.subplots()

    for i, (start_time, duration, note) in enumerate(zip(note_info[:, 0], note_info[:, 1], note_info[:, 2])):
        rect = patches.Rectangle((start_time, note - 0.5), duration, 1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    ax.set_yticks(midi_numbers)
    ax.set_yticklabels(notes)

    ax.set_xlim(0, max(note_info[:, 0]) + max(note_info[:, 1]))
    ax.set_ylim(min(midi_numbers), max(midi_numbers) + 1)
    ax.grid(True)
    
    return fig