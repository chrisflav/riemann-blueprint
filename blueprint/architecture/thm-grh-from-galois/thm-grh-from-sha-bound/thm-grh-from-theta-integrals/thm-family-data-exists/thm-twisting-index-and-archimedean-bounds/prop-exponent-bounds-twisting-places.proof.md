+++
kind = "proof"
of   = "prop-exponent-bounds-twisting-places"
uses = ["thm-hc-finiteness-gl", "thm-bz-finiteness", "thm-borel-casselman", "thm-galois-reps-csd-above-l", "thm-cusp-bounded-gl", "thm-zelevinsky-segments", "lem-exponent-bounds-from-lattice-inclusions", "thm-fontaine-bcris", "thm-geometric-lemma", "thm-hasse-norm-quadratic", "thm-jacquet-irreducible-admissible", "lem-local-models-weight-range", "thm-labesse-base-change", "thm-bhatt-scholze-coefficients", "thm-chebotarev-degree-one", "thm-clozel-cohomological", "thm-galois-reps-polarized-cuspidal", "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-above-l"]
+++
Apply [lem-exponent-bounds-from-lattice-inclusions]. Its numerical inputs and its exponent
sums are proved directly. The cutting inequality comes from the exact
exponents of Weyl lattices. Its local models are
[lem-local-models-weight-range]; the Galois input there comes from
Clozel's theorem on cohomological representations [thm-clozel-cohomological],
base change for definite unitary groups [thm-labesse-base-change], the Galois
representations of polarized cuspidal representations
[thm-galois-reps-polarized-cuspidal] and the $l$-adic characters of
algebraic Hecke characters ([thm-hecke-l-adic-character],
[thm-hecke-l-adic-character-above-l]), with Chebotarev's theorem for primes
of degree one [thm-chebotarev-degree-one] and the theorem of Bhatt and
Scholze [thm-bhatt-scholze-coefficients].
