+++
id    = "lem-h2-tate-twists-bound"
kind  = "lemma"
title = "Second cohomology of Tate twists"
lean  = ["UpperTheory.V.ZK.lemmaK_litN_alt"]
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
Assume the standard inputs ([thm-hilbert-modular-inputs]). There
is a constant $C$ with the following property. Let $l$ be a prime and $L$ a
totally imaginary number field containing the $l$-th roots of unity (the
fourth roots if $l = 2$), and let $S$ be the set of places of $L$ above $l$.
Then for every $e \ge 1$ the group $H^2\big(G_{L,S}, \Z_l(e+1)\big)$ is finite and
$$\log\big|H^2\big(G_{L,S}, \Z_l(e+1)\big)\big| \le \exp\Big(\big(2e[L:\Q]\big)^C\log\big(2|D_L|\big)\Big),$$
where $D_L$ is the discriminant of $L$.
