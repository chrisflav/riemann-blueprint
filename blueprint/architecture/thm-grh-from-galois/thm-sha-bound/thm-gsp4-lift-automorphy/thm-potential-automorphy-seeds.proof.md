+++
kind = "proof"
of   = "thm-potential-automorphy-seeds"
uses = ["thm-hilbert-modular-inputs", "thm-de-rham-abelian-schemes", "thm-p-adic-monodromy", "thm-dual-abelian-scheme", "def-galois-cohomology-inputs", "thm-base-change-unitary", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-cusp-bounded-gl", "thm-multiplicity-one-gl", "thm-geometric-lemma-filtration", "thm-hasse-norm-quadratic", "thm-automorphic-induction-quadratic", "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika-strong-mult-one", "thm-hilbert-mixed-weights", "thm-local-parameters-exist", "thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl", "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-brauer-induction-degree-zero", "thm-chevalley-congruence-units", "thm-clozel-cohomological", "thm-clozel-purity", "thm-cusp-rapid-decay", "thm-cuspidal-spectrum-gl", "thm-depth-zero-from-support", "thm-shimura-main-theorem-cm", "thm-zelevinsky-segments", "thm-gelfand-kazhdan", "thm-geometric-lemma", "thm-artin-reciprocity", "thm-green-regular-characters", "thm-grothendieck-messing", "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-functional-equation-cm", "thm-singular-moduli-class-number", "thm-jacquet-shalika", "thm-henniart-local-converse", "thm-moy-prasad-jacquet", "thm-partial-zeta-functional-equation", "thm-ray-class-field", "thm-siegel-klingen-rationality", "thm-square-integrable-segment", "thm-tempered-products"]
+++
[thm-hilbert-mixed-weights] produces a Hilbert modular form over a totally
real field $k_0$ whose Galois representation $r$ is residually $1 \oplus \xi$,
ordinary at $l$ with different weights at two sets of places above $l$.
Ribet's construction gives a lattice on which $r$ is a non-split extension of
$\xi$ by $1$. Let $R$ be the 4-dimensional representation of $G_\Q$ built from
$r$ and the mixing data of the tower. Then $R$ is automorphic, with the
expected weights, over the CM field of the tower: this follows from quadratic
base change from real to imaginary quadratic fields and cyclic base change in
rank two (both among the results of [thm-hilbert-modular-inputs]) and
automorphic induction ([thm-automorphic-induction-quadratic]). The
pseudo-representation of $R$ over $F$ is the required seed.
