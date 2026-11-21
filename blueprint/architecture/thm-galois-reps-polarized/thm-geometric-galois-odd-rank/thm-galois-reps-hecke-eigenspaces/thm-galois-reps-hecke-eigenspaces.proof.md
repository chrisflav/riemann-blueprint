+++
kind = "proof"
of   = "thm-galois-reps-hecke-eigenspaces"
uses = ["thm-hecke-character-wd-above-l", "thm-chevalley-congruence-units", "thm-p-adic-monodromy", "thm-fontaine-bcris",
        "thm-artin-reciprocity", "thm-hecke-l-adic-character", "thm-hecke-l-adic-character-de-rham",
        "thm-projective-bundle-formula", "thm-proper-base-change"]
+++
Part 1 is linear algebra on the finite-dimensional space $V_\theta$. For part 2,
proper base change ([thm-proper-base-change]) identifies the cohomology of $Z$
with that of its reduction, where the congruence relation acts. Part 3
combines [thm-eigenspaces-crystalline], [thm-hodge-tate-weights-eigenspaces] and the theory of Fontaine's
ring $B_{\mathrm{cris}}$. For part 4, an algebraic Hecke character has an
$l$-adic Galois character by Artin reciprocity and Chevalley's theorem on
units; that character is de Rham, hence potentially semistable
([thm-p-adic-monodromy]), and crystalline where it is unramified.
