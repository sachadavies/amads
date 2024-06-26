# Music Computing Tooklit: a guide to algorithmic resources

This is an attempt to see if the large field (or several fields) of music computing can coordinate a directory of the core algorithms for computing symbolic music.

Quick links:

1. Take me to the directory! --> [Ok, here it is](./directory) 
2. Wait, what? Please explain! --> Read the rest of this README which includes details of the
[remit](#Remit),
[motivation](#Motivation),
anticipated [uses](#Uses),
broad [structure](#Structure) and design,
and more besides.


## Remit

Unlike most such directories, the goal is to:

- combine:
  - links to existing resources that meet the [criteria set out below](#criteria)
  - new implementations locally only when they're not provided elsewhere.
- limit:
  - to the remit set out here and [criteria below](#criteria)

This spans algorithms for multiple formats (e.g., both _audio_ and _symbolic_),
and fields of research (notably).
That said, there is a lot more of this kind of material out there for audio (and especially signal processing) than some other parts of the equation, so we focus (at least initially) on coordinating the more scattered and uncoordinated parts.


## Motivation

[Explain entry points, lost labour in searching out resources, unknown quality.]

A great deal of good work has been done in this field, but there is also rather little coordination.
At one time [humdrum](https://www.humdrum.org/) was a/the central point of reference. 
That continues to be used and maintained (an impressive 40 years later!),
but there are downsides, e.g., the 'language neutral' set up is commendable,
but not very inviting for newcomers (again, see criteria below).

Later, along came [music21](https://github.com/cuthbertLab/music21).
First published in 2010/11, this too continues to be maintained.
That said, the creator-maintainer of music21 recently made the
[explicit decision (announced/reported here)](https://groups.google.com/g/music21list/c/HF3tgkMvNWI/m/7vaIHr88BAAJ)
that it is _not_ / _no longer_ there to provide the holistic directory function stated here;
instead it specifically invites niche projects to go solo, with or without music21 as a dependency.
So where are those other projects?
They're listed here!


## Criteria

1. Preference for one language: it makes sense to have a single reference language for interoperability, comparison and more, though where the algorithms really only exist in other languages, we will link to them too.
2. That language is python, for all the usual reasons, chief among them being it popularity.
   - some designers of computer languages programming languages may find that a rather shallow reason,
   - but commitment to access and interoperability makes a language's existing popularity critically important.
   - e.g., imagine a student of music who gets that computing will open things up for them, but who also wants the time they invest in learning the ropes to be transferable in case they ever want or need to move away from music computing (imagine!).
3. We _actively prefer_ links to external libraries, though they must be:
   - Accompanied by a credible publication, or other demonstrable take-up by the community.
   - In python (as above)
   - Open source, well documented, etc.
   - Flat, flexible, and modular. We anticipate users seeking a specific algorithm,  
5. We provide implementations here where the above conditions are not (in our view) clearly and unambiguously met.
   - Examples include
     - those set out above: not in python, not implemented elsewhere
     - .
6. Design preferences (at least for new implementations):
   - Minimal dependencies / imports: typically `numpy`, `pandas`, `matplotlib` and nothing else.
   - Maximally modular and interoperable:
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


## Licence

(Almost) all the algorithms and resources here appear in published literature.

We cite those sources in the directory and defer to those authors for licence -
please refer to the source for details.

We sincerely believe that everything here is included legitimately.
Please get in touch if you have any questions or concerns.

For new content, where not specified directly in the document, the licenses is CC-by-SA.
I.e., if you contribute and do not specify otherwise, you agree to the CC-by-SA license or a more permissive one.
