+++
kind = "proof"
of   = "prop-exponent-bounds-twisting-places"
uses = ["thm-hc-finiteness-gl", "thm-bz-finiteness", "thm-borel-casselman", "thm-galois-reps-csd-above-l", "thm-cusp-bounded-gl", "thm-zelevinsky-segments", "lem-exponent-bounds-from-lattice-inclusions", "thm-fontaine-bcris", "thm-geometric-lemma", "thm-hasse-norm-quadratic", "thm-jacquet-irreducible-admissible", "lem-local-models-weight-range"]
+++
Apply [lem-exponent-bounds-from-lattice-inclusions]. Its numerical inputs and its exponent
sums are proved directly. The cutting inequality comes from the exact
exponents of Weyl lattices. Its local models are
[lem-local-models-weight-range]; the Galois input
there comes from base change, the Galois representations of polarized
cuspidal representations and the $l$-adic Hecke characters.
