"""Implements various functions related to complexity and information density."""

from typing import Hashable, Iterable, Union


def lz77_encode(input_list: list[Hashable]) -> list:
    """Runs the LZ77 compression algorithm over the input `data`, generating tuples of (distance, length) or (char)"""

    # Catch sequences that have a length of zero
    if len(input_list) == 0:
        raise ValueError("Cannot encode an empty sequence!")
    encoded = []
    i = 0
    while i < len(input_list):
        best_length = 0
        best_distance = 0
        # Search the entire processed portion (positions 0 to i-1)
        for j in range(0, i):
            length = 0
            # Allow overlapping matches: compare while within input bounds.
            while (
                (i + length < len(input_list))
                and (j + length < len(input_list))
                and (input_list[j + length] == input_list[i + length])
            ):
                length += 1
            if length > best_length:
                best_length = length
                best_distance = i - j
        # If a match was found, output a match token.
        if best_length > 0:
            encoded.append((best_distance, best_length, input_list[i]))
            i += best_length
        else:
            # No match: output a literal token with length 1.
            encoded.append((0, 1, input_list[i]))
            i += 1
    return encoded


def lz77_decode(encoded: list[int, int, Hashable]) -> list[Hashable]:
    """Decode a list of LZ77 tokens, each of which are 3-tuples with form (distance, length, symbol)"""

    # Catch sequences that have a length of zero
    if len(encoded) == 0:
        raise ValueError("Cannot decode an empty sequence!")
    decoded = []
    for token in encoded:
        distance, length, symbol = token
        # Literal token: simply append the symbol.
        if distance == 0:
            decoded.append(symbol)
        # Match token: copy 'length' characters from the already decoded list,
        # starting at position len(decoded) - distance.
        else:
            start = len(decoded) - distance
            for i in range(length):
                decoded.append(decoded[start + i])
    return decoded


def lz77_complexity(
    sequence: Iterable[Hashable], proportional: bool = False
) -> Union[int, float]:
    """
    Applies the LZ77 compression algorithm [1] to a discrete `sequence` and returns the length of the compressed result.

    Inputs are discrete sequences of any hashable type, e.g. strings, floats, integers. Intuitively, higher
    values mean that more information is required to represent the sequence, indicating greater complexity (as in [2]).

    Parameters
    ----------
    sequence : Iterable[Hashable]
        A discrete sequence, which could be pitch classes, inter-onset intervals, etc.

    proportional : bool, optional
        If True, the complexity is expressed with respect to the size of the input, such that 1.0 means the input
        cannot be compressed (i.e., maximum possible complexity). Default is False.

    Returns
    -------
    int | float
        The length of the compressed string, either in `raw` form (int) or wrt. input sequence length (float)

    References
    ----------
    [1] Ziv, J., & Lempel, A. (1977). A universal algorithm for sequential data compression. IEEE Transactions on
        Information Theory, 23/3, 337–343. https://doi.org/10.1109/TIT.1977.1055714

    [2] Cheston, H., Schlichting, J. L., Cross, I., & Harrison, P. M. C. (2024). Rhythmic qualities of jazz
        improvisation predict performer identity and style in source-separated audio recordings. Royal Society
        Open Science, 11/11. https://doi.org/10.1098/rsos.240920

    """

    # Compress the sequence
    compressed = lz77_encode(sequence)
    # Express with relation to length of input string if required: returns a float
    if proportional:
        return len(compressed) / len(sequence)
    # Otherwise, take the length of the compressed string as the complexity of the input: returns an int
    else:
        return len(compressed)
