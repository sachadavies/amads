"""Test suite for functions inside amads/algorithms/complexity.py"""

import pytest

from amads.algorithms.complexity import lz77_decode, lz77_encode

DECODED_SEQUENCES = [
    # The following four examples are from https://timguite.github.io/jekyll/update/2020/03/15/lz77-in-python.html
    ["a"],
    ["a", "b", "a"],
    ["w", "o", "r", "d", " ", "w", "o", "r", "d"],
    ["a", "b", "a", "b", "a", "b", "a", "b"],
    # This example is taken (with a bit of retooling to match our input structure, but the same results) from
    # https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wusp/fb98aa28-5cd7-407f-8869-a6cef1ff1ccb
    ["A", "A", "B", "C", "B", "B", "A", "B", "C"],
]

ENCODED_SEQUENCES = [
    [(0, 1, "a")],
    [(0, 1, "a"), (0, 1, "b"), (2, 1, "a")],
    [(0, 1, "w"), (0, 1, "o"), (0, 1, "r"), (0, 1, "d"), (0, 1, " "), (5, 4, "w")],
    [(0, 1, "a"), (0, 1, "b"), (2, 6, "a")],
    [
        (0, 1, "A"),
        (1, 1, "A"),
        (0, 1, "B"),
        (0, 1, "C"),
        (2, 1, "B"),
        (3, 1, "B"),
        (5, 3, "A"),
    ],
]


@pytest.mark.parametrize(
    "to_encode,to_decode", zip(DECODED_SEQUENCES, ENCODED_SEQUENCES)
)
def test_lz77_encode_decode(to_encode, to_decode):
    # Encode and decode the sequence
    encoded = lz77_encode(to_encode)
    decoded = lz77_decode(encoded)
    # Encoded, the sequence should be as we expect
    assert encoded == to_decode
    # Decoding the sequence should give the original input
    assert decoded == to_encode
