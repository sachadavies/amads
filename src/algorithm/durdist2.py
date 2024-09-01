"""
Provides the `durdist2` function

Original doc: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6e06906ca1ba0bf0ac8f2cb1a929f3be95eeadfa#page=59
"""

from basics import Score, Note, Staff
from ismonophonic import ismonophonic
import math


def update_dd(dd: list[list[float]], notes: list[Note]):
    """Updates the duration distribution matrix based on the given notes.
    
    Serves as a helper function for `durdist2`

    Args:
        dd (list[list[float]]): The duration distribution matrix to be updated.
        notes (list[Note]): The list of notes to process.
    """
    prev = None
    for note in notes:
        if prev:
            # The following algorithm comes from the original MATLAB
            # implementation https://github.com/miditoolbox/1.1/blob/
            #     master/miditoolbox/durdist2.m
            bin_curr = round(2 * math.log2(note.dur)) + 4
            bin_prev = round(2 * math.log2(prev.dur)) + 4
            if bin_curr <= 8 and bin_prev <= 8:
                dd[bin_prev][bin_curr] += 1 
        prev = note


def durdist2(score: Score) -> list[list[float]]:
    """
    Returns the 2nd order duration distribution of a musical score.
    
    Each duration is assigned to one of 9 bins. 
    The centers of the bins are on a logarithmic scale as follows:
        component    bin center (in units of quarters)
        0            1/4
        1            sqrt(2)/4
        2            1/2
        3            sqrt(2)/2
        4            1
        5            sqrt(2)
        6            2
        7            2*sqrt(2)
        8            4

    Args:
        score (Score): The musical score to analyze.

    Returns:
        list[list[float]]: 9x9 matrix of the distribution of note durations.
        
    Raises:
        Exception: If the score is not monophonic (e.g. contains chords)
    """
    if not ismonophonic(score):
        raise Exception("Error: Score must be monophonic")
    
    dd = [[0] * 9 for _ in range(9)]
    
    # TODO: I believe if score has tied notes, they will be treated
    # separately rather than joined to form a single duration. I do
    # not think we need two cases here since score.find_all() will
    # find all notes either way. -RBD
    if score.is_flattened():
        notes = score.find_all(Note)
        update_dd(dd, notes)
    else:
        for staff in score.find_all(Staff):
            notes = staff.find_all(Note)
            update_dd(dd, notes)
    
    # normalize
    total = sum([sum(row) for row in dd])
    if total > 0:
        dd = [[i/total for i in row] for row in dd]
    
    return dd
    
    
