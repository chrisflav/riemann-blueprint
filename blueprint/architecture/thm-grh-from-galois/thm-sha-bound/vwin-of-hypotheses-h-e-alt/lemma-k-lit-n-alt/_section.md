+++
id    = "lemma-k-lit-n-alt"
kind  = "lemma"
title = "Second cohomology of Tate twists"
lean  = ["UpperTheory.V.ZK.lemmaK_litN_alt"]
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
Assume the standard inputs ([published-hypotheses-from-patching-alt]). There
is a constant $C$ with the following property. Let $l$ be a prime and $L$ a
totally imaginary number field containing the $l$-th roots of unity (the
fourth roots if $l = 2$), and let $S$ be the set of places of $L$ above $l$.
Then for every $e \ge 1$ the group $H^2\big(G_{L,S}, \Z_l(e+1)\big)$ is finite and
$$\log\big|H^2\big(G_{L,S}, \Z_l(e+1)\big)\big| \le \exp\Big(\big(2e[L:\Q]\big)^C\log\big(2|D_L|\big)\Big),$$
where $D_L$ is the discriminant of $L$.
