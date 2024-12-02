# SMART: Symbolic Music Algorithm Resource Toolkit

This is an attempt to see if the large field (or several fields) of music computing can coordinate a directory of the core algorithms for computing symbolic music.

For more on the motivation and background, please see [the paper](./paper.md)


## Design principles

1. Preference for one language: it makes sense to have a single reference language for interoperability, comparison and more.
2. That language is Python, for all the usual reasons, chief among them being it popularity.
   - some designers of computer languages programming languages may find that a rather shallow reason,
   - but commitment to access and interoperability makes a language's existing popularity critically important.
   - e.g., we have in mind the student of music who gets that computing will open things up for them, but who also wants the time they invest in learning the ropes to be transferable in case they ever want or need to move away from music computing (imagine!).
3. Algorithms linked to a credible publication
   - ... or other demonstrable take-up by the community.
   - implemented here as exactly as reference to the source allows (usually from scratch)
   - Open source, well documented, etc.
4. Minimal dependencies / imports: typically `numpy`, `pandas`, `matplotlib`, with partitura and/or music21 for input/output, and nothing else.
5. Maximally modular and interoperable:
     - wherever possible, scripts are fully modular and can be used independently and recombined however needed.
     - this enables users to "cherry pick" the bits they need without wading through a thicket of dependencies.


## Uses

We welcome all and any uses.
Among them, we anticipate:

- researchers using existing algorithms "off the shelf" for comparison with a new approach
- students learning a standard algorithm by implementing is from scratch and comparing the output with a reference implementation.
- those considering entry into the field to browse all this casually.


## Contributions

... are welcome!

Please pitch in relevant material, making sure to include any relevant citation.
Equaly, please feel free to add issues for algorithms you'd like to see us implement and include here.


## Licence

(Almost) all the algorithms and resources here appear in published literature.

We cite those sources in the directory and defer to those authors for licence -
please refer to the source for details.

We sincerely believe that everything here is included legitimately.
Please get in touch if you have any questions or concerns.

For new content, where not specified directly in the document, the licenses is CC-by-SA 4.0.
I.e., if you contribute and do not specify otherwise, you agree to the [CC-by-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en) license or a more permissive one.
Very briefly, CC-by-SA gives you the right to share and adapt this material, including for commercial purposes, provided you give appropriate credit and share under the same or compatible (e.g. GPL v3) license. [Full details are here](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en).


## Development

### Running tests

See `docs/developer_notes/testing.md` for instructions on running tests.
