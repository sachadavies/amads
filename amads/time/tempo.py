#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements various functions related to linear tempo modeling e.g., `tempo_slope`, `tempo_drift`"""

from collections import namedtuple
from typing import Iterable

import numpy as np

# Little wrapper class we can use to return regression results nicely
LinearRegressionWrapper = namedtuple(
    "LinearRegressionWrapper",
    ["slope", "intercept", "slope_stderr", "intercept_stderr", "r2"],
)


def tempo_slope(beats: Iterable[float]) -> float:
    """
    Return the tempo slope for an array of beats.

    The tempo slope is the signed overall tempo change per second within a performance, equivalent
    to the slope of a linear regression of instantaneous tempo against beat onset time,
    such that a negative slope implies deceleration over time and a positive slope acceleration [1].

    Parameters
    ----------
    beats : Iterable[float]
        An iterable of beat timestamps in seconds corresponding to, e.g., quarter notes.

    Returns
    -------
    float
        The tempo slope value.

    Raises
    ------
    ValueError
        If linear regression cannot be calculated.

    References
    ----------
    [1] Cheston H., Cross, I., Harrison, P. (2024). Trade-offs in Coordination Strategies for
        Duet Jazz Performances Subject to Network Delay and Jitter. Music Perception, 42/1 (pp. 48–72).
        https://doi.org/10.1525/mp.2024.42.1.48

    """

    return float(fit_tempo_linear_regression(beats).slope)


def tempo_drift(beats: Iterable[float]) -> float:
    """
    Return the tempo drift for an array of beats.

    The tempo drift is the standard error of the slope of the overall tempo change in a performance,
    such that larger values imply a greater departure from a linear tempo slope (i.e., not just
    accelerating or decelerating).

    Parameters
    ----------
    beats : Iterable[float]
        An iterable of beat timestamps in seconds corresponding to, e.g., quarter notes.

    Returns
    -------
    float
        The tempo drift value.

    Raises
    ------
    ValueError
        If linear regression cannot be calculated.

    """

    return float(fit_tempo_linear_regression(beats).slope_stderr)


def tempo_fluctuation(beats: Iterable[float]) -> float:
    """
    Calculates the percentage fluctuation about the overall tempo of provided `beats`.

    Tempo fluctuation can be calculated as the standard deviation of the tempo of a
    performance normalized by the mean tempo [1].

    Parameters
    ----------
    beats : Iterable[float]
        An iterable of beat timestamps in seconds corresponding to, e.g., quarter notes.

    Returns
    -------
    float
        The tempo fluctuation value.

    Examples
    --------
    >>> my_beats = [1., 2., 3., 4.]  # stable performance
    >>> tempo_fluctuation(my_beats)
    0.0

    References
    ----------
    [1] Cheston, H., Schlichting, J.L., Cross, I., and Harrison, P.M.C. (2024).
        Jazz Trio Database: Automated Annotation of Jazz Piano Trio Recordings Processed Using
        Audio Source Separation. Transactions of the International Society for Music Information
        Retrieval, 7/1 (pp. 144–158). https://doi.org/10.5334/tismir.186

    """

    # Validate the input before going any further (e.g., raise an error on NaN values)
    validate_beats(beats)
    # Compute instantaneous tempo values
    tempos = beats_to_tempo(beats)
    # Compute tempo fluctuation
    # No need for np.nanstd etc. here, we won't have NaN values
    return float(np.std(tempos) / np.mean(tempos))


def validate_beats(beats: Iterable[float]) -> None:
    """Checks an iterable of beat timestamps and raises errors as required"""

    beats_arr = np.array(beats, dtype=float)  # expecting a float dtype
    if np.isnan(np.sum(beats_arr)):
        raise ValueError(
            "Cannot calculate instantaneous tempo measurements from array of beats with missing values"
        )
    if len(beats_arr) < 2:
        raise ValueError("Must pass at least two beat timestamps")
    if len(beats_arr.shape) != 1:
        raise ValueError("Beat timestamps must be 1-dimensional")
    if not np.array_equal(np.sort(beats_arr), beats_arr):
        raise ValueError("Beat timestamps must increase linearly")
    if len(np.unique(beats_arr)) != len(beats_arr):
        raise ValueError("Beat timestamps must not contain duplicates")


def beats_to_tempo(beats: np.ndarray) -> np.ndarray:
    """Converts beat timestamps to instantaneous tempo measurements. Raises ValueError if any beats are missing."""

    return np.array(60 / np.diff(beats))


def linregress(x: np.ndarray, y: np.ndarray) -> LinearRegressionWrapper:
    """Fits a simple linear regression model between target + one predictor variable"""

    # Handle invalid inputs: either empty or all identical
    if x.size == 0 or y.size == 0:
        raise ValueError(
            f"Inputs must not be empty, but got `x` with size {x.size}, `y` with size {y.size}."
        )
    if np.amax(x) == np.amin(x) and len(x) > 1:
        raise ValueError(
            "Cannot calculate a linear regression if all `x` values are identical"
        )
    # Average sums of square differences from the mean
    ssxm, ssxym, _, ssym = np.cov(x, y, bias=1).flat
    # R-value
    if ssxm == 0.0 or ssym == 0.0:
        # Handles ZeroDivisionErrors
        r = 0.0
    else:
        r = ssxym / np.sqrt(ssxm * ssym)
    # Clamp between -1 < r < 1
    r = max(-1, min(r, 1))
    # Compute R^2
    r2 = r**2
    # Computing slope and intercept
    slope = ssxym / ssxm
    intercept = np.mean(y, None) - slope * np.mean(x, None)
    # Handle case when only two points are passed in
    if len(x) == 2:
        slope_stderr, intercept_stderr = 0.0, 0.0
    else:
        df = len(x) - 2  # Number of degrees of freedom
        slope_stderr = np.sqrt((1 - r2) * ssym / ssxm / df)
        intercept_stderr = slope_stderr * np.sqrt(ssxm + np.mean(x, None) ** 2)
    # Return everything as a neatly formatted named tuple, allowing dot access to attributes
    return LinearRegressionWrapper(
        slope=slope,
        intercept=intercept,
        slope_stderr=slope_stderr,
        intercept_stderr=intercept_stderr,
        r2=r2,
    )


def fit_tempo_linear_regression(beats: Iterable[float]) -> LinearRegressionWrapper:
    """Fits linear regression of BPM measurements vs. onset time."""

    # Validate our input before going any further
    validate_beats(beats)
    # Target variable: BPM measurements
    # This will also raise an error on NaN values
    beats_arr = np.array(beats)
    y = beats_to_tempo(beats_arr)
    # Predictor variable: the onset time
    x = beats_arr[1:]
    return linregress(x, y)
