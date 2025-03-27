"""Test suite for functions in amads.time.npvi"""

import unittest

from amads.time.npvi import normalized_pairwise_variability_index


class NPVITest(unittest.TestCase):
    def test_daniele_patel_2013_example_1(self):
        """Tests the first example given in the Appendix of Daniele & Patel (2013, p. 18)"""
        # This theme is from Debussy's Quartet in G Minor for Strings (1st mvmt., 2nd theme)
        durations = [
            1.0,
            1 / 2,
            1 / 2,
            1.0,
            1 / 2,
            1 / 2,
            1 / 3,
            1 / 3,
            1 / 3,
            2.0,
            1 / 3,
            1 / 3,
            1 / 3,
            1 / 3,
            1 / 3,
            1 / 3,
            3 / 2,
            1.0,
            1 / 2,
        ]
        # Values given in the paper are only reported to 1 d.p.
        expected = 42.2
        actual = normalized_pairwise_variability_index(durations)
        self.assertEqual(expected, round(actual, 1))

    def test_daniele_patel_2013_example_2(self):
        """Tests the second example given in the Appendix of Daniele & Patel (2013, p. 18)"""
        # This theme is from Elgar's Symphony No. 1 in A Flat, Op. 55 (4th mvmt., 2nd theme)
        durations = [
            1.0,
            3 / 2,
            1 / 2,
            2 / 3,
            2 / 3,
            2 / 3,
            3 / 2,
            1 / 2,
            3 / 2,
            1 / 2,
            3 / 2,
            1 / 2,
            2 / 3,
            2 / 3,
            2 / 3,
            3 / 2,
            1 / 2,
            3 / 2,
            1 / 2,
            2 / 3,
            2 / 3,
            2 / 3,
            3 / 2,
        ]
        # Values given in the paper are only reported to 1 d.p.
        expected = 57.1
        actual = normalized_pairwise_variability_index(durations)
        self.assertEqual(expected, round(actual, 1))

    def test_schultz_figure_1(self):
        """Tests all the examples given in Figure 1 of Condit-Schultz (2019, p. 301)"""
        all_durations = [
            [1.0, 1.0, 1.0, 1.0],
            [1.0, 1 / 2, 1 / 2, 1.0, 1 / 2, 1 / 2],
            [1.0, 1 / 2, 1.0, 1 / 2],
            [3 / 2, 1 / 2, 3 / 2, 1 / 2],
            [7 / 16, 1 / 16, 7 / 16, 1 / 16],
        ]
        # Results are inconsistent in rounding, so I'm just rounding to nearest 1 d.p. here
        expected_results = [0.0, 40.0, 66.7, 100.0, 150.0]
        for duration, expected in zip(all_durations, expected_results):
            actual = normalized_pairwise_variability_index(duration)
            self.assertEqual(expected, round(actual, 1))

    def test_not_enough_durations(self):
        """Test we raise an error with not enough durations"""
        with self.assertRaises(ValueError):
            bad_durations = [2.0]
            _ = normalized_pairwise_variability_index(bad_durations)
        with self.assertRaises(ValueError):
            also_bad_durations = []
            _ = normalized_pairwise_variability_index(also_bad_durations)

    def test_non_positive_durations(self):
        """Test we raise an error with negative or non-positive durations"""
        with self.assertRaises(ValueError):
            bad_durations = [1.0, 0.0, 3.0, 2.0]
            _ = normalized_pairwise_variability_index(bad_durations)
        with self.assertRaises(ValueError):
            also_bad_durations = [3.0, 3.0, -3.0, 2.0]
            _ = normalized_pairwise_variability_index(also_bad_durations)
