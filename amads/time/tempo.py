"""
This module provides functions for analyzing tempo characteristics in musical performances.
It includes calculations for tempo slope, tempo drift, and tempo fluctuation.

References:
    - Cheston, H., Schlichting, J. L., Cross, I., & Harrison, P. M. C. (2024).
      Jazz Trio Database: Automated Annotation of Jazz Piano Trio Recordings Processed Using
      Audio Source Separation. Transactions of the International Society for Music Information
      Retrieval, 7(1), 144–158. https://doi.org/10.5334/tismir.186

    - Cheston, H., Cross, I., & Harrison, P. (2024). Trade-offs in Coordination Strategies
      for Duet Jazz Performances Subject to Network Delay and Jitter.
      Music Perception, 42(1), 48–72. https://doi.org/10.1525/mp.2024.42.1.48

Author:
    Huw Cheston (2025)
"""

from collections import namedtuple
from typing import Iterable, Union

import numpy as np

__author__ = "Huw Cheston"

# Little wrapper class we can use to return regression results nicely
LinearRegressionWrapper = namedtuple(
    "LinearRegressionWrapper",
    ["slope", "intercept", "slope_stderr", "intercept_stderr", "r2"],
)


# flake8: noqa: W605
def tempo_slope(beats: Iterable[float]) -> float:
    r"""
    Calculates the tempo slope for a sequence of beat timestamps.

    The tempo slope represents the overall tempo change per second in a performance.
    It is determined by the slope of a linear regression of instantaneous tempo against
    beat onset time. A negative slope indicates deceleration, while a positive slope
    indicates acceleration.

    The equation is:

    .. math::
        \hat{S} = \frac{\sum\limits_{i=1}^N (x_i - \bar{x}) (y_i - \bar{y})}{\sum\limits_{i=1}^N (x_i - \bar{x})^2},

    where :math:`x_i` is the time of beat :math:`i` and :math:`y_i` is the tempo value in
    quarter-note beats-per-minute.

    Args:
        beats (Iterable[float]):
            An iterable of beat timestamps in seconds, such as quarter-note onsets.

    Returns:
        float: The computed tempo slope value.

    """

    return float(fit_tempo_linear_regression(beats).slope)


# flake8: noqa: W605
def tempo_drift(beats: Iterable[float]) -> float:
    r"""
    Calculates the tempo drift for a sequence of beat timestamps.

    The tempo drift is the standard error of the slope of the overall tempo change in a performance,
    such that larger values imply a greater departure from a linear tempo slope (i.e., not just
    accelerating or decelerating).

    The equation is:

    .. math::
        SE_\hat{S} = \frac{\sigma}{\sqrt{\sum\limits_{i=1}^{N} (x_i - \bar{x})^2}},

    where:

    .. math::
        \sigma = \sqrt{\frac{\sum\limits_{i=1}^{N} (y_i - (\hat{S} x_i + \hat{b}))^2}{N - 2}},

    and:

    - :math:`x_i` is the time of beat :math:`i`.
    - :math:`y_i` is the tempo value in quarter-note beats-per-minute.
    - :math:`\hat{S}` is the estimated slope of the regression.
    - :math:`\hat{b}` is the intercept.
    - :math:`N` is the number of data points.

    Args:
        beats (Iterable[float]):
            An iterable of beat timestamps in seconds, such as quarter-note onsets.

    Returns:
        float: The computed tempo drift value.

    """

    return float(fit_tempo_linear_regression(beats).slope_stderr)


# flake8: noqa: W605
def tempo_fluctuation(beats: Iterable[float]) -> float:
    r"""
    Calculates the percentage fluctuation around the overall tempo of a sequence of beats.

    Tempo fluctuation is measured as the standard deviation of the instantaneous tempo,
    normalized by the mean tempo. Higher values indicate greater variability in tempo.

    The equation is:

    .. math::
        \text{F} = \dfrac{\sqrt{\frac{1}{N-1} \sum\limits_{i=1}^N (y_i - \bar{y})^2}}{\bar{y}},

    where :math:`y_i` is the tempo value in quarter-note beats-per-minute at beat :math:`i`.

    Args:
        beats (Iterable[float]):
            An iterable of beat timestamps in seconds, such as quarter-note onsets.

    Returns:
        float: The computed tempo fluctuation value.

    """

    # Compute instantaneous tempo values: this will also validate the input
    tempos = beats_to_tempo(beats)
    # Compute tempo fluctuation
    # No need for np.nanstd etc. here, we won't have NaN values
    return float(np.std(tempos) / np.mean(tempos))


def _validate_beats(beats: Union[Iterable[float], np.ndarray]) -> None:
    """Checks an iterable of beat timestamps and raises errors as required"""

    if not isinstance(beats, np.ndarray):
        beats = np.array(beats, dtype=float)  # expecting a float dtype
    if np.isnan(np.sum(beats)):
        raise ValueError(
            "Cannot calculate instantaneous tempo measurements from array of beats with missing values"
        )
    if len(beats) < 2:
        raise ValueError("Must pass at least two beat timestamps")
    if len(beats.shape) != 1:
        raise ValueError("Beat timestamps must be 1-dimensional")
    if not np.array_equal(np.sort(beats), beats):
        raise ValueError("Beat timestamps must increase linearly")
    if len(np.unique(beats)) != len(beats):
        raise ValueError("Beat timestamps must not contain duplicates")


def beats_to_tempo(beats: np.ndarray) -> np.ndarray:
    """Converts beat timestamps to instantaneous tempo measurements."""

    # Raise error on invalid inputs
    _validate_beats(beats)
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

    # Target variable: BPM measurements
    # This will also validate the input
    beats_arr = np.array(beats)
    y = beats_to_tempo(beats_arr)
    # Predictor variable: the onset time
    x = beats_arr[1:]
    return linregress(x, y)
