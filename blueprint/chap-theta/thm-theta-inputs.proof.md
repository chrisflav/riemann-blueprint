+++
kind = "proof"
of   = "thm-theta-inputs"
uses = ["thm-siegel-weil-weil-range", "thm-siegel-weil-definite", "thm-siegel-main-theorem-hermitian",
        "thm-theta-tower-step-identities", "thm-theta-functionals-separate",
        "thm-downward-theta-lift-nonvanishing", "thm-rational-test-vectors-theta",
        "thm-indefinite-slope-bound", "prop-isometric-period-identity",
        "thm-bessel-transform-radial-space", "thm-offdiagonal-bound",
        "thm-counting-automorphic-forms-unitary", "lem-counting-constants-siegel-weil",
        "thm-counting-constant-mass-constant", "lem-valuations-level-primes"]
+++
The Siegel–Weil formula, in Weil's range ([thm-siegel-weil-weil-range]) and
for definite spaces ([thm-siegel-weil-definite]), runs through all the items.

1. The definite Siegel–Weil formula and the constant terms of theta
   integrals give the step identities ([thm-theta-tower-step-identities]).
2. Howe duality at unramified places, the Siegel–Weil formula and the
   ascent of Bessel periods up a tower give separation
   ([thm-theta-functionals-separate]).
3. The doubling method turns a pole of the partial $L$-function into a
   residue of a Siegel Eisenstein series, which is a theta integral from a
   smaller space; this gives the downward lifts
   ([thm-downward-theta-lift-nonvanishing]).
4. Unfolding the twisted theta integral into periods over a definite group
   gives the rational test vectors ([thm-rational-test-vectors-theta]).
5. Iterating the step identities along Witt towers bounds the square
   constants of theta lifts by $L$-values; with items 2 and 4 this gives
   the slope bound ([thm-indefinite-slope-bound]).
6. A diagonal estimate from the Siegel–Weil formula, the archimedean bounds
   that follow from [thm-bessel-transform-radial-space], and a period
   identity for real packages give the isometric period identity
   ([prop-isometric-period-identity]).
7. An abstract bound for a pairing over a CM field, whose inputs are
   archimedean models and counts of lattices, gives the off-diagonal bound
   ([thm-offdiagonal-bound]).
8. A kernel argument counts automorphic forms
   ([thm-counting-automorphic-forms-unitary]); Siegel's mass formula
   ([thm-siegel-main-theorem-hermitian]) supplies its volume step
   ([lem-counting-constants-siegel-weil]) and its constant
   ([thm-counting-constant-mass-constant]).
9. Katz's $p$-adic measures from CM theta functions give the valuation
   bounds ([lem-valuations-level-primes]).
