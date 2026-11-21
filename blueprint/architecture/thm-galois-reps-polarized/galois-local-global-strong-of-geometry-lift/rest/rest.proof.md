+++
kind = "proof"
of   = "rest"
uses = ["algebraic-character-wd", "automorphic-forms-finite-gl", "bernstein-zelevinsky-finiteness",
        "borel-casselman", "car-u-alt", "cheb", "chebotarev-degree-one", "chevalley-units",
        "cusp-forms-bounded-gl", "cuspidal-multiplicity-one", "cuspidal-spectrum-gl",
        "de-rham-potentially-semistable", "depth-zero-induction", "ess-square-integrable-segments",
        "fontaine-bcris", "gelfand-kazhdan-dual", "generic-unitary-dual-gl", "geometric-lemma",
        "geometric-lemma-filtration", "global-artin-reciprocity", "hasse-norm-st",
        "hecke-l-adic-character-above", "hecke-l-adic-character-crystalline",
        "hecke-l-adic-character-de-rham", "irreducible-admissible-gl", "jacquet-shalika",
        "jacquet-shalika-rigidity", "local-global-compat-at-iwahori-fixed-of-unlinked",
        "standard-functors-finite-length"]
+++
The proof has three steps. The compatibility at unramified places first gives
compatibility at places where $\pi_w$ is a principal series from characters no
two of which differ by $|\cdot|$; with $l$-adic characters of Hecke characters
this includes the de Rham property above $l$. Then
[local-global-compat-at-iwahori-fixed-of-unlinked] treats the depth-zero
places. Finally the clauses of [def-galois-reps-polarized] are assembled
place by place; at the places where they ask only for the dimension of the
Weil–Deligne representation there is nothing to prove, and the properties at
$l$ use the $p$-adic monodromy theorem ([de-rham-potentially-semistable]).
