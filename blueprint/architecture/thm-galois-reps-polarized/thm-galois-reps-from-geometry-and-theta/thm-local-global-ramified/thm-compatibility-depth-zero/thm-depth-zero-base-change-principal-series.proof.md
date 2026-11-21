+++
kind = "proof"
of   = "thm-depth-zero-base-change-principal-series"
uses = ["thm-hc-finiteness-gl", "thm-bz-finiteness", "thm-borel-casselman", "thm-chevalley-congruence-units",
        "thm-multiplicity-one-gl", "thm-depth-zero-from-support", "thm-depth-zero-jacquet-injective",
        "thm-depth-zero-support", "thm-zelevinsky-segments", "thm-geometric-lemma",
        "thm-geometric-lemma-filtration", "thm-artin-reciprocity", "thm-hasse-norm-quadratic",
        "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one", "thm-moy-prasad-jacquet"]
+++
The proof works with Jacquet modules of depth-zero representations: the
Moy–Prasad isomorphism, injectivity of the depth-zero Jacquet functor, the
geometric lemma of Bernstein and Zelevinsky and the theorem of Borel and
Casselman. *We read* the idea as the classical one: a depth-zero cuspidal
representation of $\GL_d(\Q_g)$ comes from a regular character of
$\mathbb F_{g^d}^\times$, which over a residue extension of degree divisible by $d$
splits into characters, so the base change becomes a principal series.
