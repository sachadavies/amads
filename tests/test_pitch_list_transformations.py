"""
NAME:
===============================
Test Pitch List Transformations (test_pitch_list_transformations.py)


BY:
===============================
Mark Gotham, 2021


LICENCE:
===============================
Creative Commons Attribution-ShareAlike 4.0 International License
https://creativecommons.org/licenses/by-sa/4.0/


SOURCE:
===============================
Gotham and Yust, Serial Analyser, DLfM 2021
https://github.com/MarkGotham/Serial_Analyser


ABOUT:
===============================
Functions for transforming pitch lists:
e.g., transposition, inversion, retrograde, rotation.

Most apply equally to any pitch class sequence,
some are more specific to tone rows.

"""

import unittest
from musmart import pitch_list_transformations


class RowTester(unittest.TestCase):

    def testTranspose(self):
        row_boulez = [3, 2, 9, 8, 7, 6, 4, 1, 0, 10, 5, 11]
        zero_boulez = transpose_to(row_boulez, start=0)
        self.assertEqual(zero_boulez, [0, 11, 6, 5, 4, 3, 1, 10, 9, 7, 2, 8])
        trans_boulez = transpose_to(zero_boulez, start=3)
        self.assertEqual(trans_boulez, [3, 2, 9, 8, 7, 6, 4, 1, 0, 10, 5, 11])
        trans_by_boulez = transpose_by(trans_boulez, semitones=2)
        self.assertEqual(trans_by_boulez, [5, 4, 11, 10, 9, 8, 6, 3, 2, 0, 7, 1])

    def testRotate(self):
        luto = [0, 6, 5, 11, 10, 4, 3, 9, 8, 2, 1, 7]
        for i in range(12):
            row = rotate(luto, i)
            self.assertEqual(row[0], luto[i])

    def testInvert(self):
        test_set = [0, 1, 4, 6]
        self.assertEqual(invert(test_set), [0, 11, 8, 6])

    def testPitches_to_intervals(self):
        test_row_up = [x for x in range(12)]
        self.assertEqual(pitches_to_intervals(test_row_up), [1]*11)
        test_row_down = test_row_up[::-1]
        self.assertEqual(pitches_to_intervals(test_row_down), [11]*11)

    def testRotate_hexachords(self):
        """Using Krenek's example"""
        row_krenek = [5, 7, 9, 10, 1, 3, 11, 0, 2, 4, 6, 8]
        rotated_krenek = rotate_hexachords(row_krenek)
        self.assertEqual(len(rotated_krenek), 7)
        self.assertEqual(rotated_krenek[-1], row_krenek)

    def test_pair_swap_and_retrograde(self):
        """Using Krenek's example"""
        test_row_ = [9, 2, 3, 6, 5, 1, 7, 4, 8, 0, 10, 11]
        test_pair_swap_krenek = pair_swap_krenek(test_row_)
        self.assertEqual(len(test_pair_swap_krenek), 13)
        self.assertEqual(test_pair_swap_krenek[-1], retrograde(test_row_))
