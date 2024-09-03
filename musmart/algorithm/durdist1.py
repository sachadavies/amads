
"""
Provides the `durdist1` function

Original doc: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6e06906ca1ba0bf0ac8f2cb1a929f3be95eeadfa#page=58
"""

from musmart import Score, Note
import math

print("importing durdist1.py")  # TODO: remove this


def durdist1(score: Score) -> list[float]:
    """
    Returns the distribution of note durations in a Score.
    
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
        list[float]: 9-component list of the distribution of note durations.
    """
    
    dd = [0] * 9
    for note in score.find_all(Note):
        # The following algorithm comes from the original MATLAB implementation
        # https://github.com/miditoolbox/1.1/blob/master/miditoolbox/durdist1.m
        if note.dur != 0:
            bin = round(2 * math.log2(note.dur)) + 4
            if bin <= 8:
                dd[bin] += 1
                
    # normalize
    total = sum(dd)
    if total > 0:
        dd = [i/total for i in dd]
        
    return dd
            
    
