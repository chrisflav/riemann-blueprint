+++
kind = "proof"
of   = "thm-local-global-ramified"
uses = ["thm-hecke-character-wd-above-l", "thm-hc-finiteness-gl", "thm-bz-finiteness",
        "thm-borel-casselman", "thm-galois-reps-csd-above-l", "thm-chebotarev-degree-one-frobenius", "thm-chebotarev-degree-one", "thm-chevalley-congruence-units",
        "thm-cusp-bounded-gl", "thm-multiplicity-one-gl", "thm-cuspidal-spectrum-gl",
        "thm-p-adic-monodromy", "thm-depth-zero-from-support", "thm-zelevinsky-segments",
        "thm-fontaine-bcris", "thm-gelfand-kazhdan", "thm-tadic-generic-unitary-dual", "thm-geometric-lemma",
        "thm-geometric-lemma-filtration", "thm-artin-reciprocity", "thm-hasse-norm-quadratic",
        "thm-hecke-l-adic-character-above-l", "thm-hecke-l-adic-character-crystalline",
        "thm-hecke-l-adic-character-de-rham", "thm-jacquet-irreducible-admissible", "thm-jacquet-shalika",
        "thm-jacquet-shalika-strong-mult-one", "thm-compatibility-depth-zero",
        "thm-bz-functors-finite-length"]
+++
The proof has three steps. The compatibility at unramified places first gives
compatibility at places where $\pi_w$ is a principal series from characters no
two of which differ by $|\cdot|$; with $l$-adic characters of Hecke characters
this includes the de Rham property above $l$. Then
[thm-compatibility-depth-zero] treats the depth-zero
places. Finally the clauses of [def-galois-reps-polarized] are assembled
place by place; at the places where they ask only for the dimension of the
Weil–Deligne representation there is nothing to prove, and the properties at
$l$ use the $p$-adic monodromy theorem ([thm-p-adic-monodromy]).
