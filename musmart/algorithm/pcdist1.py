"""
This module provides the `pcdist1` function.

Original doc: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6e06906ca1ba0bf0ac8f2cb1a929f3be95eeadfa#page=80.
"""

from musmart.core.basics import Score, Note


def pcdist1(score: Score, weighted=True):
    """
    Returns the pitch-class distribution of a musical score.

    Args:
        score (Score): The musical score to analyze
        weighted (bool, optional): If True, the pitch-class distribution is 
                                   weighted by note durations (default True)

    Returns:
        list[float]: A 12-element list representing the normalized 
              probabilities of each pitch class 
              (C, C#, D, D#, E, F, F#, G, G#, A, A#, B). 
              If the score is empty, the function returns a list with all 
              elements set to zero.
    """
    pcd = [0] * 12
    
    for container in score.note_containers():
        container.show()
        for note in container.find_all(Note):
            pc = note.pitch.pitch_class
            if weighted:
                pcd[pc] += note.dur
            else:
                pcd[pc] += 1
    total = sum(pcd)
    if total > 0:
        pcd = [i/total for i in pcd]
    return pcd
