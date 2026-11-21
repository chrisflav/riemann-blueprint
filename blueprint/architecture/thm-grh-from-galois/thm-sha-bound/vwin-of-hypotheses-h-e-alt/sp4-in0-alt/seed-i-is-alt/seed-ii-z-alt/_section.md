+++
id    = "seed-ii-z-alt"
kind  = "theorem"
title = "Seed points from mixed congruences"
lean  = ["UpperTheory.V.Z.Bc.seedII_Z_alt"]
uses  = ["abelian-de-rham", "algebraic-character-wd", "automorphic-forms-finite-gl",
         "bernstein-unitary-product-irreducible", "bernstein-zelevinsky-finiteness", "brauer-degree-zero",
         "chevalley-units", "clozel-cohomological", "clozel-purity", "cusp-rapid-decay", "cuspidal-spectrum-gl",
         "de-rham-potentially-semistable", "depth-zero-induction", "dual-abelian-scheme",
         "elliptic-main-theorem-cm", "ess-square-integrable-segments", "gelfand-kazhdan-dual", "geometric-lemma",
         "global-artin-reciprocity", "green-regular-characters", "grothendieck-deformation",
         "harish-chandra-finite", "hecke-l-adic-character-above", "hecke-tate-functional-equation",
         "hilbert-class-field-j", "jacquet-shalika", "lit-coh", "local-converse-gl", "moy-prasad-jacquet-iso",
         "partial-zeta-functional-equation", "ray-class-field-st", "siegel-klingen-deligne-ribet",
         "square-integrable-segment", "tempered-product-of-square-integrable", "thm-base-change-unitary"]
order = 10
+++
Assume the inputs of [seed-i-is-alt], the existence of Hilbert Eisenstein
series of weight one with their $q$-expansions, and the existence, for every
odd prime $p$, of Hilbert modular forms of level one and arbitrarily large
weight divisible by $p - 1$ whose $q$-expansion is congruent to $1$ modulo $p$
(lifts of the Hasse invariant). Assume also *automorphy of mixed inductions*: if
$r$ is the Galois representation of a Hilbert modular form over a totally
real field $k_0$, residually a non-split extension of $\xi$ by $1$, and $R$ is
the 4-dimensional representation of $G_\Q$ built from $r$ and the mixing
data of the tower, then $R$ is automorphic, with the expected weights, over
the CM field of the tower. Then the seeds of [seed-i-is-alt] exist.
