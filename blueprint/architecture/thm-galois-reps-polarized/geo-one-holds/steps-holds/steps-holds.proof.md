+++
kind = "proof"
of   = "steps-holds"
uses = ["algebraic-character-wd", "chevalley-units", "de-rham-potentially-semistable", "fontaine-bcris",
        "global-artin-reciprocity", "hecke-l-adic-character", "hecke-l-adic-character-de-rham",
        "projective-bundle-formula-vector-bundle-any-space", "proper-base-change"]
+++
Part 1 is linear algebra on the finite-dimensional space $V_\theta$. For part 2,
proper base change ([proper-base-change]) identifies the cohomology of $Z$
with that of its reduction, where the congruence relation acts. Part 3
combines [crys-step-holds], [jump-step-holds] and the theory of Fontaine's
ring $B_{\mathrm{cris}}$. For part 4, an algebraic Hecke character has an
$l$-adic Galois character by Artin reciprocity and Chevalley's theorem on
units; that character is de Rham, hence potentially semistable
([de-rham-potentially-semistable]), and crystalline where it is unramified.
