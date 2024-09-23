"""
NAME:
===============================
Test Partimenti (test_partimenti.py)


BY:
===============================
Mark Gotham, 2019


LICENCE:
===============================
Creative Commons Attribution-ShareAlike 4.0 International License
https://creativecommons.org/licenses/by-sa/4.0/


"""

from musmart import partimenti
import unittest


class PartiTester(unittest.TestCase):

    def test_partimenti_length(self):
        """
        For each partimento,
        there should be a fixed numer of 'stages'
        meaning that the melody, bass, and figures data should have the same length.
        """
        for p in [
            aprile,
            cadenza_doppia,
            cadenza_semplice,
            comma,
            converging,
            deceptive,
            do_re_mi,
            evaded,
            fonte,
            fenaroli,
            indugio,
            jupiter,
            meyer,
            modulating_prinner,
            monte,
            passo_indietro,
            pastorella,
            ponte,
            prinner,
            quiescenza,
            romanesca,
            sol_fa_mi
        ]:
            assert len(p["melody"]) == len(p["bass"])
            assert len(p["melody"]) == len(p["figures"])