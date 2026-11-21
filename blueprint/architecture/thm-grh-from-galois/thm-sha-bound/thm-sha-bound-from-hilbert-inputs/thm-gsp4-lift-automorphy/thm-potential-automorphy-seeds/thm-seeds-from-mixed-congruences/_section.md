+++
id    = "thm-seeds-from-mixed-congruences"
kind  = "theorem"
title = "Seed points from mixed congruences"
lean  = ["UpperTheory.V.Z.Bc.seedII_Z_alt"]
uses  = ["thm-de-rham-abelian-schemes", "thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl",
         "thm-bernstein-unitary-product", "thm-bz-finiteness", "thm-brauer-induction-degree-zero",
         "thm-chevalley-congruence-units", "thm-clozel-cohomological", "thm-clozel-purity", "thm-cusp-rapid-decay", "thm-cuspidal-spectrum-gl",
         "thm-p-adic-monodromy", "thm-depth-zero-from-support", "thm-dual-abelian-scheme",
         "thm-shimura-main-theorem-cm", "thm-zelevinsky-segments", "thm-gelfand-kazhdan", "thm-geometric-lemma",
         "thm-artin-reciprocity", "thm-green-regular-characters", "thm-grothendieck-messing",
         "thm-hc-finiteness-unitary", "thm-hecke-l-adic-character-above-l", "thm-hecke-functional-equation-cm",
         "thm-singular-moduli-class-number", "thm-jacquet-shalika", "def-galois-cohomology-inputs", "thm-henniart-local-converse", "thm-moy-prasad-jacquet",
         "thm-partial-zeta-functional-equation", "thm-ray-class-field", "thm-siegel-klingen-rationality",
         "thm-square-integrable-segment", "thm-tempered-products", "thm-base-change-unitary"]
order = 10
+++
Assume the inputs of [thm-potential-automorphy-seeds], the existence of Hilbert Eisenstein
series of weight one with their $q$-expansions, and the existence, for every
odd prime $p$, of Hilbert modular forms of level one and arbitrarily large
weight divisible by $p - 1$ whose $q$-expansion is congruent to $1$ modulo $p$
(lifts of the Hasse invariant). Assume also *automorphy of mixed inductions*: if
$r$ is the Galois representation of a Hilbert modular form over a totally
real field $k_0$, residually a non-split extension of $\xi$ by $1$, and $R$ is
the 4-dimensional representation of $G_\Q$ built from $r$ and the mixing
data of the tower, then $R$ is automorphic, with the expected weights, over
the CM field of the tower. Then the seeds of [thm-potential-automorphy-seeds] exist.
