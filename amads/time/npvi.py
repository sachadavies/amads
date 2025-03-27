"""
Normalized pairwise variability index for notes in a Score.

Author: Huw Cheston
Date: 2025

Citation: Daniele, J. R., & Patel, A. D. (2013). An Empirical Study of Historical Patterns in Musical Rhythm.
          Music Perception, 31/1 (pp. 10-18). https://doi.org/10.1525/mp.2013.31.1.10
          Condit-Schultz, N. (2019). Deconstructing the nPVI: A Methodological Critique of the Normalized
          Pairwise Variability Index as Applied to Music. Music Perception, 36/3 (pp. 300–313).
          https://doi.org/10.1525/mp.2019.36.3.300

"""

from typing import Iterable


def normalized_pairwise_variability_index(durations: Iterable[float]) -> float:
    """
    Extracts the normalised pairwise variability index (nPVI).

    The nPVI is a measure of variability between successive elements in a sequence, commonly used
    in music analysis to quantify rhythmic variability. The equation is
    .. math:: \text{nPVI} = \frac{100}{m-1} \times \sum\limits_{k=1}^{m-1} \left| \frac{d_k - d_{k+1}}{\frac{d_k + d_{k+1}}{2}} \right|    # noqa: W605
       :label: nPVI
    where :math:`n` is the number of intervals, and :math:`d_i` is the duration of the :math:`i^{th}` interval.

    Parameters
    ----------
    durations : Iterable[float]
        The durations to analyse

    Returns
    -------
    float
        The extracted nPVI value.

    Examples
    --------
    The first example is taken from Condit-Schultz (2019, Figure 1).

        >>> durs = [1., 1., 1., 1.]
        >>> normalized_pairwise_variability_index(durations=durs)
        0.

    The second example is Daniele & Patel (2013, Appendix).

        >>> durs = [1., 1/2, 1/2, 1., 1/2, 1/2, 1/3, 1/3, 1/3, 2., 1/3, 1/3, 1/3, 1/3, 1/3, 1/3, 3/2, 1., 1/2]
        >>> x = normalized_pairwise_variability_index(durations=durs)
        >>> round(x, 1)
        42.2

    """

    numerator = (
        sum(
            [
                abs((k - k1) / ((k + k1) / 2))
                for (k, k1) in zip(durations, durations[1:])
            ]
        )
        * 100
    )
    denominator = len(durations) - 1
    return numerator / denominator
