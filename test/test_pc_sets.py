"""
NAME:
===============================
Test PC Sets (test_pc_sets.py)

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

"""

from musmart import pitch_list_transformations
import unittest


class PCTester(unittest.TestCase):

    def test_pitches_to_prime(self):
        """
        Tests one case through the interval vector, and another that requires transformation.
        """
        prime = pitches_to_prime((0, 2, 3))
        self.assertEqual(prime, (0, 1, 3))

        # Test one case of numbers beyond 0-11
        prime = pitches_to_prime((100, 102, 103))
        self.assertEqual(prime, (0, 1, 3))

        prime = pitches_to_prime((8, 2, 4, 7))  # via I [0,2,5,6], t2 [2,4,7,8], and shuffle.
        self.assertEqual(prime, (0, 1, 4, 6))

    def test_self_complement_hexachords(self):
        """
        Tests that all and only the hexachords without a Z-related pair are self-complementary.
        (In so doing, this also tests the pitches-to-prime routine.)
        """

        count_hexachords = 0
        count_total = 0
        for entry in set_classes_from_cardinality(6):
            hexachord = entry[1]
            complement = tuple([x for x in range(12) if x not in hexachord])
            complement_prime = pitches_to_prime(complement)
            if hexachord == complement_prime:
                self.assertFalse('Z' in entry[0])
                count_hexachords += 1
                count_total += entry[3]
            else:
                self.assertTrue('Z' in entry[0])

        self.assertEqual(count_hexachords, 20)  # 20/50, so 40%
        self.assertEqual(count_total, 372)  # 372/924, so 35.4%
