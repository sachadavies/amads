"""Test suite for tempo modelling functions inside amads/time/tempo.py"""

import numpy as np
import pytest

from amads.time.tempo import (
    LinearRegressionWrapper,
    _validate_beats,
    beats_to_tempo,
    linregress,
    tempo_drift,
    tempo_fluctuation,
    tempo_slope,
)

# Quarter note beat positions for different "performances"
STABLE_PERFORMANCE = [1.0, 2.0, 3.0, 4.0]
ACCELERATING_PERFORMANCE = [1.0, 1.9, 2.7, 3.4]
DECELERATING_PERFORMANCE = [1.0, 2.1, 3.3, 4.6]


def test_tempo_slope():
    assert tempo_slope(STABLE_PERFORMANCE) == 0.0
    assert tempo_slope(ACCELERATING_PERFORMANCE) > 0
    assert tempo_slope(DECELERATING_PERFORMANCE) < 0


def test_tempo_drift():
    # Compare tempo drift of stable vs. unstable performances together
    assert tempo_drift(STABLE_PERFORMANCE) < tempo_drift(ACCELERATING_PERFORMANCE)
    assert tempo_drift(STABLE_PERFORMANCE) < tempo_drift(DECELERATING_PERFORMANCE)


def test_tempo_fluctuation():
    # Stable performance should not fluctuate
    assert tempo_fluctuation(STABLE_PERFORMANCE) == 0.0
    # Unstable performances should fluctuate
    assert tempo_fluctuation(ACCELERATING_PERFORMANCE) > 0
    assert tempo_fluctuation(DECELERATING_PERFORMANCE) > 0


def test_linregress_basic():
    # Perfect linear relationship: y = 2x
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    result = linregress(x, y)
    assert isinstance(result, LinearRegressionWrapper)
    assert pytest.approx(result.slope, rel=1e-6) == 2.0
    assert pytest.approx(result.intercept, rel=1e-6) == 0.0
    assert pytest.approx(result.r2, rel=1e-6) == 1.0
    assert result.slope_stderr >= 0
    assert result.intercept_stderr >= 0


def test_linregress_twopoints():
    x = np.array(
        [
            1,
            2,
        ]
    )
    y = np.array([3, 6])
    result = linregress(x, y)
    assert pytest.approx(result.slope, rel=1e-6) == 3.0
    assert result.slope_stderr == 0.0
    assert result.intercept_stderr == 0.0


def test_lineregress_horizontal():
    # All y-values are the same, so no slope
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([3, 3, 3, 3, 3])
    result = linregress(x, y)
    assert pytest.approx(result.slope, rel=1e-6) == 0.0
    assert pytest.approx(result.intercept, rel=1e-6) == 3.0
    assert pytest.approx(result.r2, rel=1e-6) == 0.0


def test_linregress_bad_inputs():
    # First, test when all target variable values are identical
    x = np.array([2, 2, 2, 2])
    y = np.array([1, 2, 3, 4])
    with pytest.raises(ValueError):
        linregress(x, y)
    # Second, test when inputs are empty
    x = np.array([])
    y = np.array([])
    with pytest.raises(ValueError):
        linregress(x, y)


def test_beats_to_tempo():
    # With a stable performance with IBI = 1.0, we'll expect a full array of 60 BPMs
    stable_bpms = beats_to_tempo(STABLE_PERFORMANCE)
    assert np.array_equal(
        stable_bpms.round(1),
        np.array(
            [
                60.0,
                60.0,
                60.0,
            ]
        ),
    )
    # Test another performance that accelerates: IBIs decrease, BPMs increase
    accelerating_bpms = beats_to_tempo(ACCELERATING_PERFORMANCE)
    assert np.array_equal(accelerating_bpms.round(1), np.array([66.7, 75, 85.7]))
    # Test another performance that decelerates: IBIs increase, BPMs decrease
    decelerating_bpms = beats_to_tempo(DECELERATING_PERFORMANCE)
    assert np.array_equal(decelerating_bpms.round(1), np.array([54.5, 50.0, 46.2]))


def test_validate_beats():
    # Valid case (should not raise an error)
    valid_beats = [0.5, 1.0, 1.5, 2.0, 2.5]
    assert _validate_beats(valid_beats) is None
    # Too few beats
    with pytest.raises(ValueError):
        _validate_beats([0.5])
    # Non-1D array
    with pytest.raises(ValueError):
        _validate_beats([[0.5, 1.0], [1.5, 2.0]])
    # Unsorted beats
    with pytest.raises(ValueError):
        _validate_beats([0.5, 1.5, 1.0, 2.0])
    # Duplicate values
    with pytest.raises(ValueError):
        _validate_beats([0.5, 1.0, 1.0, 2.0])  # Duplicate 1.0
    # NaN values
    with pytest.raises(ValueError):
        _validate_beats([0.5, 1.0, None, 2.0])
