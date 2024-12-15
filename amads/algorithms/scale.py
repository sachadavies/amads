"""

Original doc: https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6e06906ca1ba0bf0ac8f2cb1a929f3be95eeadfa#page=88

Scales note data in given dimension (delta, dur, or both)

Input arguments:
SCORE = score object/other EventGroup object (Note: This method MODIFIES the score object input)
FACTOR = amount of scale (must be > 0)
DIM = dimension ('delta', 'dur','all')
    - 'delta': scales the delta of ALL EVENTS
    - 'dur': scales the durations of ALL NON-EVENTGROUP EVENTS (Note, Rest)
    - 'all': scales both the delta and the duration

Output:
SCORE = the scaled version of the input object

Examples:
scaled_score = scale(score.copy(),'delta',2); % scales delta by a factor of 2
scaled_score = scale(score.copy(),'dur',0.5); % shortens durations by a factor of 2

"""

from ..core.basics import EventGroup


def scale(score, factor=2, dim="all"):
    if dim == "all":
        scale(score, factor, "dur")
        scale(score, factor, "delta")
        return score
    for elem in score.content:
        if isinstance(elem, EventGroup):
            scale(elem, factor, dim)
            if dim == "delta":
                elem.delta *= 2
        else:
            if dim == "dur":
                elem.dur *= factor
            elif dim == "delta":
                elem.delta *= 2
        score.dur = max(score.dur, elem.delta_end)
    return score
